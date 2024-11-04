from flask import Flask, request, jsonify
"""
This Flask application provides several API endpoints:
1. `/multiply` (GET):
    - Multiplies two query parameters 'a' and 'b'.
    - Example: `/multiply?a=3&b=4` returns `{"result": 12}`.
    - Returns a 400 error if the parameters are missing or not integers.
2. `/user/<username>` (GET):
    - Retrieves user information based on the provided username.
    - Example: `/user/john` returns `{"name": "John Doe", "age": 30}`.
    - Returns a 404 error if the user is not found.
3. `/users` (GET):
    - Lists all users.
    - Example: `/users` returns a dictionary of all users.
Error Handlers:
    - 404: Returns a JSON response with `{"error": "Not found"}`.
    - 500: Returns a JSON response with `{"error": "Internal server error"}`.

Example URLs for the API:
- http://127.0.0.1:5000/multiply?a=3&b=4
- http://127.0.0.1:5000/multiply?a=10&b=5
- http://127.0.0.1:5000/multiply?a=7&b=2
- http://127.0.0.1:5000/user/john
- http://127.0.0.1:5000/user/jane
- http://127.0.0.1:5000/user/alice
- http://127.0.0.1:5000/users
        
"""

app = Flask(__name__)

@app.route('/multiply', methods=['GET'])
def multiply():
    try:
        a = request.args.get('a')
        b = request.args.get('b')
        
        if a is None or b is None:
            return jsonify({"error": "Missing query parameters 'a' and 'b'"}), 400
        
        a = int(a)
        b = int(b)
        
        result = a * b
        return jsonify({"result": result})
    
    except ValueError:
        return jsonify({"error": "Query parameters 'a' and 'b' must be integers"}), 400

@app.route('/user/<username>', methods=['GET'])
def get_user(username):
    users = {
        "john": {"name": "John Doe", "age": 30},
        "jane": {"name": "Jane Doe", "age": 25},
        "alice": {"name": "Alice Smith", "age": 28}
    }
    
    user = users.get(username)
    
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['GET'])
def list_users():
    try:
        users = {
            "john": {"name": "John Doe", "age": 30},
            "jane": {"name": "Jane Doe", "age": 25},
            "alice": {"name": "Alice Smith", "age": 28}
        }
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)


