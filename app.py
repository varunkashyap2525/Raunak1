from flask import Flask, render_template_string, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# --- GMAIL SETTING ---
# Isme apna Gmail aur App Password daalna hai
# App Password kaise banta hai neeche likha hai
GMAIL_USER = "Raunakkashyap1989@gmail.com"
GMAIL_APP_PASSWORD = "YAHAN_APP_PASSWORD_DAALO"  # 16 digit ka hota hai
TO_EMAIL = "Raunakkashyap1989@gmail.com"

def send_lead_email(name, mobile, city, phone_model):
    try:
        subject = f"New Bikeebo Lead: {phone_model} - {name}"
        body = f"""
        Naya Order Aaya Hai Bikeebo Par:

        Phone Model: {phone_model}
        Customer Name: {name}
        Mobile: {mobile}
        City: {city}

        Jaldi Call Karo!
        """
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = GMAIL_USER
        msg['To'] = TO_EMAIL

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("Mail Sent!")
        return True
    except Exception as e:
        print("Mail Error:", e)
        return False

HOME_HTML = """
<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bikeebo</title>
<style>
body{margin:0; font-family:Arial; background:#f1f3f6;}
.header{background:#2874f0; color:white; padding:14px; text-align:center; font-weight:bold; font-size:20px;}
.grid{display:grid; grid-template-columns:1fr 1fr; gap:8px; padding:10px;}
.card{background:white; padding:10px; border-radius:8px; text-align:center;}
.card img{width:80px; height:90px; object-fit:contain;}
.card h4{font-size:12px; height:28px; margin:5px 0;}
.price{color:green; font-weight:bold; font-size:13px;}
.emi{color:#d32f2f; font-size:11px;}
.btn{display:block; background:#fb641b; color:white; padding:8px; border-radius:4px; text-decoration:none; font-size:13px; margin-top:6px;}
</style></head><body>
<div class="header">BIKEEBO - Loan Par Phone</div>
<div class="grid">
<div class="card"><img src="https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-17-pro-max.jpg"><h4>iPhone 17 Pro Max</h4><p class="price">₹1,39,900</p><p class="emi">EMI ₹500 se Shuru*</p><a class="btn" href="/order?phone=iPhone 17 Pro Max">Buy Now</a></div>
<div class="card"><img src="https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-13-pro-plus.jpg"><h4>Redmi Note 13 Pro+</h4><p class="price">₹18,999</p><p class="emi">EMI ₹500/m</p><a class="btn" href="/order?phone=Redmi Note 13">Buy Now</a></div>
<div class="card"><img src="https://fdn2.gsmarena.com/vv/bigpic/realme-narzo-70-pro.jpg"><h4>Realme Narzo 70</h4><p class="price">₹14,999</p><p class="emi">EMI ₹500/m</p><a class="btn" href="/order?phone=Realme Narzo 70">Buy Now</a></div>
<div class="card"><img src="https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-ultra-5g.jpg"><h4>Samsung S24 Ultra</h4><p class="price">₹1,19,999</p><p class="emi">EMI ₹700/m*</p><a class="btn" href="/order?phone=S24 Ultra">Buy Now</a></div>
</div>
</body></html>
"""

@app.route('/')
def home():
    return render_template_string(HOME_HTML)

@app.route('/order')
def order():
    phone = request.args.get('phone','Phone')
    return render_template_string("""
    <div style="font-family:Arial; background:#f1f3f6; min-height:100vh; padding:15px;">
    <div style="background:white; padding:20px; border-radius:10px;">
    <h3>{{phone}} - Delivery Details</h3>
    <form action="/submit" method="post">
    <input type="hidden" name="phone_model" value="{{phone}}">
    <input name="name" placeholder="Pura Naam" required style="width:100%; padding:14px; margin:8px 0; border-radius:6px; border:1px solid #ccc;">
    <input name="mobile" placeholder="Mobile Number" required style="width:100%; padding:14px; margin:8px 0; border-radius:6px; border:1px solid #ccc;">
    <input name="city" placeholder="City" required style="width:100%; padding:14px; margin:8px 0; border-radius:6px; border:1px solid #ccc;">
    <button style="width:100%; padding:15px; background:#2874f0; color:white; border:none; border-radius:6px; font-weight:bold; font-size:16px;">Submit Karo</button>
    </form></div></div>
    """, phone=phone)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    mobile = request.form.get('mobile')
    city = request.form.get('city')
    model = request.form.get('phone_model')
    
    # Mail bhejo
    send_lead_email(name, mobile, city, model)
    
    return """
    <div style='text-align:center; padding:80px 20px; font-family:Arial;'>
    <h1 style='color:green;'>✓ Order Mil Gaya!</h1>
    <h2>Aapse Jaldi Sampark Hoga</h2>
    <p>Tumhara details Raunakkashyap1989@gmail.com par bhej diya gaya hai.</p>
    </div>
    """

if __name__ == '__main__':
    app.run()
