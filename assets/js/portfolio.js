const menu = document.querySelector('.menu');
const nav = document.querySelector('#navigation');
function closeMenu(){menu.setAttribute('aria-expanded','false');nav.classList.remove('open');menu.textContent='☰';}
menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open);menu.textContent=open?'×':'☰';});
nav.querySelectorAll('a').forEach(a=>a.addEventListener('click',closeMenu));
addEventListener('keydown',e=>{if(e.key==='Escape')closeMenu();});
document.querySelector('#year').textContent=new Date().getFullYear();
addEventListener('scroll',()=>{const d=document.documentElement.scrollHeight-innerHeight;document.querySelector('.progress').style.width=(d>0?scrollY/d*100:0)+'%';},{passive:true});
if('IntersectionObserver' in window){const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting)nav.querySelectorAll('a').forEach(a=>a.classList.toggle('current',a.hash==='#'+e.target.id));}),{rootMargin:'-15% 0px -65% 0px'});document.querySelectorAll('main section[id]').forEach(el=>observer.observe(el));}
document.querySelectorAll('[data-filter]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('[data-filter]').forEach(b=>{b.classList.toggle('active',b===button);b.setAttribute('aria-pressed',String(b===button));});document.querySelectorAll('[data-category]').forEach(card=>{card.hidden=button.dataset.filter!=='all'&&card.dataset.category!==button.dataset.filter;});}));
const projects={
 adtech:{title:'Publisher Monetization',description:'Giải pháp kỹ thuật cho hoạt động quảng cáo và báo cáo publisher, dựa trên kinh nghiệm làm việc với Google Ad Manager.',items:['Cấu hình ad units, line items, targeting và kiểm tra ad tags.','Phân tích vấn đề phân phối quảng cáo và phối hợp xử lý với đối tác.','Báo cáo requests, impressions, RPM/eCPM và viewability.','Theo dõi dữ liệu để hỗ trợ tối ưu hoạt động vận hành.']},
 automation:{title:'AI & Workflow Automation',description:'Xây dựng workflow phù hợp với quy trình thực tế, từ nhận dữ liệu qua webhook đến xử lý và chuyển kết quả sang các công cụ khác.',items:['Thiết kế workflow n8n và kết nối REST APIs.','Tích hợp OpenAI, Gemini hoặc Claude tùy nhu cầu.','Đồng bộ dữ liệu với Google Sheets và thông báo Telegram.','Làm rõ đầu vào, đầu ra và cách xử lý lỗi để dễ vận hành.']},
 backend:{title:'Payment & Partner APIs',description:'Kinh nghiệm phát triển backend trong lĩnh vực ví điện tử tại 9Pay, tập trung vào API và kết nối dịch vụ.',items:['Phát triển RESTful APIs phục vụ hệ thống ví điện tử.','Tích hợp các kênh thanh toán và dịch vụ đối tác.','Phát triển module CRM/CMS cho đội ngũ nội bộ.','Phân tích yêu cầu từ hệ thống vận hành.']},
 operations:{title:'ERP & Internal Systems',description:'Kinh nghiệm phát triển công cụ vận hành nội bộ trong lĩnh vực logistics tại Giao Hàng Tiết Kiệm.',items:['Phát triển chức năng chấm công và theo dõi KPI.','Xây dựng RESTful APIs hỗ trợ các module nội bộ.','Chuyển yêu cầu vận hành thành chức năng nghiệp vụ.','Tổ chức dữ liệu để hỗ trợ quản lý và theo dõi công việc.']}
};
const dialog=document.querySelector('#project-dialog');
document.querySelectorAll('[data-project]').forEach(button=>button.addEventListener('click',()=>{const p=projects[button.dataset.project];document.querySelector('#dialog-title').textContent=p.title;document.querySelector('#dialog-description').textContent=p.description;document.querySelector('#dialog-list').replaceChildren(...p.items.map(text=>{const li=document.createElement('li');li.textContent=text;return li;}));dialog.showModal();}));
document.querySelector('.dialog-close').addEventListener('click',()=>dialog.close());
document.querySelector('#dialog-contact').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();}});
document.querySelector('#copy-email').addEventListener('click',async()=>{const status=document.querySelector('#copy-status');try{await navigator.clipboard.writeText('trunbiz.dev@gmail.com');status.textContent='Đã sao chép email. Hẹn gặp bạn trong hộp thư!';}catch{status.textContent='Bạn có thể sao chép địa chỉ: trunbiz.dev@gmail.com';}});


