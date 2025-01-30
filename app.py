import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

marks = pd.read_json("marks.json")

@app.route("/")
def home():
    return "Server is running!"

@app.route('/api', methods=["GET"])
def apiAccess():
    names = request.args.getlist('name')
    results = marks.set_index('name').loc[names]
    response_data = {"marks": results['marks'].tolist()}
    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)
