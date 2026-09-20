from flask import Flask, request, render_template_string, redirect, session
import os

app = Flask(__name__)
app.secret_key = "raunak1989"

LOGIN_HTML = """
<!DOCTYPE html>
<html><head>
<meta name="google-site-verification" content="v0e90DURVgaMKfgFdZWb6kkAKtmoXgbV17BJ6WnhI9o" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Raunak Singh - Best Website Designer in Lucknow">
<style>
body{background:black;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;font-family:monospace}
.box{border:2px solid #00ff00;padding:25px;width:330px;text-align:center;box-shadow:0 0 20px #00ff00;background:#000}
h2{color:#00ff00} p{color:white}
input{width:90%;padding:10px;margin:15px 0;background:#111;color:#00ff00;border:1px solid #00ff00;text-align:center}
.btn{background:blue;color:white;border:none;padding:12px;width:100%;font-weight:bold;font-size:16px;cursor:pointer}
</style></head>
<body>
<div class="box">
<h2>SECURE LOGIN</h2>
<p>Welcome to my website</p>
<form method="POST">
<p style="color:#00ff00">Password yaha dalo:</p>
<input type="password" name="pwd" placeholder="Password" required>
<button class="btn" type="submit">LOGIN</button>
</form>
<p style="font-size:11px;color:#555">Password = 1989</p>
</div>
</body></html>
"""

FORM_HTML = """
<!DOCTYPE html>
<html><head>
<meta name="google-site-verification" content="v0e90DURVgaMKfgFdZWb6kkAKtmoXgbV17BJ6WnhI9o" />
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{background:black;color:#00ff00;font-family:monospace;padding:20px}
.container{max-width:500px;margin:20px auto;background:rgba(0,10,0,0.95);border:2px solid #00ff00;padding:25px;box-shadow:0 0 20px #00ff00}
h1{text-align:center} input,select{width:100%;padding:12px;margin:8px 0;background:#000;border:1px solid #00ff00;color:#00ff00;box-sizing:border-box}
.btn{background:blue;color:white;border:none;padding:14px;width:100%;font-weight:bold;font-size:16px;cursor:pointer;margin-top:10px}
</style></head>
<body>
<div class="container">
<h1>WELCOME TO MY WEBSITE</h1>
<p style="color:white;text-align:center">Is website ko banane wala Raunak Singh hai</p>
<h3 style="text-align:center">CLIENT FORM</h3>
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
<p style="text-align:center;color:#555;font-size:12px;margin-top:10px">Contact: Raunakkashyap1989@gmail.com</p>
</div>
</body></html>
"""

SUCCESS_HTML = """
<!DOCTYPE html><html><body style="background:black;color:#00ff00;font-family:monospace;display:flex;justify-content:center;align-items:center;height:100vh;text-align:center">
<div style="border:2px solid #00ff00;padding:30px;box-shadow:0 0 20px #00ff00">
<h1>✅ बधाई हो! सबमिट हो गया</h1>
<p style="color:white;font-size:18px">आपसे जल्दी संपर्क होगा!</p>
<a href="/home" style="color:blue">Wapas jao</a>
</div></body></html>
"""

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST' and request.form.get('pwd') == '1989':
        session['ok'] = True
        return redirect('/home')
    return render_template_string(LOGIN_HTML)

@app.route('/home')
def home():
    if not session.get('ok'): return redirect('/')
    return render_template_string(FORM_HTML)

@app.route('/submit', methods=['POST'])
def submit():
    if not session.get('ok'): return redirect('/')
    print("NEW LEAD:", dict(request.form))
    return render_template_string(SUCCESS_HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT",10000)))
