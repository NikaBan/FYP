from flask import (Flask, render_template, jsonify, request)

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('homepage.html')

@app.route("/send", methods=["POST"])
def send():
    username = request.json.get("username")
    return jsonify(username)

if __name__ == "__main__":
    app.run(debug = True)