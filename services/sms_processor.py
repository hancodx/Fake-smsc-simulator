import time
from datetime import datetime

from services.storage import messages
from utils.simulator import generate_status, generate_latency


def process_sms(message_data):

    latency = generate_latency()

    # Simulate telecom processing delay
    time.sleep(latency / 1000)

    status = generate_status()

    message_data["status"] = status
    message_data["latency"] = latency
    message_data["processedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    messages.append(message_data)