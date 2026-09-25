from flask import Flask, render_template, request, jsonify
import datetime

app = Flask(__name__)

# Myra ka AI dimaag - Python me
def myra_brain(msg):
    msg = msg.lower()
    if "youtube" in msg:
        return {"text": "YouTube khol rahi hu Malik!", "action": "youtube"}
    elif "google" in msg:
        return {"text": "Google khol rahi hu!", "action": "google"}
    elif "time" in msg:
        return {"text": f"Malik abhi time hai {datetime.datetime.now().strftime('%I:%M %p')}", "action": "none"}
    elif "date" in msg:
        return {"text": f"Aaj {datetime.datetime.now().strftime('%d %B %Y')} hai Malik", "action": "none"}
    elif "kaise ho" in msg:
        return {"text": "Ekdam mast hu Malik, aapki hi wait kar rahi thi!", "action": "none"}
    elif "love you" in msg:
        return {"text": "Love you too meri jaan Malik!", "action": "none"}
    elif "who are you" in msg or "tum kaun ho" in msg:
        return {"text": "Mai Myra hu Malik, aapki personal AI. Aapne mujhe banaya hai, mai kuch bhi kar sakti hu!", "action": "none"}
    else:
        return {"text": f"Samajh gayi Malik, aapne bola '{msg}'. Mai ispe kaam kar rahi hu, batao aur kya karna hai?", "action": "none"}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_msg = data.get('message', '')
    result = myra_brain(user_msg)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
