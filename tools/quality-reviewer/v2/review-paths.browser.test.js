'use strict';
// Supply existing private previews; never creates reviews or deliverables.
// NODE_PATH can point to the installed Playwright library. Chrome must be installed.
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright');
const { assertPrivateOutput } = require('./review-view');
const folder = path.resolve(process.argv[2] || '');
assertPrivateOutput(path.join(folder, 'check.json'));
(async () => {
  const browser = await chromium.launch({ headless: true, channel: 'chrome' });
  try {
    for (const audience of ['student','lead']) {
      const context = await browser.newContext({ acceptDownloads: true, viewport: {width:1440,height:1000} });
      const page = await context.newPage();
      const errors = [], requests = [];
      page.on('pageerror', e => errors.push(e.message)); page.on('request', r => requests.push(r.url()));
      await page.goto(pathToFileURL(path.join(folder,audience + '-review.html')).href);
      const data = await page.locator('#review-data').textContent().then(JSON.parse);
      assert.equal(await page.locator('.finding').count(),data.findings.length);
      assert.equal(await page.locator(audience === 'lead' ? '.student-tools' : '.lead-tools').count(),0);
      assert.equal(await page.locator('.mode-switch').count(),0);
      assert.equal(await page.locator('.review-section h2').first().textContent(),'Strengths');
      assert.equal(await page.locator('.evidence-links button').count(),data.findings.reduce((n,f)=>n+f.pages.length,0));
      if (process.argv[3]) {
        const evidence = JSON.parse(fs.readFileSync(process.argv[3],'utf8'));
        await page.locator('#source-pdf').setInputFiles(evidence.source);
        await page.waitForFunction(()=>document.getElementById('status').textContent.includes('verified and attached'));
        await page.locator('#source-pdf').setInputFiles({name:'wrong.pdf',mimeType:'application/pdf',buffer:Buffer.from('Invalid-file negative software check')});
        await page.waitForFunction(()=>document.getElementById('status').textContent.includes('does not match'));
      }
      for (const finding of data.findings) {
        assert.equal(await page.locator('#'+finding.id+' h3').textContent(),finding.title);
        assert.deepEqual(await page.locator('#'+finding.id+' dd').allTextContents(),finding.fields.map(f=>f.text.trim()));
      }
      const save = async button => {
        const pending = page.waitForEvent('download'); await page.locator(button).click();
        const download = await pending; const target = path.join(folder,audience + '-' + download.suggestedFilename()); await download.saveAs(target); return target;
      };
      assert.equal(fs.readFileSync(await save('#download-review'),'utf8'),data.rawReview);
      if (audience === 'student') {
        await page.locator('.student-tools summary').first().click();
        await page.locator('#response-f1').fill('Private browser test: check my choice against the cited evidence.');
      } else {
        await page.locator('#action-f1').selectOption('keep');
        await page.locator('#note-f1').fill('Private browser test reason.');
        await page.locator('#lead-name').fill('Browser test operator');
        assert.match(await page.locator('#unresolved').textContent(),new RegExp('^'+(data.findings.length-1)+' '));
      }
      const recordPath = await save('#save-notes');
      const record = JSON.parse(fs.readFileSync(recordPath,'utf8'));
      assert.equal(record.audience,audience); assert.equal(record.reviewHash,data.sourceHash); assert.equal(record.keys,data.keys);
      assert.equal(record.promptVersion,data.promptVersion); assert.equal(record.sourceMode,data.mode);
      assert.equal('lead' in record,audience==='lead');
      assert.deepEqual(Object.keys(record.findings.f1).sort(),audience==='lead'?['action','note']:['response']);
      const input = audience==='lead'?'#note-f1':'#response-f1';
      const expected = await page.locator(input).inputValue();
      await page.locator(input).fill('Unsaved change');
      const cancelled = page.waitForEvent('dialog').then(dialog=>dialog.dismiss());
      await page.locator('#restore-notes').setInputFiles(recordPath); await cancelled;
      await page.waitForFunction(()=>document.getElementById('restore-notes').value==='');
      assert.equal(await page.locator(input).inputValue(),'Unsaved change');
      const accepted = page.waitForEvent('dialog').then(dialog=>dialog.accept());
      await page.locator('#restore-notes').setInputFiles(recordPath); await accepted;
      await page.waitForFunction(()=>document.getElementById('status').textContent.includes('restored'));
      assert.equal(await page.locator(input).inputValue(),expected);
      const wrong = {...record,audience:audience==='lead'?'student':'lead'};
      await page.locator('#restore-notes').setInputFiles({name:'wrong.json',mimeType:'application/json',buffer:Buffer.from(JSON.stringify(wrong))});
      await page.waitForFunction(()=>document.getElementById('status').textContent.includes('Could not restore'));
      assert.equal(await page.locator(input).inputValue(),expected);
      await page.keyboard.press('Control+Home'); await page.locator('body').click({position:{x:2,y:2}}); await page.keyboard.press('Tab');
      assert.equal(await page.evaluate(()=>document.activeElement.className),'skip');
      await page.keyboard.press('Enter'); assert.equal(await page.evaluate(()=>document.activeElement.id),'review');
      await page.locator('#theme').click(); assert.equal(await page.locator('html').getAttribute('data-theme'),'dark'); await page.locator('#theme').click();
      await page.evaluate(()=>window.scrollTo(0,0));
      await page.screenshot({path:path.join(folder,audience+'-desktop.png')});
      await page.setViewportSize({width:390,height:844});
      assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
      await page.evaluate(()=>window.scrollTo(0,0));
      await page.screenshot({path:path.join(folder,audience+'-phone.png')});
      await page.emulateMedia({media:'print'}); await page.evaluate(()=>window.dispatchEvent(new Event('beforeprint')));
      assert(await page.locator('.print-value').allTextContents().then(xs=>xs.includes(expected)));
      assert.equal(await page.locator('.finding').count(),data.findings.length);
      if(audience==='lead') assert.equal(await page.locator('#lead-summary').isVisible(),true);
      await page.pdf({path:path.join(folder,audience+'-print.pdf'),format:'A4',printBackground:true});
      await page.evaluate(()=>window.dispatchEvent(new Event('afterprint')));
      assert.deepEqual(errors,[]); assert(requests.every(url=>url.startsWith('file:')||url.startsWith('blob:')));
      await context.close();
      console.log(audience + ': content/evidence, audience separation, export/restore/cancel/rejection, keyboard, desktop/phone, theme, print, no external requests passed.');
    }
  } finally { await browser.close(); }
})().catch(error=>{console.error(error);process.exitCode=1;});
