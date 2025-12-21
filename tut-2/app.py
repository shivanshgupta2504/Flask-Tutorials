from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/hello')
def hello():
    return '<h1>New Route</h1>'

@app.route("/greet/<name>") # parameter
def greet(name):
    return f"<h1>Hello, {name}!</h1>"

@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return f"{num1} + {num2} = {num1 + num2}"

@app.route("/handle_url_params") # /handle_url_params?name=Mike&age=23
# Two parameters - name and age
def handle_params():
    name = request.args.get("name", "")
    age = int(request.args.get("age", -1))
    return f"{name} is {age} years old"

@app.route("/handle_request", methods=["GET", "POST"])
def handle_request():
    if request.method == "GET":
        return "<h1>You made a GET Request</h1>"
    elif request.method == "POST":
        return "<h1>You made a POST Request</h1>"
    else:
        return "<h1>You will never see this message</h1>"

@app.route('/status_code')
def status_code():
    return '<h1>Hello World!</h1>', 202

@app.route('/custom_header')
def custom_header():
    response = make_response("<h1>Hello World!</h1>")
    response.status_code = 202
    response.headers['content-type'] = 'application/octet-stream'
    return response

# curl commands
# curl -X POST http://127.0.0.1:8080/handle_request - To send a request to particular url endpoint
# curl -I -X POST http://127.0.0.1:8080/handle_request - Gives headers also

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)