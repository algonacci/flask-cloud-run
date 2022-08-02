import os
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hello, World!"})

@app.route('/api/psot', methods=['POST'])
def post_something():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        return jsonify(data)
    else:
        return jsonify({"message": "Invalid request."})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
