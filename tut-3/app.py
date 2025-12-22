from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    my_value = "NueralNine"
    my_result = 10 + 20
    my_list = [i for i in range(10, 51, 10)]
    return render_template("index.html", my_value=my_value, my_result=my_result, my_list=my_list)

@app.route("/other") # Whatever maybe the endpoint is, dynamic url looks for the function name
def other():
    some_text = "Hello World"
    return render_template("other.html", some_text=some_text)

@app.route("/redirect_endpoint")
def redirect_endpoint():
    return redirect(url_for("other"))

# Here we add the Custom filters(functions)
@app.template_filter("reverse_string")
def reverse_string(s: str):
    return s[::-1]

@app.template_filter("repeat")
def repeat(s: str, times: int = 2):
    return s * times

@app.template_filter("alternate_case")
def alternate_case(s: str):
    return "".join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
