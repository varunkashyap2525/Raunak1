from flask import Flask, request, render_template_string, redirect, session
import os
app = Flask(__name__)
app.secret_key = "raunak1989"

login_html = """
<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
body{background:#000;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;font-family:Arial}
.box{border:2px solid #0f0;padding:25px;width:300px;text-align:center;box-shadow:0 0 15px #0f0}
input{width:90%;padding:10px;margin:15px 0;background:#111;color:#0f0;border:1px solid #0f0;text-align:center}
.btn{background:blue;color:#fff;border:none;padding:10px;width:100%;font-weight:bold;font-size:16px}
</style></head>
<body><div class="box">
<h2 style="color:#0f0">SECURE LOGIN</h2>
<p style="color:#fff">Welcome to my website</p>
<form method="POST">
<p style="color:#0f0">Password yaha dalo:</p>
<input type="password" name="pwd" required placeholder="Enter Password">
<button class="btn" type="submit">LOGIN</button>
</form>
<p style="color:#555;font-size:11px">Password = 1989</p>
</div></body></html>
"""

home_html = """
<!DOCTYPE html><html><body style="background:black;color:#0f0;text-align:center;font-family:monospace;padding:30px">
<h1 style="border:2px solid #0f0;padding:20px">WELCOME TO MY WEBSITE</h1>
<h2 style="color:white">Is website ko banane wala Raunak Singh hai</h2>
<p>Contact: Raunakkashyap1989@gmail.com</p>
</body></html>
"""

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST' and request.form.get('pwd') == '1989':
        session['ok']=True
        return redirect('/home')
    return render_template_string(login_html)

@app.route('/home')
def home():
    if not session.get('ok'):
        return redirect('/')
    return render_template_string(home_html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT",10000)))
