/* Local-only display and human notes. The frozen review is never mutated. */
(() => {
  'use strict';
  const review = JSON.parse(document.getElementById('review-data').textContent);
  const byId = id => document.getElementById(id);
  const node = (tag, cls, text) => { const el = document.createElement(tag); if (cls) el.className = cls; if (text !== undefined) el.textContent = text; return el; };
  const status = text => { byId('status').textContent = text; };
  const audience = document.body.dataset.audience;
  const notes = { recordVersion: 'review-notes-2', audience, promptVersion: review.promptVersion, sourceMode: review.mode, provenance: review.provenance || null, reviewHash: review.sourceHash, keys: review.keys, ...(audience === 'lead' ? { lead: { name: '', note: '' } } : {}), findings: {} };
  let pdfUrl = null, dirty = false;
  const inputs = {};
  const sectionNames = { 'Review context': 'Context', 'BEFORE YOU USE THIS': 'Review notes',
    'WHAT WORKS': 'Strengths', 'FINDINGS, IN ORDER': 'Findings', 'WHAT TO FIX, IN ORDER': 'Findings',
    'WHAT THIS REVIEW COULD NOT JUDGE': 'Limits', 'QUESTIONS WORTH ASKING THE TEAM': 'Questions',
    'HOW TO CHECK THIS FEEDBACK': 'Source checks', 'AFTER THE FULL REVIEW': 'Discussion', 'PASTE-BACK RECORD': 'Review record' };
  if (window.matchMedia('(max-width:850px)').matches) document.querySelectorAll('.sidebar-group').forEach(el => { el.open = false; });
  const modified = () => { dirty = true; };
  function pageButton(page) {
    const el = node('button', '', 'PDF ' + page);
    el.type = 'button';
    el.addEventListener('click', () => {
      if (!pdfUrl) { status('Attach the original PDF to open page ' + page + '. It stays on this device.'); byId('source-pdf').focus(); return; }
      window.open(pdfUrl + '#page=' + page, '_blank', 'noopener');
    });
    return el;
  }
  byId('provenance').textContent = review.provenance || 'Completed ' + audience + ' review. No new analysis performed.';
  byId('review-title').textContent = review.title;
  byId('review-meta').textContent = review.pageCount + ' source pages · ' + review.mode + ' review · ' + review.keys;
  byId('source-count').textContent = review.pageCount + ' pages';
  byId('integrity').textContent = review.evidenceStatus + ' Original review SHA-256: ' + review.sourceHash;
  const cited = new Set(review.findings.flatMap(f => f.pages));
  for (const p of review.includedPages) {
    const b = pageButton(p); b.textContent = p;
    if (cited.has(p)) b.classList.add('cited');
    b.setAttribute('aria-label', 'PDF page ' + p + (cited.has(p) ? ', cited by a finding' : ', not assessed by this view'));
    byId('page-nav').append(b);
  }
  const ordered = [...review.sections].sort((a,b) => (a.title === 'WHAT WORKS' ? -1 : b.title === 'WHAT WORKS' ? 1 : 0));
  for (const [index, section] of ordered.entries()) {
    const isFindings = ['FINDINGS, IN ORDER', 'WHAT TO FIX, IN ORDER'].includes(section.title);
    const isContext = section.title === 'Review context' || section.title === 'BEFORE YOU USE THIS';
    const sectionEl = node(isContext ? 'details' : 'section', 'review-section' + (section.title === 'WHAT WORKS' ? ' strengths' : '') + (isContext ? ' context' : ''));
    sectionEl.id = 'section-' + index;
    const heading = node(isContext ? 'summary' : 'h2', '', sectionNames[section.title] || section.title);
    sectionEl.append(heading);
    const link = node('a', '', heading.textContent); link.href = '#' + sectionEl.id;
    if (isContext) link.addEventListener('click', () => { sectionEl.open = true; });
    byId('section-nav').append(link);
    if (!isFindings) sectionEl.append(node('div', 'prose', section.text.trim()));
    else {
      sectionEl.append(node('div', 'prose', section.intro));
      if (!review.findings.length) sectionEl.append(node('p', 'muted', 'No findings were recorded. There are no mandatory fixes in this view.'));
      for (const f of review.findings) {
        const article = node('article', 'finding'); article.id = f.id;
        const kicker = node('div', 'finding-kicker'); kicker.append(node('span', '', 'FINDING ' + f.number));
        const severity = node('span', 'severity', f.severity); severity.dataset.level = f.severity; kicker.append(severity);
        article.append(kicker, node('h3', '', f.title));
        // Standardize display labels only. Field content and the saved review are not rewritten.
        if (f.fields) {
          const fields = node('dl', 'finding-fields');
          for (const field of f.fields) fields.append(node('dt', '', field.label), node('dd', 'prose', field.text.trim()));
          article.append(fields);
        } else article.append(node('div', 'prose', f.text.slice(f.text.indexOf('\n') + 1)));
        const links = node('div', 'evidence-links'); f.pages.forEach(p => links.append(pageButton(p))); article.append(links);
        notes.findings[f.id] = audience === 'lead' ? { action: '', note: '' } : { response: '' };
        let response, action, note;
        if (audience === 'student') {
        const student = node('details', 'human-tools student-tools');
        student.append(node('summary', '', 'Discuss this finding'));
        const label = node('label', '', 'Your reasoning and evidence'); response = node('textarea'); response.rows = 3; response.id = 'response-' + f.id; label.htmlFor = response.id; label.append(response);
        response.addEventListener('input', () => { notes.findings[f.id].response = response.value; modified(); }); student.append(label);
        const copy = node('button', '', 'Copy discussion prompt'); copy.type = 'button'; copy.addEventListener('click', async () => {
          const text = 'Help me reason through this finding without writing slide text for me.\n\n' + f.text + '\n\nMy reasoning:\n' + response.value;
          try { await navigator.clipboard.writeText(text); status('Discussion prompt copied. Paste it into your review chat.'); }
          catch (_) { download('discussion-' + f.id + '.txt', text, 'text/plain'); status('Clipboard unavailable. Discussion prompt downloaded.'); }
        }); student.append(copy); article.append(student);
        } else {
        const lead = node('section', 'human-tools lead-tools');
        const actionLabel = node('label', '', 'Decision'); action = node('select'); action.id = 'action-' + f.id; actionLabel.htmlFor = action.id;
        for (const [value, text] of [['', 'Not decided'], ['keep', 'Keep'], ['ask', 'Ask'], ['cut', 'Cut']]) { const option = node('option', '', text); option.value = value; action.append(option); }
        actionLabel.append(action); action.addEventListener('change', () => { notes.findings[f.id].action = action.value; modified(); updateUnresolved(); });
        const noteLabel = node('label', '', 'Reason or question'); note = node('textarea'); note.id = 'note-' + f.id; noteLabel.htmlFor = note.id; note.rows = 2; noteLabel.append(note);
        note.addEventListener('input', () => { notes.findings[f.id].note = note.value; modified(); updateUnresolved(); }); lead.append(actionLabel, noteLabel); article.append(lead);
        }
        inputs[f.id] = { action, note, response }; sectionEl.append(article);
      }
    }
    byId('review-content').append(sectionEl);
  }
  function updateUnresolved() {
    if (audience !== 'lead') return;
    const unresolved = Object.values(notes.findings).filter(n => !n.action || n.action === 'ask' || !n.note.trim()).length;
    byId('unresolved').textContent = unresolved + ' findings need a decision, reason or answer.';
  }
  updateUnresolved();
  if (audience === 'lead') for (const [id, key] of [['lead-name','name'], ['lead-note','note']]) byId(id).addEventListener('input', () => { notes.lead[key] = byId(id).value; modified(); });
  function download(name, text, mime) {
    const url = URL.createObjectURL(new Blob([text], { type: mime })); const a = node('a'); a.href = url; a.download = name; a.click(); setTimeout(() => URL.revokeObjectURL(url), 30000);
  }
  byId('download-review').onclick = () => download('original-review.md', review.rawReview, 'text/markdown');
  byId('save-notes').onclick = () => { download(audience + '-record.json', JSON.stringify(notes, null, 2), 'application/json'); dirty = false; status('Notes exported. Keep the downloaded file in your private workspace.'); };
  byId('restore-notes').onchange = async event => {
    const file = event.target.files[0]; if (!file) return;
    try {
      const restored = JSON.parse(await file.text());
      if (restored.recordVersion !== notes.recordVersion || restored.audience !== audience || restored.promptVersion !== notes.promptVersion || restored.sourceMode !== notes.sourceMode || restored.reviewHash !== notes.reviewHash || restored.keys !== notes.keys || !restored.findings) throw new Error('This notes file does not belong to this review.');
      if (audience === 'lead' && (!restored.lead || typeof restored.lead.name !== 'string' || typeof restored.lead.note !== 'string')) throw new Error('Invalid lead notes.');
      if (Object.keys(restored.findings).sort().join() !== Object.keys(notes.findings).sort().join()) throw new Error('Finding IDs do not match.');
      for (const f of review.findings) {
        const n = restored.findings[f.id];
        if (!n || (audience === 'lead' ? !['', 'keep', 'ask', 'cut'].includes(n.action) || typeof n.note !== 'string' : typeof n.response !== 'string')) throw new Error('Invalid finding notes.');
      }
      if (dirty && !window.confirm('Replace your unsaved notes with this file?')) return;
      if (audience === 'lead') notes.lead = { name: restored.lead.name, note: restored.lead.note };
      if (audience === 'lead') { byId('lead-name').value = notes.lead.name; byId('lead-note').value = notes.lead.note; }
      for (const f of review.findings) { const n = restored.findings[f.id]; notes.findings[f.id] = audience === 'lead' ? { action: n.action, note: n.note } : { response: n.response }; for (const key of ['action', 'note', 'response']) if (inputs[f.id][key]) inputs[f.id][key].value = n[key]; }
      updateUnresolved(); dirty = false; status('Your notes were restored. The original review is unchanged.');
    } catch (error) { status('Could not restore notes: ' + error.message); }
    finally { event.target.value = ''; }
  };
  byId('source-pdf').onchange = async event => {
    const f = event.target.files[0]; if (!f) return;
    if (pdfUrl) URL.revokeObjectURL(pdfUrl); pdfUrl = null;
    if (!/\.pdf$/i.test(f.name)) { status('Choose the original PDF.'); return; }
    try {
      if (review.documentHash) {
        const bytes = await crypto.subtle.digest('SHA-256', await f.arrayBuffer());
        const actual = Array.from(new Uint8Array(bytes), b => b.toString(16).padStart(2, '0')).join('');
        if (actual !== review.documentHash) { status('This PDF does not match the source used for this review.'); return; }
      }
      // Ignore a completed read if the user selected another file while hashing.
      if (event.target.files[0] !== f) return;
      pdfUrl = URL.createObjectURL(f);
      status(review.documentHash ? 'Original PDF verified and attached locally.' : 'PDF attached locally. Source identity was not recorded; check the file yourself.');
    } catch (_) { status('Could not verify this PDF locally. Keep using the original file separately.'); }
  };
  byId('theme').onclick = () => { const dark = document.documentElement.dataset.theme !== 'dark'; document.documentElement.dataset.theme = dark ? 'dark' : 'light'; byId('theme').textContent = dark ? 'Light appearance' : 'Dark appearance'; byId('theme').setAttribute('aria-pressed', String(dark)); };
  byId('print').onclick = () => window.print();
  let printActive = false;
  window.addEventListener('beforeprint', () => {
    if (printActive) return;
    printActive = true;
    document.querySelectorAll('details').forEach(el => { el.dataset.wasOpen = String(el.open); el.open = true; });
    document.querySelectorAll('textarea,input[type=text],select').forEach(input => {
      const copy = node('div', 'print-value', input.tagName === 'SELECT' ? input.selectedOptions[0].textContent : (input.value || 'Not recorded'));
      input.insertAdjacentElement('afterend', copy);
    });
  });
  window.addEventListener('afterprint', () => {
    document.querySelectorAll('.print-value').forEach(el => el.remove());
    document.querySelectorAll('details').forEach(el => { el.open = el.dataset.wasOpen === 'true'; delete el.dataset.wasOpen; });
    printActive = false;
  });
  window.addEventListener('beforeunload', event => { if (dirty) { event.preventDefault(); event.returnValue = ''; } });
})();
