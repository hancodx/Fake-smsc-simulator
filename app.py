from flask import Flask, request, jsonify, render_template
from queue import Queue
from threading import Thread

from services.sms_processor import process_sms
from services.storage import messages

app = Flask(__name__)

# GLOBAL QUEUE
sms_queue = Queue()

# WORKER
def worker():

    while True:

        data = sms_queue.get()

        process_sms(data)

        sms_queue.task_done()

# START WORKERS
for i in range(50):

    t = Thread(
        target=worker,
        daemon=True
    )

    t.start()


@app.route("/")
def index():

    return render_template("index.html")

# SEND SMS
@app.route("/send", methods=["POST"])
def send_sms():

    data = request.json

    sms_queue.put(data)

    return jsonify({
        "success": True,
        "queued": True
    })

#GET MESSAGES
@app.route("/messages")
def get_messages():

    return jsonify(messages)

# STATS
@app.route("/stats")
def stats():

    total = len(messages)

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

    return jsonify({
        "total": total,
        "delivered": delivered,
        "failed": failed,
        "pending": pending
    })

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=9999,
        threaded=True
    )