from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "DevOps Practical Challenge",
        "status": "running",
        "message": "Application deployed successfully"
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200
