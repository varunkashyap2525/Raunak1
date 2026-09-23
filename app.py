from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bikeebo - Loan Par Phone</title>
<style>
body{font-family:Arial; margin:0; background:#f0f2f5;}
.header{background:#000; color:white; padding:14px; text-align:center; font-size:22px; font-weight:bold; letter-spacing:1px;}
.sub{ background:#ffe600; text-align:center; padding:6px; font-weight:bold;}
.grid{display:grid; grid-template-columns:1fr 1fr; gap:10px; padding:10px;}
.card{background:white; border-radius:10px; padding:10px; text-align:center; box-shadow:0 1px 4px #ccc;}
.card img{width:90px; height:110px; object-fit:contain;}
.card h4{font-size:13px; margin:5px 0; height:32px; overflow:hidden;}
.price{color:#0a8a00; font-weight:bold; font-size:14px; margin:2px;}
.emi{color:#ff5500; font-size:11px; margin:2px;}
.btn{background:#000; color:white; padding:6px 12px; border-radius:20px; font-size:12px; text-decoration:none; display:inline-block; margin-top:5px;}
</style>
</head>
<body>
<div class="header">BIKEEBO</div>
<div class="sub">Loan Par Phone - EMI ₹500 se Shuru</div>

<div class="grid">

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-17-pro-max.jpg">
<h4>iPhone 17 Pro Max</h4>
<p class="price">₹1,39,900</p>
<p class="emi">EMI ₹3999/m</p>
<a class="btn" href="/order">Buy Now</a>
</div>

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-16-pro-max.jpg">
<h4>iPhone 16 Pro Max</h4>
<p class="price">₹1,19,900</p>
<p class="emi">EMI ₹2999/m</p>
<a class="btn" href="/order">Buy Now</a>
</div>

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-15-pro-max.jpg">
<h4>iPhone 15 Pro Max</h4>
<p class="price">₹89,900</p>
<p class="emi">EMI ₹2499/m</p>
<a class="btn" href="/order">Buy Now</a>
</div>

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-14-pro.jpg">
<h4>iPhone 14 Pro</h4>
<p class="price">₹69,900</p>
<p class="emi">EMI ₹1999/m</p>
<a class="btn" href="/order">Buy Now</a>
</div>

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-ultra-5g.jpg">
<h4>Samsung S24 Ultra</h4>
<p class="price">₹1,29,999</p>
<p class="emi">EMI ₹2999/m</p>
<a class="btn" href="/order">Buy Now</a>
</div>

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-ultra-5g.jpg">
<h4>Samsung S23 Ultra</h4>
<p class="price">₹84,999</p>
<p class="emi">EMI ₹1999/m</p>
<a class="btn" href="/order">Buy Now</a>
</div>

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/oneplus-12.jpg">
<h4>OnePlus 12</h4>
<p class="price">₹59,999</p>
<p class="emi">EMI ₹1499/m</p>
<a class="btn" href="/order">Buy Now</a>
</div>

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-13-pro-plus.jpg">
<h4>Redmi Note 13 Pro+</h4>
<p class="price">₹28,999</p>
<p class="emi">EMI ₹799/m</p>
<a class="btn" href="/order">Buy Now</a>
</div>

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/vivo-v30-pro.jpg">
<h4>Vivo V30 Pro</h4>
<p class="price">₹41,999</p>
<p class="emi">EMI ₹999/m</p>
<a class="btn" href="/order">Buy Now</a>
</div>

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/realme-narzo-70-pro.jpg">
<h4>Realme Narzo 70</h4>
<p class="price">₹15,999</p>
<p class="emi">EMI ₹500/m</p>
<a class="btn" href="/order">Buy Now</a>
</div>

</div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/order')
def order():
    return """
    <div style='font-family:Arial; padding:20px;'>
    <h3>Bikeebo - Order Form</h3>
    <form action='/thanks'>
    <input style='width:100%; padding:10px; margin:5px 0;' placeholder='Naam' required><br>
    <input style='width:100%; padding:10px; margin:5px 0;' placeholder='Phone Number' required><br>
    <input style='width:100%; padding:10px; margin:5px 0;' placeholder='City' required><br>
    <input style='width:100%; padding:10px; margin:5px 0;' placeholder='Full Address' required><br>
    <button style='width:100%; padding:12px; background:black; color:white; border-radius:8px; margin-top:10px;'>Loan Ke Liye Apply Kare</button>
    <p style='font-size:12px; color:gray;'>Hamari team 2 ghante me call karegi. Koi advance payment nahi dena hai.</p>
    </form></div>
    """

@app.route('/thanks')
def thanks():
    return "<h2 style='text-align:center; margin-top:100px;'>Order Received! Bikeebo team call karegi.</h2>"

if __name__ == '__main__':
    app.run()
