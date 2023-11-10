from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/data", methods=["post"])
def data():
    content =  json.loads(request.get_data())
    print(content)

    return {"res": "Success"}

app.run(debug=True)