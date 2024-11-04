from flask import Flask, request

# Can you write a simple flask api in Python which 
# Use a port other than 5000
# 2. When called with no parameter just return "Helllo"
# 3. When called with one parameter name and then returns Greetings with the name.
# 4. Give examples of how to call

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name')
    if name:
        return f'Greetings, {name}!'
    else:
        return 'Greetings'

if __name__ == '__main__':
    app.run(port=8080)

# Examples of how to call:
# 1. Without parameter: http://127.0.0.1:8080/
# 2. With parameter: http://127.0.0.1:8080/?name=John