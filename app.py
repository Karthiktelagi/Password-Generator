from flask import Flask, render_template, request, jsonify
from passwordgenerator import generate_password

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    length = data.get("length")

    # Validation
    if not length:
        return jsonify({"error": "Password length is required"}), 400

    length = int(length)

    if length < 4 or length > 50:
        return jsonify({"error": "Length must be between 4 and 50"}), 400

    password = generate_password(length)
    return jsonify({"password": password})

if __name__ == "__main__":
    app.run(debug=True)
