const ids=[];
const C={bg:'#F3F3E9',ink:'#16332F',muted:'#60716A',line:'#D4DDD2',card:'#FFFFFF',green:'#007D69',orange:'#BD532F',blue:'#6577BE',pale:'#E2EBDE'};
const rgb=h=>({r:parseInt(h.slice(1,3),16)/255,g:parseInt(h.slice(3,5),16)/255,b:parseInt(h.slice(5,7),16)/255});
const paint=h=>[{type:'SOLID',color:rgb(h)}];
const fonts=[{family:'IBM Plex Sans',style:'Regular'},{family:'IBM Plex Sans',style:'SemiBold'},{family:'IBM Plex Mono',style:'Regular'}];
await Promise.all(fonts.map(f=>figma.loadFontAsync(f)));
function keep(n){ids.push(n.id);return n;}
function stack(parent,name,w,gap=16,pad=0,bg=null,dir='VERTICAL'){
 const n=keep(figma.createAutoLayout(dir));n.name=name;if(parent)parent.appendChild(n);
 n.resize(w,10);n.primaryAxisSizingMode=dir==='HORIZONTAL'?'FIXED':'AUTO';n.counterAxisSizingMode=dir==='HORIZONTAL'?'AUTO':'FIXED';
 n.paddingTop=pad;n.paddingBottom=pad;n.paddingLeft=pad;n.paddingRight=pad;n.itemSpacing=gap;
 n.fills=bg?paint(bg):[];n.clipsContent=false;return n;
}
function text(parent,str,size=20,w=1264,color=C.ink,bold=false,mono=false){
 const n=keep(figma.createText());parent.appendChild(n);n.fontName=mono?fonts[2]:bold?fonts[1]:fonts[0];
 n.fontSize=size;n.characters=str;n.fills=paint(color);n.lineHeight={unit:'PERCENT',value:135};
 n.resize(w,10);n.textAutoResize='HEIGHT';n.name=str.slice(0,70);return n;
}
function rule(parent,w=1312){const n=keep(figma.createRectangle());parent.appendChild(n);n.resize(w,1);n.fills=paint(C.line);return n;}
function tag(parent,str){return text(parent,str,15,1264,C.green,false,true);}
function link(parent,label,url,w=1264){const n=text(parent,label,15,w,C.green);n.setRangeHyperlink(0,label.length,{type:'URL',value:url});return n;}
function row(parent,name,cols,widths,header=false){
 const n=stack(parent,name,1312,20,header?14:14,header?C.pale:null,'HORIZONTAL');
 for(let i=0;i<cols.length;i++)text(n,cols[i],header?16:18,widths[i],header?C.muted:C.ink,header);return n;
}
let right=0;for(const n of figma.currentPage.children)right=Math.max(right,n.x+n.width);
function board(name,index){const n=stack(null,name,1440,24,64,C.bg);n.x=right+100+index*1540;n.y=100;return n;}
const a=board('01 — Research specification',0);
tag(a,'ENERGY FUTURES  /  RESEARCH 01  /  24 OCT 2026');
text(a,'How much power\nwill the world need?',68,1280,C.ink,true);
text(a,'First define the demand. Then compare what can supply it.',27,1264,C.muted);
const metrics=stack(a,'Verified starting anchors',1312,24,0,null,'HORIZONTAL');
for(const [v,l] of [['28,600 TWh','2025 electricity consumption'],['3.6% / 3.8%','2026 / 2027 forecast growth'],['1.3%','2025 total energy growth']]){
 const c=stack(metrics,l,421,8,24,C.card);text(c,v,39,373,C.green,true);text(c,l,17,373,C.muted);
}
text(a,'Electricity and total energy are different ledgers. The starting figures above do not share a common denominator.',18,1264,C.muted);
rule(a);
tag(a,'SIX QUESTIONS THAT MAKE Q1 ANSWERABLE');
row(a,'Research table header',['QUESTION','CONCRETE COMPARISON','OUTPUT WE NEED'],[282,460,490],true);
const questions=[
 ['01  What are we counting?','Primary → final → useful energy; electricity consumption versus generation.','Separate EJ and TWh baselines; reconcile boundaries, losses and source vintages.'],
 ['02  Where is growth?','China, India, US, EU27, Southeast Asia, rest of world. Compare % AND added TWh.','Regional baseline + growth waterfall + electricity per person.'],
 ['03  What uses it?','Industry, buildings and transport. Data centers sit inside a declared sector.','Non-overlapping sector totals and incremental demand in TWh/year.'],
 ['04  What changes demand?','Service activity × intensity × technology adoption; fuel displacement alongside electricity.','A model that separates growth, efficiency and electrification.'],
 ['05  When is it needed?','Same annual TWh; different hourly peaks, seasons and flexible loads.','Regional hourly profiles, peak GW and load-duration curves.'],
 ['06  What must be built?','Demand growth + losses versus output from plants that remain in service.','Required new annual generation; then capacity and build pace.']
];
for(const q of questions){row(a,q[0],q,[282,460,490]);rule(a);}
const call=stack(a,'Research completion criterion',1312,10,24,C.pale);
text(call,'The target: a demand specification for every technology.',27,1264,C.ink,true);
text(call,'For each region and scenario: annual electricity, remaining fuel/heat demand, hourly load, peak power and flexibility. Technology costs and the winning mix come in questions 2 and 3.',20,1264);
link(a,'IEA · Electricity Mid-Year Update 2026 · published 23 July 2026','https://www.iea.org/reports/electricity-mid-year-update-2026/executive-summary');
link(a,'IEA · Global Energy Review 2026 · total energy growth','https://www.iea.org/reports/global-energy-review-2026/key-findings');

