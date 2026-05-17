import time
import random
import uuid

from services.storage import messages

def process_sms(data):

    # LATENCY
    latency = random.randint(5, 50)

    time.sleep(latency / 1000)

    # STATUS
    status = random.choices(
        ["DELIVERED", "FAILED", "PENDING"],
        weights=[85, 10, 5]
    )[0]

    # SMS OBJECT
    sms = {

        "id": str(uuid.uuid4()),

        "to": data.get("to"),

        "message": data.get("message"),

        "campaignId": data.get("campaignId"),

        "priority": data.get("priority"),

        "status": status,

        "latency": latency,

        "createdAt": time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    # STORE
    messages.insert(0, sms)

    # LIMIT MEMORY
    if len(messages) > 100000:

        messages.pop()