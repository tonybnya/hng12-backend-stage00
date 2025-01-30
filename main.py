import os
from flask import Flask, jsonify
from flask_cors import CORS
from utils import get_current_iso_datetime

# create the Flask application
app = Flask(__name__)
# enable CORS for all routes
CORS(app)


# define the root endpoint
@app.route("/")
def home():
    infos = {
        "email": "tonybnya@gmail.com",
        "current_datetime": get_current_iso_datetime(),
        "github_url": "https://github.com/tonybnya/hng12-backend-stage00",
    }
    return jsonify(infos), 200


# run the Flask application
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
