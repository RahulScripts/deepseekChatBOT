# app.py
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json['message']
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "Expert programming assistant specializing in code debugging"},
                {"role": "user", "content": user_message}
            ],
            temperature=0.3,
            max_tokens=2048
        )
        return jsonify({
            "response": response.choices[0].message.content,
            "status": "success"
        })
    except Exception as e:
        return jsonify({
            "response": f"Error: {str(e)}",
            "status": "error"
        })

if __name__ == '__main__':
    app.run(debug=True)