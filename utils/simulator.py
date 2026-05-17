import random


def generate_status():

    rand = random.randint(1, 100)

    # Telecom simulation
    if rand <= 80:
        return "DELIVERED"

    elif rand <= 95:
        return "PENDING"

    return "FAILED"


def generate_latency():

    return random.randint(50, 800)