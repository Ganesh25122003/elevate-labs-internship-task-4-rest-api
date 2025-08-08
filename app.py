from flask import Flask, request, jsonify

app = Flask(__name__)
users = {}

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@app.route("/users", methods=["POST"])
def add_user():
    data = request.json
    user_id = data["id"]
    name = data["name"]
    users[user_id] = {"id": user_id, "name": name}
    return jsonify({"message": "User added successfully."})

@app.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    users[user_id]["name"] = data["name"]
    return jsonify({"message": "User updated successfully."})

@app.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404
    del users[user_id]
    return jsonify({"message": "User deleted successfully."})

if __name__ == "__main__":
    app.run(debug=True)