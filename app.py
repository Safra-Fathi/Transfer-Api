# app.py
from flask import Flask, request, jsonify
from services import TransferService
from models import Transaction

app = Flask(__name__)

# Initialize the TransferService
service = TransferService()

@app.route('/accounts', methods=['POST'])
def create_account():
    data = request.json
    try:
        service.create_account(data['account_number'], data.get('balance', 0.0))
        return jsonify({"message": "Account created successfully"}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/accounts/<account_number>', methods=['GET'])
def get_account(account_number):
    account = service.get_account(account_number)
    if account:
        return jsonify({"account_number": account.account_number, "balance": account.balance})
    return jsonify({"error": "Account not found"}), 404

@app.route('/transfer', methods=['POST'])
def transfer_funds():
    data = request.json
    transaction = Transaction(
        source_account_number=data['source_account_number'],
        destination_account_number=data['destination_account_number'],
        amount=data['amount']
    )
    result = service.transfer(transaction)
    if result == "Transfer successful.":
        return jsonify({"message": result}), 200
    return jsonify({"error": result}), 400

if __name__ == '__main__':
    app.run(debug=True)
