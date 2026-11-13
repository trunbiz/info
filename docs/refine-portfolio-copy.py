from pathlib import Path
import json, re

root = Path(__file__).resolve().parents[1]
page = root / 'index.html'
html = page.read_text(encoding='utf-8')
replacements = {
 'Louis Tran, Backend Developer tại Hà Nội. Laravel, n8n, AI Automation và Google Ad Manager. Cùng xây dựng hệ thống giải quyết bài toán thực tế.': 'Louis Tran — Backend Developer, ứng dụng và huấn luyện AI cho sản phẩm thực tế. Phát triển Laravel APIs, tự động hóa n8n và các giải pháp AdTech.',
 'BACKEND DEVELOPER · AI AUTOMATION': 'BACKEND DEVELOPER · AI & AUTOMATION',
 'Tôi biến những bài toán phức tạp thành hệ thống dễ sử dụng. Xây dựng backend vững chắc, kết nối dữ liệu và tự động hóa công việc để đội ngũ tập trung vào điều quan trọng hơn.': 'Tôi là lập trình viên Backend, đồng thời phát triển các sản phẩm ứng dụng AI. Tôi kết hợp kinh nghiệm xây dựng hệ thống với khả năng sử dụng, huấn luyện AI và tự động hóa để giải quyết những công việc cụ thể trong kinh doanh và vận hành.',
 'Tôi quan tâm đến điều xảy ra sau khi code được đưa lên production: hệ thống có ổn định, dễ vận hành và giải quyết đúng vấn đề hay không.': 'Từ hệ thống thanh toán, logistics đến các sản phẩm của riêng mình, tôi luôn bắt đầu bằng một câu hỏi: người dùng đang cần giải quyết việc gì?',
 'Xây dựng để công việc<br>trở nên đơn giản hơn.': 'Làm kỹ phần hệ thống.<br>Hiểu rõ việc cần giải quyết.',
 'Laravel, PHP và MySQL là nền tảng chính của tôi. Bên cạnh phát triển API và ứng dụng web, tôi xây dựng workflow với n8n, kết nối AI và các dịch vụ qua API/webhook để giảm thao tác lặp lại.': 'Laravel, PHP và MySQL là nền tảng kỹ thuật chính của tôi. Tôi cũng sử dụng và huấn luyện AI theo yêu cầu của dự án, xây dựng quy trình tự động hóa với n8n và kết nối các dịch vụ qua API. Với các sản phẩm cá nhân, tôi trực tiếp đưa ý tưởng thành tính năng, theo dõi cách chúng hoạt động và tiếp tục cải tiến.',
 'Tự động hóa có mục đích': 'Ứng dụng & huấn luyện AI',
 'Kết nối n8n, AI, Google Sheets và Telegram thành luồng công việc có thể theo dõi và bảo trì.': 'Đưa AI vào bài toán cụ thể: hiểu nhu cầu khách hàng, hỗ trợ nội dung và xử lý công việc lặp lại. Kết nối kết quả với hệ thống để sử dụng trong thực tế.',
 'Các sản phẩm AI cá nhân tôi đang xây dựng, cùng những hệ thống tôi đã tham gia phát triển. Bốn dự án cá nhân sử dụng ảnh chụp giao diện website thực tế.': 'Tôi tự phát triển sản phẩm để đưa những ý tưởng về AI và tự động hóa vào thực tế. Mỗi dự án bắt đầu từ một nhu cầu cụ thể: tìm khách hàng, hỗ trợ mua sắm, chia sẻ công cụ hay xây dựng một nền tảng nội dung.',
 'AI nhận diện nhu cầu từ bài viết và bình luận Facebook Group, xếp hạng lead phù hợp và giữ lại ngữ cảnh để hỗ trợ bước tiếp cận tiếp theo.': 'Tôi xây dựng Max Morus để giúp người làm kinh doanh tìm thấy nhu cầu đang được chia sẻ trong Facebook Group. AI hỗ trợ đọc ngữ cảnh, phân loại và ưu tiên lead để việc tìm khách có cơ sở hơn.',
 'Nền tảng mua sắm hoàn tiền và affiliate, kết hợp công cụ gợi ý sản phẩm bằng AI và tự động hóa để hỗ trợ người mua lẫn người làm nội dung.': 'Với Muarehon, tôi phát triển nền tảng mua sắm hoàn tiền và affiliate, từ ghi nhận đơn đến theo dõi trạng thái hoàn tiền. Các công cụ AI hỗ trợ gợi ý sản phẩm và giảm thao tác thủ công cho người làm affiliate.',
 'Nền tảng giới thiệu công cụ, phần mềm và kiến thức AI thực hành cho người Việt, với thư viện bài viết, prompt mẫu và các giải pháp hỗ trợ công việc.': 'Tôi xây dựng AI Tool Hub 101 để chia sẻ công cụ, phần mềm và cách ứng dụng AI vào công việc. Nội dung tập trung vào hướng dẫn thực hành, prompt mẫu và những giải pháp người dùng có thể áp dụng.',
 'Dự án nội dung cá nhân trong hệ sinh thái AI của tôi, với các chủ đề công nghệ, giải trí và những câu chuyện đang được quan tâm.': 'Holoviral là dự án tôi phát triển trong lĩnh vực nội dung số, với các chủ đề công nghệ, giải trí và đời sống. Tôi tập trung vào cách tổ chức thông tin và trải nghiệm đọc, tìm kiếm, khám phá nội dung.',
 'Kết nối công cụ, xử lý dữ liệu và giảm công việc lặp lại với n8n, API và AI.': 'Thiết kế quy trình kết hợp AI, n8n và API để xử lý dữ liệu, chuyển kết quả giữa các công cụ và giảm thao tác lặp lại.',
 'Cùng xây dựng<br><em>điều có ích.</em>': 'Tôi có thể giúp gì<br><em>cho dự án của bạn?</em>',
 'Từ một tích hợp nhỏ đến hệ thống nhiều thành phần, bắt đầu bằng việc hiểu đúng vấn đề.': 'Tôi nhận phát triển backend, triển khai AI theo yêu cầu và tự động hóa quy trình. Phạm vi công việc được thống nhất từ bài toán, dữ liệu và cách đội ngũ sẽ sử dụng hệ thống.',
 '<h3>AI & n8n Automation</h3><p>Biến quy trình thủ công thành workflow rõ ràng, kết nối ứng dụng đang dùng với AI và dữ liệu doanh nghiệp.</p><ul><li>n8n, API & webhooks</li><li>Tích hợp OpenAI, Gemini, Claude</li><li>Google Sheets & Telegram</li></ul>': '<h3>Ứng dụng AI & Automation</h3><p>Ứng dụng và huấn luyện AI phục vụ yêu cầu của dự án, kết nối với dữ liệu và công cụ đội ngũ đang sử dụng.</p><ul><li>Thiết kế prompt & hướng dẫn AI</li><li>Huấn luyện AI theo tác vụ của dự án</li><li>Tích hợp AI, n8n, API & webhooks</li></ul>',
 'Kể tôi nghe về sản phẩm, quy trình đang mất thời gian<br>hoặc vấn đề kỹ thuật bạn muốn giải quyết.': 'Bạn cần xây dựng sản phẩm, ứng dụng AI vào công việc<br>hay xử lý một vấn đề backend? Hãy trao đổi với tôi.',
 'portfolio.css?v=6': 'portfolio.css?v=7',
 'portfolio.js?v=6': 'portfolio.js?v=7',
}
for old, new in replacements.items():
 if old not in html:
  raise ValueError('Missing expected copy: ' + old)
 html = html.replace(old, new)

