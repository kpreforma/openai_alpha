from flask import Flask, render_template, request
from openai_test import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to index page (/) to submit form"
    if request.method == 'POST':
        form_data = request.form
        response = openai_response(form_data["message"] + ". Respond with less than 30 words.", "website")
        response_message_content = response["choices"][0]["message"]["content"]
        return render_template('data.html', output = response_message_content)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)
