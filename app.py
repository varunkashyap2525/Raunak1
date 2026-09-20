from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html><head>
<meta name="google-site-verification" content="v0e90DURVgaMKfgFdZWb6kkAKtmoXgbV17BJ6WnhI9o" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Raunak Singh - Best Website Designer in Lucknow, Uttar Pradesh">
<title>Raunak Singh - Website Designer Lucknow</title>
<style>
body{background:black;color:#00ff00;font-family:monospace;padding:20px;margin:0}
.container{max-width:500px;margin:20px auto;background:rgba(0,10,0,0.95);border:2px solid #00ff00;padding:25px;box-shadow:0 0 20px #00ff00}
h1{text-align:center;text-shadow:0 0 10px #00ff00}
input,select{width:100%;padding:12px;margin:8px 0;background:#000;border:1px solid #00ff00;color:#00ff00;box-sizing:border-box}
.btn{background:blue;color:white;border:none;padding:14px;width:100%;font-weight:bold;font-size:16px;cursor:pointer;margin-top:10px}
.btn:hover{background:#00ff00;color:#000;box-shadow:0 0 10px #00ff00}
.success{border:2px solid #00ff00;padding:30px;text-align:center;box-shadow:0 0 20px #00ff00}
</style></head>
<body>
<div class="container">
<h1>WELCOME TO MY WEBSITE</h1>
<p style="color:white;text-align:center">Is website ko banane wala Raunak Singh hai</p>
<h3 style="text-align:center">>> CLIENT FORM <<</h3>
<form action="/submit" method="POST">
<input type="text" name="username" placeholder="Username *" required>
<input type="tel" name="phone" placeholder="Phone Number *" required>
<input type="text" name="father" placeholder="Father Name *" required>
<input type="text" name="mother" placeholder="Mother Name *" required>
<input type="tel" name="phone2" placeholder="Second Phone Number">
<select name="website_type" required>
<option value="">Kis Prakar ki Website Chahiye? *</option>
<option>Business Website</option>
<option>Portfolio Website</option>
<option>E-Commerce Shop</option>
<option>Blog / News</option>
<option>Hacking / Cyber</option>
<option>Other</option>
</select>
<button class="btn" type="submit">SUBMIT</button>
</form>
<p style="text-align:center;color:#555;font-size:12px;margin-top:15px">Contact: Raunakkashyap1989@gmail.com | Lucknow, UP</p>
</div>
</body></html>
"""

SUCCESS_HTML = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
<body style="background:black;color:#00ff00;font-family:monospace;display:flex;justify-content:center;align-items:center;height:100vh;text-align:center">
<div style="border:2px solid #00ff00;padding:30px;box-shadow:0 0 20px #00ff00;max-width:400px">
<h1>✅ बधाई हो! सबमिट हो गया</h1>
<p style="color:white;font-size:18px;margin-top:15px">आपसे जल्दी संपर्क होगा!</p>
<p style="color:#aaa;margin-top:10px">Raunak Singh aapse jaldi baat karega.</p>
<a href="/" style="color:blue;text-decoration:none;display:block;margin-top:20px">← Wapas jao</a>
</div></body></html>
"""

@app.route('/', methods=['GET'])
def home():
    return render_template_string(HTML_PAGE)

@app.route('/submit', methods=['POST'])
def submit():
    data = dict(request.form)
    print("NEW LEAD RECEIVED:", data)  # Ye Render ke logs me dikhega
    return render_template_string(SUCCESS_HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT",10000)))