ai_section = '''<div class="ai-practice" aria-labelledby="ai-practice-title"><div class="ai-practice-heading"><p class="eyebrow">AI TRONG CÔNG VIỆC CỦA TÔI</p><h3 id="ai-practice-title">Từ sử dụng AI đến xây dựng sản phẩm với AI.</h3><p>Tôi dùng AI trong quá trình phát triển phần mềm và đưa AI vào tính năng sản phẩm. Với mỗi bài toán, tôi xác định nhiệm vụ, chuẩn bị ngữ cảnh và huấn luyện AI theo yêu cầu trước khi kết nối vào quy trình sử dụng.</p></div><div class="ai-practice-grid"><article class="panel"><span class="eyebrow">01 / ỨNG DỤNG</span><h3>Chọn đúng việc cho AI</h3><p>Phân tích bài toán để xác định phần AI có thể hỗ trợ: đọc hiểu nội dung, phân loại nhu cầu, gợi ý sản phẩm hoặc hỗ trợ soạn thảo.</p></article><article class="panel"><span class="eyebrow">02 / HUẤN LUYỆN</span><h3>Hướng dẫn AI theo yêu cầu</h3><p>Chuẩn bị ngữ cảnh, hướng dẫn và ví dụ phù hợp với tác vụ; kiểm tra đầu ra và điều chỉnh để AI đáp ứng mục tiêu của dự án.</p></article><article class="panel"><span class="eyebrow">03 / TRIỂN KHAI</span><h3>Đưa vào luồng công việc</h3><p>Kết nối AI với backend, API và n8n để kết quả được sử dụng trong sản phẩm. Theo dõi và cải tiến trong quá trình vận hành.</p></article></div></div>'''
anchor = '</section>\n<section class="section container" id="experience">'
assert anchor in html
html = html.replace(anchor, ai_section + anchor, 1)
page.write_text(html, encoding='utf-8')

js_path = root/'assets/js/portfolio.js'
js = js_path.read_text(encoding='utf-8')
for key in ['maxmorus', 'muarehon', 'aitoolhub101', 'holoviral']:
 pattern = r'"'+key+r'":(\{[^\n]+\}),'
 match = re.search(pattern, js)
 assert match, key
 value = json.loads(match.group(1))
 value['description'] = replacements[value['description']]
 js = re.sub(pattern, lambda m: json.dumps(key)+':'+json.dumps(value,ensure_ascii=False)+',', js)
old = "automation:{title:'AI & Workflow Automation',description:'Xây dựng workflow phù hợp với quy trình thực tế, từ nhận dữ liệu qua webhook đến xử lý và chuyển kết quả sang các công cụ khác.',items:['Thiết kế workflow n8n và kết nối REST APIs.','Tích hợp OpenAI, Gemini hoặc Claude tùy nhu cầu.','Đồng bộ dữ liệu với Google Sheets và thông báo Telegram.','Làm rõ đầu vào, đầu ra và cách xử lý lỗi để dễ vận hành.']}"
new = "automation:{title:'AI & Workflow Automation',description:'Tôi kết hợp khả năng sử dụng, huấn luyện AI và phát triển backend để đưa AI vào quy trình công việc cụ thể.',items:['Xác định tác vụ và chuẩn bị ngữ cảnh, hướng dẫn cho AI.','Huấn luyện AI theo yêu cầu, kiểm tra đầu ra và điều chỉnh.','Kết nối AI với backend, REST APIs và workflow n8n.','Đưa kết quả vào các công cụ làm việc như Google Sheets hoặc Telegram.']}"
assert old in js
js = js.replace(old,new)
js_path.write_text(js,encoding='utf-8')
print('Updated hero, about, AI capabilities, projects, services and modal copy.')
