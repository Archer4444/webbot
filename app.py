from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "7034f23db727899a8a392180dba485526b442c2c957c0dbd701c938eccfc910e"
API_URL = "https://api.together.ai/v1/chat/completions"
MODEL = "Qwen/Qwen2.5-72B-Instruct-Turbo"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json.get('message')
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": user_message}]
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.ok:
        bot_reply = response.json().get("choices")[0]["message"]["content"]
        return jsonify({"reply": bot_reply})
    else:
        return jsonify({"reply": "Ошибка получения ответа."})

if __name__ == "__main__":
    app.run(debug=True)
