from flask import Flask, jsonify
app = Flask(name)
@app.route("/") def home(): return jsonify({ "status": "success", "message": "Hello from local application exposed via ngrok" })
if name == "main": app.run(host="0.0.0.0", port=5000)