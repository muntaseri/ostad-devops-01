from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({ "status": "success", "message": "Hello from local application exposed via ngrok" })

if __name__ == "__main__":
    app.run(debug=True)