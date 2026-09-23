from flask import Flask, render_template_string, request

app = Flask(__name__)

# Tumhara WhatsApp Number
WHATSAPP_NUMBER = "917754048502"  # 91 laga ke

PHONES = [
("iPhone 17 Pro Max","https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-17-pro-max.jpg","139900","500*"),
("iPhone 16 Pro Max","https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-16-pro-max.jpg","119900","700*"),
("iPhone 15 Pro Max","https://fdn2.gsmarena.com/vv/bigpic/apple-iphone-15-pro-max.jpg","89900","700*"),
("Samsung S24 Ultra","https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s24-ultra-5g.jpg","129999","700*"),
("Samsung S23 Ultra","https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-s23-ultra-5g.jpg","84999","700*"),
("Samsung A55","https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a55.jpg","36999","500/m"),
("Samsung A35","https://fdn2.gsmarena.com/vv/bigpic/samsung-galaxy-a35.jpg","28999","500/m"),
("OnePlus 12","https://fdn2.gsmarena.com/vv/bigpic/oneplus-12.jpg","59999","600/m"),
("OnePlus 11R","https://fdn2.gsmarena.com/vv/bigpic/oneplus-11r-5g.jpg","39999","500/m"),
("OnePlus Nord CE4","https://fdn2.gsmarena.com/vv/bigpic/oneplus-nord-ce4.jpg","24999","500/m"),
("Vivo V30 Pro","https://fdn2.gsmarena.com/vv/bigpic/vivo-v30-pro.jpg","41999","500/m"),
("Vivo T3 Pro","https://fdn2.gsmarena.com/vv/bigpic/vivo-t3-pro.jpg","24999","500/m"),
("Redmi Note 13 Pro+","https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-13-pro-plus.jpg","28999","500/m"),
("Redmi Note 12 Pro","https://fdn2.gsmarena.com/vv/bigpic/xiaomi-redmi-note-12-pro.jpg","19999","500/m"),
("Realme Narzo 70 Pro","https://fdn2.gsmarena.com/vv/bigpic/realme-narzo-70-pro.jpg","15999","500/m"),
("Realme 12 Pro+","https://fdn2.gsmarena.com/vv/bigpic/realme-12-pro-plus.jpg","27999","500/m"),
("Oppo Reno11 Pro","https://fdn2.gsmarena.com/vv/bigpic/oppo-reno11-pro.jpg","39999","500/m"),
("Poco X6 Pro","https://fdn2.gsmarena.com/vv/bigpic/xiaomi-poco-x6-pro.jpg","19999","500/m"),
]

HTML = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Bikeebo</title>
<style>
body{margin:0; font-family:Arial; background: linear-gradient(270deg, #0f0c29, #302b63, #24243e); background-size: 600% 600%; animation: bgMove 10s ease infinite; }
@keyframes bgMove{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.header{background:rgba(0,0,0,0.9); color:white; padding:13px; text-align:center; font-size:22px; font-weight:bold; position:sticky; top:0; z-index:10;}
.sticker{background:#ffeb3b; color:black; text-align:center; padding:7px; font-weight:bold; font-size:13px;}
.grid{display:grid; grid-template-columns:1fr 1fr; gap:8px; padding:10px;}
.card{background:white; border-radius:12px; padding:10px; text-align:center;}
.card img{width:85px; height:95px; object-fit:contain;}
.card h4{font-size:11px; height:28px; margin:5px 0;}
.price{color:green; font-weight:bold; font-size:12px;}
.emi{color:red; font-size:11px; font-weight:bold;}
.btn{background:#2874f0; color:white; padding:7px; border-radius:15px; font-size:11px; display:block; margin-top:4px; cursor:pointer;}
#formSection{display:none; position:fixed; bottom:0; left:0; right:0; z-index:100; background:rgba(0,0,0,0.7); padding:15px;}
.form-box{background:white; border-radius:16px; padding:20px; max-width:400px; margin:0 auto;}
.form-box input{width:100%; padding:14px; margin:8px 0; border-radius:8px; border:1px solid #ccc; box-sizing:border-box;}
.form-box button{width:100%; padding:14px; background:#25D366; color:white; border:none; border-radius:8px; font-weight:bold; font-size:16px;}
.close{float:right; font-size:20px; cursor:pointer; font-weight:bold;}
</style>
</head>
<body>
<div class="header">BIKEEBO</div>
<div class="sticker">🔥 EMI ₹500 se Shuru - Loan Par Phone - 7754048502 🔥</div>

<div class="grid">
{% for name, img, price, emi in phones %}
<div class="card">
<img src="{{img}}">
<h4>{{name}}</h4>
<div class="price">₹{{price}}</div>
<div class="emi">EMI {{emi}}</div>
<div class="btn" onclick="openForm('{{name}}')">Buy Now</div>
</div>
{% endfor %}
</div>

<div id="formSection">
<div class="form-box">
<span class="close" onclick="closeForm()">X</span>
<h3 id="selectedPhone" style="margin:0 0 10px;">Order Form</h3>
<input type="hidden" id="phone_model">
<input id="name" placeholder="Pura Naam*">
<input id="mobile" placeholder="Apna Mobile Number*">
<input id="city" placeholder="City / Jila*">
<button onclick="submitForm()">WhatsApp Par Bhejo - FAST</button>
<div id="msg" style="text-align:center; margin-top:10px; font-weight:bold; color:green;"></div>
</div>
</div>

<script>
function openForm(phone){
 document.getElementById('phone_model').value = phone;
 document.getElementById('selectedPhone').innerText = phone + ' - Order';
 document.getElementById('formSection').style.display = 'block';
}
function closeForm(){ document.getElementById('formSection').style.display = 'none'; }

function submitForm(){
 let name=document.getElementById('name').value;
 let mobile=document.getElementById('mobile').value;
 let city=document.getElementById('city').value;
 let model=document.getElementById('phone_model').value;
 if(!name || !mobile || !city){alert('Form bharo'); return;}

 // WhatsApp Message
 let message = `*New Bikeebo Order*%0A%0APhone: ${model}%0AName: ${name}%0AMobile: ${mobile}%0ACity: ${city}%0A%0AJaldi Call Karo!`;
 let waNumber = "{{wa_number}}";
 let waLink = `https://wa.me/${waNumber}?text=${message}`;
 
 // Pehle customer ka WhatsApp kholo, fir tumhare paas bhi lead ayega
 window.open(waLink, '_blank');
 
 document.getElementById('msg').innerText='✓ WhatsApp Khul Raha Hai...';
 setTimeout(()=>{ closeForm(); }, 1500);
}
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML, phones=PHONES, wa_number=WHATSAPP_NUMBER)

if __name__ == '__main__':
    app.run()
