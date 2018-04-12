from flask import Flask
from flask import jsonify
from sensors.Temperature import Temperature

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/temperature")
def get_temperature():
    t = Temperature()
    return jsonify(t.read())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)