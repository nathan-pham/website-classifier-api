from flask import Flask, Response, request
from server_utils import spec, response
from model_utils import predict

app = Flask(__name__)


@app.route("/")
def home():
    return Response(response=spec, status=200, mimetype="text/plain")


@app.route("/api/predict", methods=["GET"])
def get_predict():
    content = request.args.get("content")
    return response(True, "Successfully predicted content", predict(content))


@app.route("/api/predict", methods=["POST"])
def post_predict():
    content = request.get_json()["content"]
    return response(True, "Successfully predicted content", predict(content))


app.run("0.0.0.0", port="5500")