const b=board('02 — Demand growth sensitivity',1);
tag(b,'FIRST MODEL  /  SCALE TEST  /  NOT A CALIBRATED FORECAST');
text(b,'Small growth gaps.\nVery different worlds.',60,1280,C.ink,true);
text(b,'Same 2025 anchor: 28,600 TWh. Three assumed annual growth rates through 2050.',23,1264,C.muted);
const formula=stack(b,'Model equation',1312,8,20,C.pale);text(formula,'D(year) = 28,600 × (1 + g)^(year − 2025)',25,1272,C.ink,false,true);
const plot=keep(figma.createFrame());b.appendChild(plot);plot.name='Editable demand sensitivity chart';plot.resize(1312,500);plot.fills=[];plot.clipsContent=false;
function ptext(parent,str,x,y,w=160,size=17,color=C.muted,bold=false){const n=text(parent,str,size,w,color,bold);n.x=x;n.y=y;return n;}
function rect(parent,x,y,w,h,col){const n=keep(figma.createRectangle());parent.appendChild(n);n.resize(w,h);n.x=x;n.y=y;n.fills=paint(col);return n;}
function path(parent,points,col,weight=4){
 const minX=Math.min(...points.map(p=>p[0])),minY=Math.min(...points.map(p=>p[1]));
 const n=keep(figma.createVector());parent.appendChild(n);n.vectorPaths=[{windingRule:'NONE',data:points.map((p,i)=>(i?'L ':'M ')+(p[0]-minX).toFixed(3)+' '+(p[1]-minY).toFixed(3)).join(' ')}];
 n.x=minX;n.y=minY;n.strokes=paint(col);n.strokeWeight=weight;n.fills=[];return n;
}
const x=y=>85+(y-2025)/25*1020;const y=v=>420-v/80000*360;
ptext(plot,'Annual electricity consumption · thousand TWh',85,0,900,17);
for(let v=0;v<=80000;v+=20000){rect(plot,85,y(v),1020,1,C.line);ptext(plot,String(v/1000),25,y(v)-13,50,17);}
for(const yr of [2025,2030,2040,2050])ptext(plot,String(yr),x(yr)-28,438,75,17);
for(const [g,col] of [[.02,C.blue],[.03,C.green],[.04,C.orange]]){
 const points=Array.from({length:26},(_,i)=>[x(2025+i),y(28600*(1+g)**i)]);path(plot,points,col,4);
 const val=28600*(1+g)**25;ptext(plot,`${(g*100).toFixed(0)}% → ${(val/1000).toFixed(1)}k`,1120,y(val)-14,185,21,col,true);
}
const point=keep(figma.createEllipse());plot.appendChild(point);point.resize(12,12);point.x=x(2025)-6;point.y=y(28600)-6;point.fills=paint(C.ink);
ptext(plot,'2025 reported anchor',110,300,290,16,C.ink);
text(b,'These curves are analyst-selected sensitivities. They are not IEA forecasts, probabilities or a confidence interval.',18,1264,C.orange);
row(b,'Milestone header',['ASSUMED GROWTH','2030 · TWh/yr','2040 · TWh/yr','2050 · TWh/yr'],[332,290,290,300],true);
for(const g of [.02,.03,.04])row(b,'Growth '+g,[(g*100).toFixed(0)+'% per year',...[2030,2040,2050].map(yr=>Math.round(28600*(1+g)**(yr-2025)).toLocaleString('en-US'))],[332,290,290,300]);
const takeaway=stack(b,'Sensitivity implication',1312,12,24,C.pale);
text(takeaway,'4% versus 2% adds ~29,300 TWh/year in 2050.',32,1264,C.ink,true);
text(takeaway,'That difference is slightly larger than all reported world electricity consumption in 2025. The research must explain the growth rate through sector and regional drivers.',21,1264);
const bench=stack(b,'Published forecast benchmark',1312,8,24,C.card);
text(bench,'Independent near-term benchmark: ~30,700 TWh in 2027.',25,1264,C.ink,true);
text(bench,'IEA July 2026 forecast. Kept separate from the curves. The February edition used 28,200 TWh for 2025; this canvas uses July’s revised 28,600 TWh baseline.',18,1264,C.muted);
link(b,'Source for baseline + 2027 benchmark · IEA July 2026','https://www.iea.org/reports/electricity-mid-year-update-2026/executive-summary');
text(b,'Next: calibrate activity, efficiency and electrification by sector; reconcile published long-term scenarios before comparing them.',18,1264,C.muted);

