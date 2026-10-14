# weak code
import yaml, base64, pickle
from flask import Flask, request

app = Flask(__name__)

@app.route("/import-settings", methods=["POST"])
def import_settings():
    data = request.get_data()
    cfg = yaml.load(data, Loader=yaml.Loader)
    apply_settings(cfg)
    return "imported"

@app.route("/restore", methods=["POST"])
def restore():
    blob = base64.b64decode(request.form["state"])
    state = pickle.loads(blob)
    return str(state.get("cart", []))


"""
1. Unsafe YAML deserialization
2. Unsafe pickle deserialization
"""
