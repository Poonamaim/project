from flask import Flask, jsonify, request

pooja = Flask(__name__)  # This creates the Flask app instance

# Sample data (list of users)
users = [
    {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
    {'id': 2, 'name': 'Jane Doe', 'email': 'jane@example.com'}
]

# Route to get all users
@pooja.route('/api/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Route to get a single user by ID
@pooja.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

# Route to create a new user
@pooja.route('/api/users', methods=['POST'])
def create_user():
    new_user = request.get_json()
    new_user['id'] = len(users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

# Route to update an existing user
@pooja.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    updated_data = request.get_json()
    user.update(updated_data)
    return jsonify(user)

# Route to delete a user
@pooja.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return jsonify({'message': 'User deleted'}), 200

if __name__ == '__main__':
    pooja.run(debug=True)  # Start the Flask application
    