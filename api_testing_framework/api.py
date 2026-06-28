from flask import Flask, jsonify, request

app = Flask(__name__)
# simulated database (in-memory)
users = {}


@app.route('/users', methods=['POST'])
def get_users(user_id):
    user = users.get(user_id)
    if user:
        return jsonify({"id": user_id, "name": user}), 200
    return jsonify({"error": "User not found"}), 404


@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    user_id = data.get('id')
    name = data.get('name')
    if user_id in users:
        return jsonify({"error": "User already exists"}), 400
    users[user_id] = name
    return jsonify({"message": "User added successfully"}), 201