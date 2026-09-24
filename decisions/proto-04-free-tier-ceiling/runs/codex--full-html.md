<script>
const REVIEW = {
  client: "Client E",
  artifact: "final recommendation deck",
  slides: 10,
  aiLevel: "Needs targeted revision",
  effort: "2-3 days",
  confidence:"Medium",

  criteria: [
    {name:"Analysis and insight", score:"1/4", state:"bad"},
    {name:"Evidence quality", score:"2/4", state:"mid"},
    {name:"Risks and uncertainty", score:"2/4", state:"mid"},
    {name:"Feasibility and implementation", score:"2/4", state:"mid"},
    {name:"Client decision", score:"3/4", state:"ok"},
    {name:"Problem framing", score:"3/4", state:"ok"}
  ],

  sections: [
    {label:"Decision", span:2},
    {label:"Case for membership", span:3},
    {label:"Offer design", span:2},
    {label:"Economics and risk", span:2},
    {label:"Implementation", span:1}
  ],

  tiles: {7:"partial", 8:"critical", 9:"critical", 10:"critical"},

  callouts: [
    {at:7, state:"partial", t:"Capacity claim", sub:"workload is not measured"},
    {at:8, state:"critical", t:"Conversion case", sub:"uses the wrong comparator"},
    {at:9, state:"critical", t:"Pilot sample", sub:"selects the warmest contacts"},
    {at:10, state:"critical", t:"Launch gate", sub:"5% has no basis"}
  ],

  connectors: [],

  main: {
    title: "The full-launch gate rests on a biased pilot and ungrounded conversion thresholds.",
    quotes: [
      {slide:8, text:"The 8% assumption is conservative against the 32% attendance rate and is the main thing to test."},
      {slide:9, text:"A soft launch to the most engaged 200 contacts tests both before the full launch."},
      {slide:10, text:"Month three: full launch if the soft launch clears 5%."}
    ],
    why: "The board could approve a full rollout that produces too little net income to justify the work. The selected pilot group is likely to overstate full-list conversion, while neither 8% nor the 5% gate is tied to costs or the income-diversification need."
  },

  fixes: [
    {do:"Define the board's decision rule from net value, not conversion alone.", why:"Tie the launch gate to incremental revenue, benefit costs, coordinator time and the income-diversification target."},
    {do:"Redesign the soft launch so it can test the full-list case.", why:"Use a representative or split sample and measure conversion, administration time and benefit-delivery load."},
    {do:"Separate the forecast, target and launch gate.", why:"Label the 8% case as an assumption, test a range and explain why the chosen gate is sufficient."},
    {do:"Prove the membership offer fits existing capacity.", why:"Estimate recurring work for booking, events, discounts, administration and renewals, then reduce the offer if it does not fit."},
    {do:"Run a visual and source-link QA on the original deck.", why:"Only extracted text was available, so chart readability, slide hierarchy and visible links between claims and sources were not assessed."}
  ],

  findings: [{
    principle: "Use decision-linked test thresholds",
    see: "The deck calls 8% conservative by comparing it with event attendance, then tests on the 200 most engaged contacts and allows a full launch at 5%. It does not tie either conversion rate to net income, staff cost or a diversification need.",
    quotes: [
      {slide:8, text:"The 8% assumption is conservative against the 32% attendance rate and is the main thing to test."},
      {slide:9, text:"A soft launch to the most engaged 200 contacts tests both before the full launch."},
      {slide:10, text:"Month two: review conversion against the 8% target."},
      {slide:10, text:"Month three: full launch if the soft launch clears 5%."}
    ],
    why: "The board could scale on a biased result and a threshold with no economic meaning. A 5% result may still be unattractive once member benefits and coordinator time are counted.",
    reflect: "What minimum net income or diversification gain would justify the coordinator's time, and what pilot sample would predict conversion across the full mailing list?",
    fix: "Build the go or no-go rule from the minimum acceptable net contribution and workload. Test it on a representative or segmented sample, then show low, base and high conversion cases."
  },{
    principle: "Test the binding capacity constraint",
    see: "The deck states that the benefits use existing capacity and assigns the launch to the coordinator, while treating staff strain as an assumption. It gives no workload estimate or capacity measure for priority booking, two events, discounts, administration and renewals.",
    quotes: [
      {slide:7, text:"These use capacity Client E already has."},
      {slide:9, text:"We assume the mailing list is accurate and that members-only events do not strain staff."},
      {slide:10, text:"The Client E coordinator owns the launch."}
    ],
    why: "Client E could commit its part-time coordinator to benefits the organisation cannot deliver reliably. That would change the offer, the timing or the decision to proceed and would put member trust at risk.",
    reflect: "Which recurring tasks does the membership create, how many hours will each require and what existing work will move if demand is higher than expected?",
    fix: "Map the work by launch and steady-state task, assign hours and capacity limits and include a stop or simplify trigger in the pilot."
  }]
};
</script>
<title>__CLIENT__ deliverable review</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Public+Sans:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap">
<style>
:root{--bg:#EFF1EE;--card:#FFF;--sunk:#F4F7F1;--ink:#1B1F19;--body:#3A4136;--muted:#6F776A;
--rule:#DEE3D9;--green:#2E7D32;--gf:#78B038;--gs:#EAF3DC;--red:#A8402C;--rs:#FBEDE9;
--amber:#8A6510;--as:#FAF1DC;--sh:0 1px 2px rgba(27,31,25,.05),0 6px 20px -12px rgba(27,31,25,.2);}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#101208;--card:#181B12;
--sunk:#1E2218;--ink:#E9EDE1;--body:#C4CCB9;--muted:#8C9482;--rule:#2B3123;--green:#9BCF52;
--gf:#78B038;--gs:#212A14;--red:#E28C74;--rs:#2E1913;--amber:#D3A54A;--as:#2A2110;
--sh:0 1px 2px rgba(0,0,0,.4),0 8px 24px -14px rgba(0,0,0,.7);}}
:root[data-theme="dark"]{--bg:#101208;--card:#181B12;--sunk:#1E2218;--ink:#E9EDE1;--body:#C4CCB9;
--muted:#8C9482;--rule:#2B3123;--green:#9BCF52;--gf:#78B038;--gs:#212A14;--red:#E28C74;
--rs:#2E1913;--amber:#D3A54A;--as:#2A2110;--sh:0 1px 2px rgba(0,0,0,.4),0 8px 24px -14px rgba(0,0,0,.7);}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--body);margin:0;font-family:"Public Sans",system-ui,sans-serif;font-size:15px;line-height:1.55;-webkit-font-smoothing:antialiased}
.wrap{max-width:880px;margin:0 auto;padding:16px 16px 60px;display:flex;flex-direction:column;gap:13px}
.card{background:var(--card);border-radius:9px;box-shadow:var(--sh);padding:18px 20px}
h2{font-size:.7rem;letter-spacing:.13em;text-transform:uppercase;color:var(--muted);margin:0 0 11px;font-weight:600;font-family:"JetBrains Mono",monospace}
h3{margin:0;font-size:1rem;color:var(--ink);font-weight:600;line-height:1.35}
p{margin:0}
.bar{display:flex;align-items:center;gap:13px;flex-wrap:wrap}
.brand{font-weight:700;color:var(--ink)}.brand em{font-style:normal;color:var(--green)}
.meta{color:var(--muted);font-size:.8rem;line-height:1.35}
.tabs{margin-left:auto;display:flex;background:var(--sunk);border-radius:7px;padding:3px;gap:2px}
.tab{padding:6px 14px;border-radius:5px;font-size:.85rem;color:var(--muted);border:none;background:none;cursor:pointer;font-family:inherit}
.tab[aria-selected=true]{background:var(--card);color:var(--ink);font-weight:600;box-shadow:0 1px 2px rgba(0,0,0,.09)}
.pills{display:flex;gap:9px;flex-wrap:wrap}
.pill{border:1px solid var(--rule);border-radius:7px;padding:9px 14px;flex:1;min-width:130px}
.pill .k{font-size:.63rem;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);font-family:"JetBrains Mono",monospace;display:block;margin-bottom:5px}
.pill .v{font-size:1.05rem;color:var(--ink);font-weight:600;display:flex;align-items:center;gap:7px}
.dot{width:8px;height:8px;border-radius:50%;flex:none}
.cav{background:var(--as);border-radius:6px;padding:9px 12px;font-size:.8rem;margin-top:10px}
.cav b{color:var(--amber)}
.strip{display:flex;gap:7px;flex-wrap:wrap}
.cr{border:1px solid var(--rule);border-radius:20px;padding:4px 12px;font-size:.79rem}
.cr.bad{border-color:var(--red);color:var(--red)}.cr.mid{border-color:var(--amber);color:var(--amber)}
.cr.ok{border-color:var(--gf);color:var(--green)}
.tlwrap{overflow-x:auto;padding:4px 0 2px}.tl{min-width:660px;position:relative}
.callouts{position:relative;height:92px}
.co{position:absolute;bottom:0;transform:translateX(-50%);font-size:.7rem;line-height:1.25;text-align:center;width:104px}
.co b{display:block;font-weight:600}.co.critical b{color:var(--red)}.co.partial b{color:var(--amber)}
.co i{display:block;width:1px;height:9px;background:var(--rule);margin:3px auto 0}
.co.hi i{height:51px}
.arcs{height:26px}
.tiles{display:flex;gap:3px}
.t{flex:1;height:26px;border-radius:3px;background:var(--gs);position:relative}
.t.partial{background:var(--amber)}.t.critical{background:var(--red)}
.t span{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-size:.58rem;font-family:"JetBrains Mono",monospace;color:var(--muted)}
.t.partial span,.t.critical span{color:#fff}
.secs{display:flex;gap:3px;margin-top:6px}
.sec{font-size:.63rem;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);font-family:"JetBrains Mono",monospace;border-top:2px solid var(--rule);padding-top:4px;text-align:center;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.legend{display:flex;gap:15px;font-size:.72rem;color:var(--muted);margin-top:11px;flex-wrap:wrap}
.legend i{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:5px;vertical-align:-1px}
.main{border-left:3px solid var(--red);background:var(--rs);border-radius:0 7px 7px 0;padding:14px 16px}
.q{background:var(--card);border-radius:5px;padding:8px 11px;margin-top:7px}
.q .sl{font-size:.62rem;letter-spacing:.11em;text-transform:uppercase;color:var(--muted);font-family:"JetBrains Mono",monospace;display:block;margin-bottom:3px}
.q p{font-style:italic;font-size:.86rem;color:var(--ink)}
.fix{display:flex;gap:11px;padding:11px 0;border-bottom:1px solid var(--rule)}
.fix:last-child{border-bottom:none}
.fix .n{font-family:"JetBrains Mono",monospace;font-size:.75rem;color:var(--red);font-weight:600;padding-top:2px;flex:none}
.fix .b{font-size:.89rem}.fix .b b{color:var(--ink)}
.fix .w{color:var(--muted);font-size:.83rem;margin-top:3px}
.sf{border:1px solid var(--rule);border-radius:8px;padding:16px 18px;margin-bottom:11px}
.prin{font-size:.68rem;letter-spacing:.1em;text-transform:uppercase;color:var(--green);font-family:"JetBrains Mono",monospace;font-weight:600;margin-bottom:6px}
.lbl{font-size:.66rem;letter-spacing:.11em;text-transform:uppercase;color:var(--muted);font-family:"JetBrains Mono",monospace;margin:13px 0 5px;font-weight:600}
.sf p{font-size:.89rem}
textarea{width:100%;border:1px solid var(--rule);border-radius:6px;padding:10px;font-family:inherit;font-size:.88rem;background:var(--sunk);color:var(--ink);resize:vertical;min-height:64px}
textarea:focus{outline:2px solid var(--gf);outline-offset:1px}
.btn{margin-top:9px;background:var(--gf);color:#fff;border:none;border-radius:6px;padding:8px 16px;font-family:inherit;font-size:.85rem;font-weight:600;cursor:pointer}
.btn[disabled]{background:var(--rule);color:var(--muted);cursor:not-allowed}
.hint{font-size:.78rem;color:var(--muted);margin-top:6px}
.reveal{margin-top:12px;background:var(--gs);border-radius:7px;padding:13px 15px;font-size:.88rem}
.reveal .lbl{margin-top:0;color:var(--green)}
.yours{background:var(--sunk);border-radius:7px;padding:11px 13px;font-size:.87rem;margin-top:10px;white-space:pre-wrap}
[hidden]{display:none!important}
.foot{text-align:center;color:var(--muted);font-size:.77rem;line-height:1.7;padding-top:4px}
</style>
<div class="wrap">
  <div class="card bar">
    <div class="brand">180DC <em>AI Quality Reviewer</em></div>
    <div class="meta" id="meta"></div>
    <div class="tabs" role="tablist">
      <button class="tab" id="tabLead" role="tab" aria-selected="true">Lead mode</button>
      <button class="tab" id="tabStu" role="tab" aria-selected="false">Student mode</button>
    </div>
  </div>
  <div id="lead"></div>
  <div id="stu" hidden></div>
  <p class="foot">Runs in your browser. Nothing leaves this machine unless you download it.<br>
    The reviewer advises, a named human decides. Nothing reaches a client on this review alone.</p>
</div>
<script>
var R=REVIEW, esc=function(s){return String(s).replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})};
var ctr=function(i){return ((i-0.5)/R.slides*100)};
var quo=function(qs){return qs.map(function(q){return '<div class="q"><span class="sl">Slide '+q.slide+'</span><p>&ldquo;'+esc(q.text)+'&rdquo;</p></div>'}).join('')};
document.getElementById('meta').innerHTML=esc(R.client)+' &mdash; '+esc(R.artifact)+'<br>'+R.slides+' slides';
document.title=R.client+' deliverable review';

