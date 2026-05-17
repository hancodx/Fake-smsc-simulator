# Fake SMSC Simulator

A lightweight Fake SMSC Simulator built for testing and simulating SMS delivery workflows in distributed messaging systems.

This mini-project simulates a real SMSC Gateway used in telecom environments.  
It receives SMS requests from external services and returns simulated delivery statuses such as:

- SENT
- DELIVERED
- FAILED

The simulator was created for educational and testing purposes as part of a Bulk SMS Platform architecture using Kafka and microservices.

---

## Features

- Receive SMS requests via REST API
- Simulate SMS delivery
- Generate random delivery statuses
- Return fake delivery responses
- Easy integration with Kafka-based systems
- Lightweight and simple architecture

---

## Technologies Used

- Python
- Flask
- REST API
- JSON
- Random Status Simulation

---

## Project Structure

```bash
fake-smsc-simulator/
│
├── services/
├── static/
├── templates/
├── utils/
├── app.py
├── requirements.txt
└── README.md
