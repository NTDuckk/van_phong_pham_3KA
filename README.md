1. Cài đặt

Bước 1: Clone repository

Sao chép mã nguồn từ GitHub và truy cập thư mục:

git clone https://github.com/NTDuckk/van_phong_pham_3KA.git
cd van-phong-pham-3ka

Bước 2: Tạo và kích hoạt virtual environment

Tạo môi trường ảo Python và kích hoạt:

python -m venv venv
source venv/bin/activate  # Trên Windows sử dụng: venv\Scripts\activate

Bước 3: Cài đặt các package cần thiết

Cài đặt các thư viện được khai báo trong file requirements.txt:

pip install -r requirements.txt

Bước 4: Thiết lập kết nối CSDL

Cấu hình kết nối ở file db_Connection.py cho MongoDB và SQL Server theo nhu cầu.

2. Sử dụng

Bước 1: Chạy Flask application

Chạy file chính của ứng dụng Flask:

python app.py

Bước 2: Truy cập trang web

Mở trình duyệt web và truy cập:

http://127.0.0.1:5000