const c=board('03 — Concrete comparison units',2);
tag(c,'COMPARE LIKE WITH LIKE  /  ALL EXAMPLES BELOW USE ASSUMED INPUTS');
text(c,'Put every claim\nin the same units.',60,1280,C.ink,true);
text(c,'TWh per year measures energy. GW measures power. Timing changes the system we need.',23,1264,C.muted);
tag(c,'01 / HOW MUCH ANNUAL ELECTRICITY DOES A NEW USE ADD?');
const loadplot=keep(figma.createFrame());c.appendChild(loadplot);loadplot.name='Editable annual demand comparison';loadplot.resize(1312,280);loadplot.fills=[];
const loads=[['10 million EVs',21.6,'12,000 km/year × 0.18 kWh/km at charger'],['100 million households',200,'Each adds 2,000 kWh/year'],['100 GW of data-center load',744.6,'Facility-level power × 85% load factor']];
for(let i=0;i<loads.length;i++){
 const [label,val,note]=loads[i],top=i*88;
 ptext(loadplot,label,0,top,385,20,C.ink,true);ptext(loadplot,note,0,top+31,405,16,C.muted);
 rect(loadplot,430,top+7,val/800*700,30,[C.blue,C.green,C.orange][i]);ptext(loadplot,val.toFixed(1)+' TWh',440+val/800*700,top+6,170,20,C.ink,true);
}
text(c,'Scale illustrations, not forecasts. Do not add overlapping loads. Data-center facility power already includes cooling and other overhead.',18,1264,C.muted);
rule(c);
tag(c,'02 / SAME SERVICE: 100 TWh OF USEFUL HEAT');
const heat=stack(c,'Heat comparison',1312,24,0,null,'HORIZONTAL');
for(const [h,v,n] of [['Gas boiler','111.1 TWh of gas','Assumed efficiency: 90%'],['Heat pump','33.3 TWh of electricity','Assumed seasonal COP: 3']]){
 const hc=stack(heat,h,644,8,24,C.card);text(hc,h,22,596,C.muted);text(hc,v,34,596,C.green,true);text(hc,n,18,596,C.muted);
}
text(c,'Switching this service adds 33.3 TWh of electricity and removes 111.1 TWh of gas. Final purchased energy falls. Primary energy and emissions require a separate supply calculation.',20,1264);
rule(c);
tag(c,'03 / SAME OUTPUT: 1,000 TWh OF GENERATION PER YEAR');
row(c,'Capacity header',['ASSUMED CAPACITY FACTOR','INSTALLED CAPACITY','WHAT THIS DOES NOT TELL US'],[430,310,492],true);
for(const cf of [.2,.4,.9])row(c,'Capacity '+cf,[(cf*100).toFixed(0)+'%',Math.round(1000/(8.76*cf))+' GW',cf===.2?'Hourly availability and reliability':cf===.4?'Storage, networks or delivered cost':'First-year output before a full year of operation'],[430,310,492]);
text(c,'Capacity = annual TWh ÷ (8.76 × capacity factor). Generic annual energy equivalents; capacity factor is not dependable capacity.',18,1264,C.muted);
rule(c);
tag(c,'04 / SAME ANNUAL DEMAND: 100 TWh, DIFFERENT PEAKS');
text(c,'80% load factor → 14.3 GW peak       40% load factor → 28.5 GW peak',29,1264,C.ink,true);
text(c,'Peak GW = annual TWh ÷ (8.76 × load factor). This is why the next model needs regional hourly profiles.',19,1264,C.muted);
const next=stack(c,'Next research step',1312,12,24,C.pale);
text(next,'Next build: the sector × region demand ledger.',29,1264,C.ink,true);
text(next,'Historical baseline → activity assumptions → efficiency + adoption → annual demand → hourly shape → generation requirement. Back-test before treating the model as a forecast.',21,1264);
text(c,'Status: research design + scaling prototype. A full historical dataset, calibrated forecast and supply adequacy model remain to be built.',17,1264,C.muted);
figma.viewport.scrollAndZoomIntoView([a]);
return {createdNodeIds:ids,boards:[a,b,c].map(n=>({id:n.id,name:n.name,x:n.x,y:n.y,width:n.width,height:n.height})),nodeCount:ids.length};
