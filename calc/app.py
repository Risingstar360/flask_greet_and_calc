from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route("/add")
def add_num():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    ans = add(a,b)
    return str(ans)

@app.route("/sub")
def sub_num():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    ans = sub(a,b)
    return str(ans)

@app.route("/mult")
def mult_num():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    ans = mult(a,b)
    return str(ans)

@app.route("/div")
def div_num():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    ans = div(a,b)
    return str(ans)
