import requests
from flask import Flask, jsonify, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/flaskdb"
mongo = PyMongo(app)

collection = mongo.db.collection
cursor = list(collection.find({}, {"_id": 0}))

@app.route('/')
def index():
    return "Hello"

@app.route('/json_obj')
def raw_json():
    return jsonify(cursor)

# response = requests.get("http://192.168.111.132:5000/json_obj")
res = requests.get("http://192.168.111.132:5000/json_obj")
print(res.status_code)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
