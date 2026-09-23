from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bikeebo - Loan Par Phone</title>
<style>
body{font-family:Arial; margin:0; background:#f5f5f5;}
.header{background:#111; color:white; padding:15px; text-align:center; font-size:22px;}
.banner{background:#007bff; color:white; text-align:center; padding:10px;}
.card{background:white; margin:15px; border-radius:12px; padding:15px; box-shadow:0 2px 8px #ccc; text-align:center;}
.card img{width:150px; height:150px; object-fit:contain;}
.price{color:green; font-weight:bold; font-size:18px;}
.emi{color:#ff6600; font-size:14px;}
.btn{background:#111; color:white; padding:10px 20px; border:none; border-radius:8px; margin-top:10px; cursor:pointer; display:inline-block; text-decoration:none;}
.form{padding:20px; background:white; margin:20px; border-radius:10px;}
input{width:100%; padding:10px; margin:6px 0; border:1px solid #ccc; border-radius:6px;}
</style>
</head>
<body>
<div class="header">Bikeebo - Sabse Sasta Loan Par Phone</div>
<div class="banner">EMI sirf ₹500/month se shuru | All India Delivery</div>

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-17.jpg">
<h3>iPhone 17 Pro Max</h3>
<p class="price">₹1,19,900</p>
<p class="emi">Loan Par Uplabdh - EMI ₹3,999/month</p>
<a class="btn" href="/order">Buy Now</a>
</div>

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-16-pro-max.jpg">
<h3>iPhone 16</h3>
<p class="price">₹79,900</p>
<p class="emi">Loan Par Uplabdh - EMI ₹2,499/month</p>
<a class="btn" href="/order">Buy Now</a>
</div>

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-15-pro-max.jpg">
<h3>iPhone 15</h3>
<p class="price">₹69,900</p>
<p class="emi">Loan Par Uplabdh - EMI ₹1,999/month</p>
<a class="btn" href="/order">Buy Now</a>
</div>

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-14-pro-max.jpg">
<h3>iPhone 14</h3>
<p class="price">₹59,900</p>
<p class="emi">Loan Par Uplabdh - EMI ₹1,499/month</p>
<a class="btn" href="/order">Buy Now</a>
</div>

<div class="card">
<img src="https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-13.jpg">
<h3>Android Phone - Redmi Note 13</h3>
<p class="price">₹18,999</p>
<p class="emi">Loan Par Uplabdh - EMI ₹500/month</p>
<a class="btn" href="/order">Buy Now</a>
</div>

</body>
</html>
"""

ORDER_HTML = """
<div style="font-family:Arial; padding:20px;">
<h2>Bikeebo - Order Form</h2>
<div class="form">
<form action="/thanks">
<input type="text" placeholder="Apna Naam" required>
<input type="tel" placeholder="Phone Number" required>
<input type="text" placeholder="City Name" required>
<input type="text" placeholder="Full Address" required>
<p style="font-size:13px; color:gray;">Note: Loan approval ke baad hamari team aapko call karegi. Koi advance payment QR par na kare.</p>
<input type="submit" value="Order Confirm Karo" style="background:#007bff; color:white; border:none;">
</form>
</div>
</div>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/order')
def order():
    return render_template_string(ORDER_HTML)

@app.route('/thanks')
def thanks():
    return "<h1 style='text-align:center; margin-top:100px;'>Thank You! Bikeebo Team jaldi call karegi.</h1>"

if __name__ == '__main__':
    app.run()
