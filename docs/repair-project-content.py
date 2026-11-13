from pathlib import Path
import re, json

root = Path(__file__).resolve().parents[1]
projects = [
 ('maxmorus', 'Max Morus', 'maxmorus.com', 'AI LEAD DISCOVERY', 'AI nhận diện nhu cầu từ bài viết và bình luận Facebook Group, xếp hạng lead phù hợp và giữ lại ngữ cảnh để hỗ trợ bước tiếp cận tiếp theo.', ['AI Lead Discovery','Facebook Groups','Automation'], ['Phân tích nhu cầu từ bài viết và bình luận Facebook Group.', 'Xếp hạng lead theo tiêu chí và giữ ngữ cảnh gốc.', 'Hỗ trợ tổ chức tác vụ tiếp cận và xuất dữ liệu.']),
 ('muarehon', 'Muarehon', 'muarehon.com', 'CASHBACK & AI TOOLS', 'Nền tảng mua sắm hoàn tiền và affiliate, kết hợp công cụ gợi ý sản phẩm bằng AI và tự động hóa để hỗ trợ người mua lẫn người làm nội dung.', ['Cashback','Affiliate','AI Tools'], ['Kiểm tra hoàn tiền từ liên kết sản phẩm.', 'Theo dõi đơn hàng và trạng thái hoàn tiền.', 'Công cụ hỗ trợ affiliate và gợi ý sản phẩm bằng AI.']),
 ('aitoolhub101', 'AI Tool Hub 101', 'aitoolhub101.com', 'AI TOOLS & KNOWLEDGE', 'Nền tảng giới thiệu công cụ, phần mềm và kiến thức AI thực hành cho người Việt, với thư viện bài viết, prompt mẫu và các giải pháp hỗ trợ công việc.', ['AI Tools','Prompt Library','Automation'], ['Khám phá tool và phần mềm theo nhu cầu công việc.', 'Thư viện bài viết AI thực hành và prompt mẫu.', 'Giới thiệu các công cụ như Auto Comment và ZaloMind.']),
 ('holoviral', 'Holoviral', 'holoviral.com', 'CONTENT & DIGITAL MEDIA', 'Dự án nội dung cá nhân trong hệ sinh thái AI của tôi, với các chủ đề công nghệ, giải trí và những câu chuyện đang được quan tâm.', ['Digital Media','Content','Technology'], ['Khám phá nội dung công nghệ và giải trí.', 'Theo dõi các câu chuyện đang được quan tâm.', 'Tìm kiếm và đọc nội dung theo chủ đề.']),
]
html = (root/'index.html').read_text(encoding='utf-8-sig')
cards = []
for key,name,domain,category,description,tags,items in projects:
 cards.append(f'''<article class="work-card personal-project" data-category="personal"><a class="project-screenshot" href="https://{domain}/" target="_blank" rel="noopener noreferrer" aria-label="Xem website {name}"><span class="screenshot-bar"><i></i><i></i><i></i><span>{domain}</span><b>↗</b></span><img src="assets/img/projects/{key}.webp" width="1260" height="630" loading="lazy" decoding="async" alt="Ảnh chụp giao diện website {name}"></a><div class="work-body"><div class="work-top">{category}<button data-project="{key}" aria-label="Chi tiết {name}">↗</button></div><h3>{name}</h3><p>{description}</p><div class="tags">{''.join('<span>'+t+'</span>' for t in tags)}</div><div class="project-actions"><a href="https://{domain}/" target="_blank" rel="noopener noreferrer">Truy cập website ↗</a><button data-project="{key}">Về dự án →</button></div></div></article>''')
html = re.sub(r'<article class="work-card personal-project".*?</article>', lambda m: cards.pop(0), html, flags=re.S)
html = html.replace('AI c? nh?n', 'AI cá nhân').replace('Truy c?p website ?', 'Truy cập website ↗')
html = html.replace('Louis ? ?ang thi?t k?', 'Louis · Đang thiết kế').replace('Design ? ?ang s?p x?p','Design · Đang sắp xếp').replace('Content ? ?ang vi?t','Content · Đang viết').replace('Con tr? ?ang d?ng n?i dung','Con trỏ đang dựng nội dung').replace('T?m d?ng ?', 'Tạm dừng Ⅱ')
html = html.replace('Hình trên thẻ là minh họa ý tưởng sản phẩm.', 'Bốn dự án cá nhân sử dụng ảnh chụp giao diện website thực tế.')
html = html.replace('Hệ thống & giải pháp<span>.</span>', 'Sản phẩm & dự án<span>.</span>')
html = html.replace('Những nhóm bài toán tôi đã tham gia phát triển và vận hành. Hình bên dưới là sơ đồ minh họa giải pháp.', 'Các sản phẩm AI cá nhân tôi đang xây dựng, cùng những hệ thống tôi đã tham gia phát triển. Bốn dự án cá nhân sử dụng ảnh chụp giao diện website thực tế.')
html = html.replace('Tất cả <small>04</small>', 'Tất cả <small>08</small>')
html = re.sub(r'<link rel="preconnect" href="https://fonts.googleapis.com">', '', html)
html = re.sub(r'<link href="https://fonts.googleapis.com/[^\"]+" rel="stylesheet">', '', html)
html = html.replace('portfolio.css?v=5','portfolio.css?v=6').replace('portfolio.js?v=5','portfolio.js?v=6')
(root/'index.html').write_text(html,encoding='utf-8')
js = (root/'assets/js/portfolio.js').read_text(encoding='utf-8-sig')
for key,name,domain,category,description,tags,items in projects:
 value = {'title':name,'description':description,'url':'https://'+domain+'/', 'items':items}
 js = re.sub(r'"'+key+r'":\{[^\n]+\},', lambda m: json.dumps(key)+':'+json.dumps(value,ensure_ascii=False)+',', js)
(root/'assets/js/portfolio.js').write_text(js,encoding='utf-8')
print('Restored Vietnamese content and project images.')
