from flask import Blueprint, jsonify

hello_blueprint = Blueprint('hello', __name__)

@hello_blueprint.route("/api/hello")
def hello():
    return jsonify({"message": "Hello depuis Flask!"})