var tiles='',i;
for(i=1;i<=R.slides;i++){var st=R.tiles[i]||'';tiles+='<div class="t '+st+'" title="Slide '+i+(st?' — '+st:'')+'"><span>'+i+'</span></div>';}
// A 70-slide deck at a fixed width gives 6px tiles. Scale the strip with the deck instead.
var STRIP=Math.max(660,R.slides*18);
// Callout boxes are ~104px. Any two closer than that on screen would overlap, so lift alternates.
var CO=(R.callouts||[]).slice().sort(function(p,q){return p.at-q.at}), lastX=-999;
CO.forEach(function(c){var x=ctr(c.at)/100*STRIP; c.hi=(x-lastX)<108; lastX=x;});
var arcs=(R.connectors||[]).map(function(c){var a=ctr(c.from)*10,b=ctr(c.to)*10;
  return '<path d="M '+a+' 24 C '+a+' 2, '+b+' 2, '+b+' 24" fill="none" stroke="var(--red)" stroke-width="1.5" stroke-dasharray="4 3"/>'}).join('');

document.getElementById('lead').innerHTML =
'<div class="card" style="margin-bottom:13px"><div class="pills">'+
 '<div class="pill"><span class="k">Your call</span><div class="v"><span class="dot" style="background:var(--muted)"></span>Not set</div></div>'+
 '<div class="pill"><span class="k">AI guess</span><div class="v">'+esc(R.aiLevel)+'</div></div>'+
 '<div class="pill"><span class="k">Effort</span><div class="v">'+esc(R.effort)+'</div></div>'+
 '<div class="pill"><span class="k">Confidence</span><div class="v"><span class="dot" style="background:var(--amber)"></span>'+esc(R.confidence)+'</div></div>'+
 '</div><div class="cav"><b>Do not pass the grade on.</b> The same deck has come back at two different levels on identical input. Work from the findings, which carry quotes you can check.</div></div>'+
