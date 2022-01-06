from flask import Flask,jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data":data,
        "message":"SUCCESS"
    }),200

@app.route("/stars")
def stars():
    name = request.args.get("name")
    star_data = next(item for item in data if item["name"] == name)
    return jsonify({
        "data":star_data,
        "message":"SUCCESS"
    }),200

if (__name__ == "__main__"):
    app.run(debug=True)