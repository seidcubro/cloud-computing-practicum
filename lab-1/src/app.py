from flask import Flask, request, jsonify

app = Flask(__name__)

@app.before_request
def log_request():
    print(f"[REQUEST] {request.remote_addr} {request.method} {request.path}")

@app.route("/health", methods=["GET"])
def health():
    return jsonify(status="ok"), 200

@app.route("/", methods=["GET"])
def root():
    return jsonify(service="cs361-hello-service", version="1.0.0"), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