'<div class="card" style="margin-bottom:13px"><h2>Where the deck is weakest</h2><div class="strip">'+
 R.criteria.map(function(c){return '<span class="cr '+c.state+'">'+esc(c.name)+' '+esc(c.score)+'</span>'}).join('')+'</div></div>'+
'<div class="card" style="margin-bottom:13px"><h2>Deck timeline</h2><div class="tlwrap"><div class="tl" style="min-width:'+STRIP+'px">'+
 '<div class="callouts">'+CO.map(function(c){ return '<div class="co '+c.state+(c.hi?' hi':'')+'" style="left:'+ctr(c.at)+'%"><b>'+esc(c.t)+'</b>'+esc(c.sub)+'<i></i></div>'}).join('')+'</div>'+
 '<svg class="arcs" viewBox="0 0 1000 26" preserveAspectRatio="none" aria-hidden="true">'+arcs+'</svg>'+
 '<div class="tiles">'+tiles+'</div>'+
 '<div class="secs">'+R.sections.map(function(s){return '<div class="sec" style="flex:'+s.span+'">'+esc(s.label)+'</div>'}).join('')+'</div>'+
 '</div></div><div class="legend"><span><i style="background:var(--gs);border:1px solid var(--rule)"></i>Pass</span>'+
 '<span><i style="background:var(--amber)"></i>Partial</span><span><i style="background:var(--red)"></i>Critical</span>'+
 (arcs?'<span><svg width="22" height="8"><path d="M1 7 C1 1, 21 1, 21 7" fill="none" stroke="var(--red)" stroke-width="1.5" stroke-dasharray="4 3"/></svg> Contradiction across slides</span>':'')+'</div></div>'+
