
# CRM IMM 2024

## Description
This is a basic CRM system for managing budgets and commercial calls of clients.

## Features
- Manage clients
- Record commercial calls
- Manage budgets
- Multi-company support
- API for external connections

## Installation
1. Clone the repository.
2. Install the necessary dependencies.
3. Run the application.

## Usage
- To add a client: `POST /clients`
- To get all clients: `GET /clients`

# Sample API Code
from flask import Flask, request, jsonify

app = Flask(__name__)

clients = []

@app.route('/clients', methods=['POST'])
def add_client():
    client_data = request.json
    clients.append(client_data)
    return jsonify(client_data), 201

@app.route('/clients', methods=['GET'])
def get_clients():
    return jsonify(clients)

if __name__ == '__main__':
    app.run(debug=True)
