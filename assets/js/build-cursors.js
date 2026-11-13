/* Independent of the rest of the UI: always boot the visible design cursors. */
(() => {
 const root=document.documentElement;
 const toggle=document.getElementById('builder-toggle');
 const targets=[...document.querySelectorAll('.hero-copy h1,.hero-copy h2,.hero-copy .intro,.hero-visual .portrait,.hero-visual .code-note,.section-heading,.story,.about-details>.panel,.education,.job,.work-card,.service,.process,.contact-section h2,.contact-section .email')];
 targets.forEach(el=>el.classList.add('build-target'));
 const colors=['#8057e4','#ed8759','#329d98'];
 const names=['Louis','Design','Content'];
 const agents=colors.map((color,i)=>({node:document.getElementById(`builder-cursor-${i}`),color,x:innerWidth*(.32+i*.18),y:180+i*130,target:null,slot:-1}));
 let enabled=true,frame=0,last=0,dirty=true,visible=[],epoch=performance.now(),generation=0;
 const built=new WeakSet();
 function refresh(){
  const items=targets.filter(el=>{const r=el.getBoundingClientRect();return !el.closest('[hidden]')&&r.width>0&&r.bottom>110&&r.top<innerHeight-90;});
  const previous=visible.map(el=>targets.indexOf(el)).join(',');
  visible=items;
  if(previous!==visible.map(el=>targets.indexOf(el)).join(',')){epoch=performance.now();generation++;}
  dirty=false;
 }
 function clear(agent){if(agent.target)agent.target.classList.remove('is-building');}
 function click(agent){
  const ring=document.createElement('i');ring.className='builder-click-ring';ring.style.setProperty('--ring-color',agent.color);ring.style.left=`${agent.x-12}px`;ring.style.top=`${agent.y-12}px`;ring.setAttribute('aria-hidden','true');document.body.append(ring);setTimeout(()=>ring.remove(),700);
 }
 function tick(now){
  frame=0;if(!enabled||document.hidden)return;
  if(dirty)refresh();
  const dt=Math.min(now-last||16,60);last=now;
  const beat=(now-epoch)/2600;
  const turn=Math.floor(beat),phase=beat-turn;
  const count=Math.min(innerWidth<721?1:3,visible.length);
  agents.forEach((agent,i)=>{
   const target=i<count&&visible.length?visible[(turn+i)%visible.length]:null;
   agent.node.style.visibility=target&&!document.querySelector('dialog[open]')?'visible':'hidden';
   if(!target){clear(agent);agent.target=null;return;}
   const slot=generation*100000+turn*3+i;
   if(target!==agent.target||slot!==agent.slot){clear(agent);agent.target=target;agent.slot=slot;agent.clicked=false;}
   const rect=target.getBoundingClientRect();
   // Fly in, trace the content from left to right, then select the lower edge.
   let tx,ty;
   if(phase<.32){tx=rect.left+Math.min(30,rect.width*.1);ty=rect.top+12;}
   else if(phase<.73){const progress=(phase-.32)/.41;tx=rect.left+rect.width*(.12+.68*progress);ty=rect.top+Math.min(35,rect.height*.3);}
   else{tx=rect.right-20;ty=rect.top+Math.min(rect.height-6,100);}
   tx=Math.max(12,Math.min(innerWidth-170,tx));ty=Math.max(95,Math.min(innerHeight-90,ty));
   const ease=1-Math.exp(-dt/110);agent.x+=(tx-agent.x)*ease;agent.y+=(ty-agent.y)*ease;
   agent.node.style.transform=`translate3d(${agent.x.toFixed(1)}px,${agent.y.toFixed(1)}px,0)`;
   const arrived=Math.hypot(tx-agent.x,ty-agent.y)<30;
   target.style.setProperty('--builder-color',agent.color);
   target.classList.toggle('is-building',phase>.15);
   agent.node.querySelector('.cursor-label').textContent=`${names[i]} · ${phase<.32?'Đang chọn':phase<.73?'Đang dựng nội dung':'Hoàn thiện ✓'}`;
   if(arrived&&!agent.clicked){agent.clicked=true;click(agent);if(!built.has(target)){built.add(target);target.classList.remove('build-enter');requestAnimationFrame(()=>target.classList.add('build-enter'));}}
  });
  frame=requestAnimationFrame(tick);
 }
 function start(){if(!frame&&enabled&&!document.hidden)frame=requestAnimationFrame(tick);}
 function update(){dirty=true;start();}
 addEventListener('scroll',update,{passive:true});addEventListener('resize',update,{passive:true});
 document.addEventListener('visibilitychange',()=>{if(document.hidden){cancelAnimationFrame(frame);frame=0;}else{dirty=true;last=0;start();}});
 document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',update));
 toggle.addEventListener('click',()=>{enabled=!enabled;root.dataset.buildMotion=enabled?'on':'off';toggle.setAttribute('aria-pressed',String(enabled));toggle.querySelector('span').textContent=enabled?'Con trỏ đang dựng nội dung':'Đã tạm dừng hiệu ứng';toggle.querySelector('b').textContent=enabled?'Tạm dừng Ⅱ':'Bật hiệu ứng ▶';if(enabled){epoch=performance.now();dirty=true;start();}else{cancelAnimationFrame(frame);frame=0;agents.forEach(clear);}});
 start();
})();