'<div class="card" style="margin-bottom:13px"><h2>The main issue</h2><div class="main"><h3>'+esc(R.main.title)+'</h3>'+
 quo(R.main.quotes)+'<p style="font-size:.87rem;margin-top:11px">'+esc(R.main.why)+'</p></div></div>'+
'<div class="card"><h2>Fixes before this goes to the client</h2>'+
 R.fixes.map(function(f,n){return '<div class="fix"><span class="n">'+String(n+1).padStart(2,'0')+'</span><div><p class="b"><b>'+esc(f.do)+'</b></p><p class="w">'+esc(f.why)+'</p></div></div>'}).join('')+'</div>';

document.getElementById('stu').innerHTML =
'<div class="card" style="margin-bottom:13px"><p style="font-size:.9rem"><b style="color:var(--ink)">'+
 R.findings.length+' things to work on.</b> Each one quotes your own deck so you can check it. Answer the question before the suggested fix unlocks &mdash; the thinking is the point, not the fix.</p></div>'+
'<div class="card">'+R.findings.map(function(x,i){ return '<div class="sf"><div class="prin">'+esc(x.principle)+'</div><h3>Finding '+(i+1)+' of '+R.findings.length+'</h3>'+
 '<div class="lbl">What we see</div><p>'+esc(x.see)+'</p>'+quo(x.quotes)+
 '<div class="lbl">Why it matters to the client</div><p>'+esc(x.why)+'</p>'+
 '<div class="lbl">Answer this first</div><p>'+esc(x.reflect)+'</p>'+
 '<textarea id="a'+i+'" placeholder="Your answer. A sentence or two is enough."></textarea>'+
 '<button class="btn" id="b'+i+'" disabled>Show the suggested fix</button>'+
 '<p class="hint" id="h'+i+'">Write at least 15 characters to unlock.</p>'+
 '<div class="reveal" id="r'+i+'" hidden><div class="lbl">Your answer</div><div class="yours" id="y'+i+'"></div>'+
 '<div class="lbl">A suggested direction</div><p>'+esc(x.fix)+'</p></div></div>'}).join('')+'</div>';

R.findings.forEach(function(x,i){
  var a=document.getElementById('a'+i),b=document.getElementById('b'+i),
      h=document.getElementById('h'+i),r=document.getElementById('r'+i),y=document.getElementById('y'+i);
  a.addEventListener('input',function(){var ok=a.value.trim().length>=15;b.disabled=!ok;
    h.textContent=ok?'Unlocked. Your answer stays on screen next to the suggestion.':'Write at least 15 characters to unlock.';});
  b.addEventListener('click',function(){y.textContent=a.value.trim();r.hidden=false;b.disabled=true;
    h.textContent='Compare the two. Where they differ is the thing worth thinking about.';});
});
var L=document.getElementById('lead'),S=document.getElementById('stu'),
    tL=document.getElementById('tabLead'),tS=document.getElementById('tabStu');
function show(l){L.hidden=!l;S.hidden=l;tL.setAttribute('aria-selected',l);tS.setAttribute('aria-selected',!l);}
tL.addEventListener('click',function(){show(true)});tS.addEventListener('click',function(){show(false)});
</script>