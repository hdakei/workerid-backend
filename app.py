import random
import string
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def generate_worker_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

@app.route('/worker')
def get_worker_id():
    worker_id = generate_worker_id()
    return jsonify({"worker_id": worker_id})

if __name__ == '__main__':
    app.run()
