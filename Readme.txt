========================================
Louis Tran - Personal Portfolio Website
========================================

1) Giới thiệu
-------------
Đây là website portfolio/CV online của Louis Tran (Full-Stack + AdTech/GAM).
Website được xây dựng dựa trên template iPortfolio (BootstrapMade) và tùy biến lại nội dung
phù hợp với định hướng: Laravel/PHP, MySQL, Vue/TypeScript, Google Ad Manager & AdTech,
Analytics/Reporting (GA4), DevOps/Ops.

2) Tính năng chính
------------------
- One-page portfolio: About / Facts / Skills / Resume / Portfolio / Services / Contact
- Tự động cập nhật:
  + Age (tuổi) theo ngày sinh
  + Years of experience theo ngày bắt đầu đi làm
- Portfolio filter (lọc theo nhóm dự án)
- Slider testimonials (có thể dùng dạng “Working style highlights” hoặc ẩn)
- Responsive (desktop/mobile)

3) Cấu trúc thư mục (tham khảo)
-------------------------------
/index.html
/assets/
  /css/
  /js/
  /img/
    profile-img.jpg
    /portfolio/  (ảnh portfolio)
    /testimonials/ (ảnh testimonials - nếu dùng)
  /vendor/ (nếu template có)

4) Cách chỉnh nội dung nhanh
----------------------------
- Mở file index.html và tìm các section theo id:
  #about, #facts, #skills, #resume, #portfolio, #services, #testimonials, #contact

- Thay ảnh:
  + Ảnh avatar: assets/img/profile-img.jpg (hoặc path tương ứng trong template)
  + Ảnh portfolio: assets/img/portfolio/portfolio-*.jpg

- Thay link social (LinkedIn/GitHub/Email…) ở phần header / contact.

5) Auto Age & Years of Experience
--------------------------------
Để số tuổi và số năm kinh nghiệm tự cập nhật, dùng 2 class sau trong HTML:

- Tuổi: <span class="js-age">25</span>
- Kinh nghiệm: <span class="js-exp-years">5</span>

Sau đó thêm script dưới đây trước thẻ </body> (hoặc đưa vào assets/js/custom.js):

<script>
(function () {
  const BIRTHDAY = "1995-01-22";     // YYYY-MM-DD
  const WORK_START = "2019-01-01";   // YYYY-MM-DD

  function fullYearsSince(dateStr, asOf = new Date()) {
    const start = new Date(dateStr + "T00:00:00");
    let years = asOf.getFullYear() - start.getFullYear();
    const m = asOf.getMonth() - start.getMonth();
    if (m < 0 || (m === 0 && asOf.getDate() < start.getDate())) years--;
    return Math.max(0, years);
  }

  const age = fullYearsSince(BIRTHDAY);
  const expYears = fullYearsSince(WORK_START);

  const ageEls = document.getElementsByClassName("js-age");
  for (let i = 0; i < ageEls.length; i++) ageEls[i].textContent = age;

  const expEls = document.getElementsByClassName("js-exp-years");
  for (let i = 0; i < expEls.length; i++) expEls[i].textContent = expYears;
})();
</script>

6) Contact Form: xử lý “ai gửi thì mình nhận ở đâu?”
----------------------------------------------------
Lưu ý quan trọng:
- Nếu bạn host bằng GitHub Pages: KHÔNG chạy được PHP backend.
  => form action="forms/contact.php" sẽ không gửi mail được.

Giải pháp đề xuất (không cần backend):
A) Formspree (khuyên dùng)
- Đăng ký Formspree và lấy endpoint dạng:
  https://formspree.io/f/XXXXYYYY
- Đổi form:
  <form action="https://formspree.io/f/XXXXYYYY" method="POST" class="php-email-form">

- (Tuỳ chọn) Nếu muốn giữ UI Loading/Sent của template, dùng fetch submit:
  (Có thể hỏi ChatGPT để lấy đoạn JS submit fetch tương thích template của bạn.)

B) Netlify Forms
- Nếu bạn deploy qua Netlify, có thể bật Netlify Forms để nhận submission trên dashboard.

C) EmailJS
- Gửi mail từ phía client. Cần cấu hình chống spam (không khuyên nếu không kiểm soát).

7) Deploy lên GitHub Pages
--------------------------
- Push code lên GitHub repo
- Vào Settings -> Pages
- Chọn branch (thường là main) và folder root
- Save và chờ GitHub build
- Site sẽ có dạng: https://<username>.github.io/<repo>/

8) Gợi ý nội dung phù hợp với định vị của Louis
-----------------------------------------------
- Skills: Laravel/PHP, MySQL, Vue/TS, AdTech (GAM + header bidding concepts), GA4 reporting, DevOps, WordPress ops
- Resume: nêu rõ vai trò AdTech/GAM tại Magic Media
- Portfolio: nhóm Web Apps / AdTech / Analytics & Tools / DevOps-Ops
- Testimonials: nếu chưa có quote thật => dùng “Working style highlights” hoặc “References available upon request”

9) Credits / License
--------------------
- Template: iPortfolio by BootstrapMade (vui lòng giữ credit theo điều khoản của template).
- Framework/UI: Bootstrap + các vendor đi kèm trong template (AOS/Swiper/PureCounter… tùy bản bạn dùng).
- Icons: Bootstrap Icons / Boxicons (tùy template).

10) Liên hệ
-----------
- Email: trunbiz.dev@gmail.com
- Phone: (+84) 363 243 133
- Location: Phu Do, Nam Tu Liem, Ha Noi

========================================
End of README.txt
========================================