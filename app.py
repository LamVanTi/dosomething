from flask import Flask, request, render_template_string
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Lấy IP
    if request.headers.get('X-Forwarded-For'):
        ip = request.headers.get('X-Forwarded-For')
    else:
        ip = request.remote_addr

    # Lưu log IP (chỉ IP thôi)
    time = datetime.datetime.now()
    with open("log.txt", "a") as f:
        f.write(f"{time} - {ip}\n")

    # HTML form
    html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Khảo sát sinh viên</title>
    <style>
        * {
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .container {
            background: #ffffff;
            padding: 35px;
            border-radius: 16px;
            width: 360px;
            box-shadow: 0 15px 40px rgba(0,0,0,0.15);
            animation: fadeIn 0.5s ease;
        }

        h2 {
            text-align: center;
            margin-bottom: 25px;
            color: #333;
        }

        label {
            font-size: 14px;
            font-weight: 600;
            color: #444;
            display: block;
            margin-bottom: 5px;
        }

        input, select, textarea {
            width: 100%;
            padding: 10px 12px;
            margin-bottom: 15px;
            border-radius: 8px;
            border: 1px solid #ddd;
            background: #f9f9f9;
            transition: all 0.25s ease;
            font-size: 14px;
        }

        input:focus, select:focus, textarea:focus {
            border-color: #667eea;
            background: #fff;
            outline: none;
            box-shadow: 0 0 0 3px rgba(102,126,234,0.2);
        }

        input[type="checkbox"] {
            width: auto;
            margin-right: 8px;
            transform: scale(1.1);
        }

        .checkbox-group {
            margin-bottom: 15px;
        }

        .checkbox-group label {
            font-weight: normal;
            display: flex;
            align-items: center;
            margin-bottom: 6px;
        }

        button {
            width: 100%;
            padding: 12px;
            background: linear-gradient(135deg, #667eea, #764ba2);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
    </style>
</head>

<body>

<div class="container">
    <h2>Khảo sát nhu cầu sinh viên</h2>

    <form method="POST" action="/submit">

        <label>Bạn đang là sinh viên năm mấy?</label>
        <select name="year">
            <option>Năm 1</option>
            <option>Năm 2</option>
            <option>Năm 3</option>
            <option>Năm 4</option>
        </select>

        <label>Nhu cầu sinh hoạt bạn quan tâm:</label>
        <div class="checkbox-group">
            <label><input type="checkbox" name="need" value="wifi"> Wifi miễn phí</label>
            <label><input type="checkbox" name="need" value="study_space"> Không gian học tập</label>
            <label><input type="checkbox" name="need" value="canteen"> Căn tin giá rẻ</label>
            <label><input type="checkbox" name="need" value="parking"> Bãi giữ xe</label>
            <label><input type="checkbox" name="need" value="library"> Thư viện</label>
        </div>

        <label>Mức chi tiêu trung bình mỗi tháng:</label>
        <select name="budget">
            <option>Dưới 2 triệu</option>
            <option>2 - 4 triệu</option>
            <option>4 - 6 triệu</option>
            <option>Trên 6 triệu</option>
        </select>

        <label>Ý kiến thêm:</label>
        <textarea name="note" placeholder="Nhập ý kiến..." rows="3"></textarea>

        <button type="submit">Gửi khảo sát</button>

    </form>
</div>

</body>
</html>
"""

    return render_template_string(html_form)


@app.route('/submit', methods=['POST'])
def submit():
    # Không lưu dữ liệu form
    return "<h3>Gửi thành công!</h3>"


if __name__ == '__main__':
    app.run()