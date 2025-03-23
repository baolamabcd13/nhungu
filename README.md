## 🚀 Cách cài đặt & chạy

### 1. Clone dự án từ GitHub

```bash
git https://github.com/baolamabcd13/nhungu.git
cd nhungu
```

---

### 2. Cài đặt thư viện Python

```bash
pip install -r requirements.txt
```

File `requirements.txt` bao gồm:

```
graphviz
matplotlib
```

---

### 3. Cài đặt Graphviz trên Windows

Để sử dụng được `graphviz` trong Python:

#### ✅ Bước 1: Tải Graphviz

Tải bản cài đặt chính thức từ:  
👉 https://graphviz.gitlab.io/_pages/Download/Download_windows.html

#### ✅ Bước 2: Cài đặt và thêm vào PATH

- Trong quá trình cài đặt, **chọn tùy chọn "Add Graphviz to the system PATH for all users"**
- Nếu quên, bạn có thể thêm thủ công vào PATH:
  - Thêm thư mục: `C:\Program Files\Graphvizin` vào biến môi trường PATH
  - Khởi động lại máy (hoặc terminal) để áp dụng

---

### 4. Chạy script tạo hình

```bash
python draw_graphviz.py
python LBPSL.py
python stacked_bar_chart.py
```
