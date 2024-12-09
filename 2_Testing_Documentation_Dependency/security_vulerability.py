from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

with app.app_context():
  db.create_all()

@app.route('/')
def home():
    return "Welcome to the Security Testing Demo!"

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "username": user.username} for user in users])

@app.route('/user/<int:id>', methods=['GET'])
def get_user(id):
    with db.session() as session:
        user = session.get(User, id)
        if user:
            return jsonify({"id": user.id, "username": user.username})
    return jsonify({"message": "User not found"}), 404

@app.route('/user', methods=['POST'])
def add_user():
    data = request.get_json()
    if 'username' not in data or 'password' not in data:
        return jsonify({"message": "Username and password are required"}), 400
    if not isinstance(data['username'], str) or not isinstance(data['password'], str):
        return jsonify({"message": "Invalid input type"}), 400

    if not data['username'].isalnum() or len(data['username']) < 3 or len(data['username']) > 80:
        return jsonify({"message": "Invalid username"}), 400

    if len(data['password']) < 8 or len(data['password']) > 120:
        return jsonify({"message": "Invalid password"}), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify({"message": "Username already exists"}), 400

    try:
        hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
        new_user = User(username=data['username'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User added successfully"}), 201
    except Exception as e:
        return jsonify({"message": "Error adding user", "error": str(e)}), 500
@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    if 'username' not in data or 'password' not in data:
        return jsonify({"message": "Username and password are required"}), 400

    try:
        user = db.session.get(User, id)
        if not user:
            return jsonify({"message": "User not found"}), 404

        user.username = data['username']
        user.password = generate_password_hash(data['password'], method='pbkdf2:sha256')
        db.session.commit()
        return jsonify({"message": "User updated successfully"})
    except Exception as e:
        return jsonify({"message": "Error updating user", "error": str(e)}), 500

@app.route('/user/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = db.session.get(User, id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": "User deleted successfully"})
        return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"message": "Error deleting user", "error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)





# As a Security Expert can you check this code above check for Security Vulnerabilities like SQL injection, password leakage and all common type of attacks and update the code to make it secure. 

# For the code above can you add examples of the Web URL Lto call the APIs
# Example URLs to call the APIs:

# Get all users
# GET http://localhost:8080/users

# Get a specific user by ID
# GET http://localhost:8080/user/<id>

# Delete a user by ID
# DELETE http://localhost:8080/user/<id>

# Example of calling the API /user with JSON body using curl command:
# Add a new user
# curl -X POST http://localhost:8080/user -H "Content-Type: application/json" -d '{"username": "newuser", "password": "newpassword"}'

# Update an existing user by ID
# curl -X PUT http://localhost:8080/user/<id> -H "Content-Type: application/json" -d '{"username": "updateduser", "password": "updatedpassword"}'

