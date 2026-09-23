from flask import Flask, render_template_string, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Gmail Setting
GMAIL_USER = "Raunakkashyap1989@gmail.com"
GMAIL_APP_PASSWORD = "YAHAN_APP_PASSWORD_DAALO" # 16 digit
TO_EMAIL = "Raunakkashyap1989@gmail.com"

def send_mail(name, mobile, city, model):
    try:
        body = f"New Lead: {model}\nName: {name}\nMobile: {mobile}\nCity: {city}"
        msg = MIMEText(body)
        msg['Subject'] = f"Bikeebo Lead - {model} - {name}"
        msg['From'] = GMAIL_USER
        msg['To'] = TO_EMAIL
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        s.send_message(msg)
        s.quit()
    except Exception as e:
        print(e)

PHONES = [
("Apple iPhone 17 Pro Max","https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-17-pro-max.jpg","139900","500*"),
("Apple iPhone 16 Pro Max","https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-16-pro-max.jpg","119900","700*"),
("Apple iPhone 15","https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-15.jpg","69900","700*"),
("Samsung S24 Ultra","https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-ultra-5g.jpg","129999","700*"),
("Samsung S23 Ultra","https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-ultra-5g.jpg","84999","700*"),
("Samsung S23 FE","https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-fe.jpg","39999","600/m"),
("Samsung A55","https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a55.jpg","36999","500/m"),
("Samsung A35","https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a35.jpg","28999","500/m"),
("OnePlus 12","https://fdn2.gsmarena.com/vv/bigpic/oneplus-12.jpg","59999","600/m"),
("OnePlus 11R","https://fdn2.gsmarena.com/vv/bigpic/oneplus-11r-5g.jpg","39999","500/m"),
("OnePlus Nord CE4","https://fdn2.gsmarena.com/vv/bigpic/oneplus-nord-ce4.jpg","24999","500/m"),
("Vivo V30 Pro","https://fdn2.gsmarena.com/vv/bigpic/vivo-v30-pro.jpg","41999","500/m"),
("Vivo T3 Pro","https://fdn2.gsmarena.com/vv/bigpic/vivo-t3-pro.jpg","24999","500/m"),
("Vivo Y200","https://fdn2.gsmarena.com/vv/bigpic/vivo-y200.jpg","20999","500/m"),
("Redmi Note 13 Pro+","https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-13-pro-plus.jpg","28999","500/m"),
("Redmi Note 13 Pro","https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-13-pro.jpg","24999","500/m"),
("Redmi Note 12 Pro","https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-12-pro.jpg","19999","500/m"),
("Realme Narzo 70 Pro","https://fdn2.gsmarena.com/vv/bigpic/realme-narzo-70-pro.jpg","15999","500/m"),
("Realme 12 Pro+","https://fdn2.gsmarena.com/vv/bigpic/realme-12-pro-plus.jpg","27999","500/m"),
("Oppo Reno11 Pro","https://fdn2.gsmarena.com/vv/bigpic/oppo-reno11-pro.jpg","39999","500/m"),
("Oppo F25 Pro","https://fdn2.gsmarena.com/vv/bigpic/oppo-f25-pro.jpg","23999","500/m"),
("Infinix Note 40 Pro","https://fdn2.gsmarena.com/vv/bigpic/infinix-note-40-pro.jpg","18999","500/m"),
("Poco X6 Pro","https://fdn2.gsmarena.com/vv/bigpic/xiaomi-poco-x6-pro.jpg","19999","500/m"),
("iQOO Z9","https://fdn2.gsmarena.com/vv/bigpic/vivo-iqoo-z9.jpg","18999","500/m"),
("Nothing Phone 2","https://fdn2.gsmarena.com/vv/bigpic/nothing-phone2.jpg","34999","500/m"),
("Motorola Edge 50 Pro","https://fdn2.gsmarena.com/vv/bigpic/motorola-edge-50-pro.jpg","30999","500/m"),
]

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bikeebo - 25 Phones</title>
<style>
body{margin:0; font-family:Arial; background: linear-gradient(270deg, #0f0c29, #302b63, #24243e); background-size: 600% 600%; animation: bgMove 10s ease infinite; color:white;}
@keyframes bgMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.header{background:rgba(0,0,0,0.8); padding:12px; text-align:center; font-size:22px; font-weight:bold; position:sticky; top:0; z-index:10;}
.sticker{background:#ffeb3b; color:black; text-align:center; padding:6px; font-weight:bold; font-size:13px; animation: blink 1s infinite;}
@keyframes blink{50%{opacity:0.6}}
.grid{display:grid; grid-template-columns:1fr 1fr; gap:8px; padding:10px;}
.card{background:white; color:black; border-radius:12px; padding:10px; text-align:center; box-shadow:0 2px 8px rgba(0,0,0,0.3);}
.card img{width:85px; height:95px; object-fit:contain;}
.card h4{font-size:11px; height:30px; margin:5px 0;}
.price{color:green; font-weight:bold; font-size:12px;}
.emi{color:red; font-size:11px; font-weight:bold;}
.btn{background:#2874f0; color:white; padding:6px; border-radius:15px; text-decoration:none; font-size:11px; display:block; margin-top:4px;}
.form-wrap{display:flex; justify-content:center; padding:20px;}
.form-box{background:white; color:black; width:100%; max-width:400px; padding:22px; border-radius:16px; box-shadow:0 5px 20px rgba(0,0,0,0.5);}
.form-box h2{text-align:center; margin:0 0 10px;}
.form-box input{width:100%; padding:14px; margin:8px 0; border-radius:8px; border:1px solid #ccc; box-sizing:border-box; font-size:15px;}
.form-box button{width:100%; padding:14px; background:#fb641b; color:white; border:none; border-radius:8px; font-size:16px; font-weight:bold;}
#msg{text-align:center; font-weight:bold; margin-top:10px; color:green;}
</style>
</head>
<body>
<div class="header">BIKEEBO</div>
<div class="sticker">🔥 SALE - Loan Par Phone - EMI ₹500 se Shuru 🔥 - Free Delivery 🔥</div>

<div class="grid">
{% for name, img, price, emi in phones %}
<div class="card">
<img src="{{img}}">
<h4>{{name}}</h4>
<div class="price">₹{{price}}</div>
<div class="emi">EMI {{emi}}</div>
<a class="btn" href="#orderForm" onclick="setPhone('{{name}}')">Buy Now</a>
</div>
{% endfor %}
</div>

<div class="sticker">💥 25+ Phones Available - Best Price - All India Delivery 💥</div>

<div class="form-wrap">
<div class="form-box" id="orderForm">
<h2>Loan / Order Form</h2>
<input type="hidden" id="phone_model" value="Bikeebo Phone">
<input id="name" placeholder="Pura Naam*" required>
<input id="mobile" placeholder="Mobile Number*" required>
<input id="city" placeholder="City / Jila*" required>
<button onclick="submitForm()">SUBMIT - FAST</button>
<div id="msg"></div>
<p style="font-size:11px; color:gray; text-align:center;">* iPhone par EMI downpayment ke baad. 500-700 wali EMI 20k tak ke phones par.</p>
</div>
</div>

<div class="sticker">© Bikeebo - Aapse Jaldi Sampark Hoga</div>

<script>
function setPhone(n){
 document.getElementById('phone_model').value = n;
 document.getElementById('orderForm').scrollIntoView({behavior:'smooth'});
}
function submitForm(){
 let name=document.getElementById('name').value;
 let mobile=document.getElementById('mobile').value;
 let city=document.getElementById('city').value;
 let model=document.getElementById('phone_model').value;
 if(!name || !mobile || !city){alert('Form bhariye'); return;}
 document.getElementById('msg').innerText='Submitting...';
 fetch('/submit', {
   method:'POST',
   headers:{'Content-Type':'application/json'},
   body: JSON.stringify({name:name, mobile:mobile, city:city, model:model})
 }).then(r=>r.json()).then(d=>{
   document.getElementById('msg').innerText='✓ Ho Gaya! Aapse Jaldi Sampark Hoga';
   document.getElementById('name').value=''; document.getElementById('mobile').value=''; document.getElementById('city').value='';
 }).catch(e=>{
   document.getElementById('msg').innerText='Error - Dobara try karo';
 });
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, phones=PHONES)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    send_mail(data.get('name'), data.get('mobile'), data.get('city'), data.get('model'))
    return {"status":"ok"}

if __name__ == '__main__':
    app.run()
