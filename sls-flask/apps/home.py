from flask import Blueprint, make_response, jsonify

home = Blueprint("home", __name__, url_prefix="/")


@home.route("")
def get_home():
    """
    Home
    """
    return make_response(jsonify(message="Hello from root!"), 200)
