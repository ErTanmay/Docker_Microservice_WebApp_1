from flask import Flask, jsonify
import requests

app = Flask(__name__)

BACKEND_URL = "http://host-app:8080/add"  # URL of the backend service

@app.route('/proxyAdd/<int:n1>/<int:n2>', methods=['GET'])
def addition(n1, n2):
    try:
        # Forward the request to the backend service
        response = requests.get(f"{BACKEND_URL}/{n1}/{n2}")

        # Return backend response
        return jsonify(response.json()), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Request failed", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)  # Runs on port 5000
