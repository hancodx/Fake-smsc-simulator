import random


def generate_status():

    rand = random.randint(1, 100)

    if rand <= 70:
        return "DELIVERED"

    elif rand <= 90:
        return "PENDING"

    return "FAILED"


def generate_latency():
    return random.randint(100, 3000)