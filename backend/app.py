# backend/app.py — Week 1 version
from flask import Flask, jsonify, request
from flask_cors import CORS
import logging
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)


try:
    model = pickle.load(open('numa_model.pk1', 'rb'))
    logging.info("✅ Numa's brain loaded")
except FileNotFoundError:
    model = None
    logging.warning("⚠️ Model not found yet — run train_model.py")

# ─────────────────────────────────
# /ping — health check
# ─────────────────────────────────
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'message':      'Numa is awake 🌙',
        'model_loaded': model is not None,
        'status':       'ok'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)