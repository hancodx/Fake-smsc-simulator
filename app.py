from flask import Flask, request, jsonify, render_template
from datetime import datetime
import threading

from services.storage import messages
from services.sms_processor import process_sms

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template("index.html")


# Receive SMS request
@app.route("/send", methods=["POST"])
def send_sms():

    data = request.json

    message = {
        "id": len(messages) + 1,
        "to": data.get("to"),
        "message": data.get("message"),
        "priority": data.get("priority"),
        "campaignId": data.get("campaignId"),
        "status": "PROCESSING",
        "latency": 0,
        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    # Async processing
    threading.Thread(
        target=process_sms,
        args=(message,)
    ).start()

    return jsonify({
        "success": True,
        "message": "SMS received by Fake SMSC"
    })


# Get all messages
@app.route("/messages")
def get_messages():
    return jsonify(messages[::-1])


# Dashboard statistics
@app.route("/stats")
def get_stats():

    delivered = len([
        m for m in messages
        if m["status"] == "DELIVERED"
    ])

    failed = len([
        m for m in messages
        if m["status"] == "FAILED"
    ])

    pending = len([
        m for m in messages
        if m["status"] == "PENDING"
    ])

    stats = {
        "total": len(messages),
        "delivered": delivered,
        "failed": failed,
        "pending": pending
    }

    return jsonify(stats)


if __name__ == "__main__":
    app.run(debug=True)