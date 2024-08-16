import os
from flask import Blueprint

home = Blueprint("home", __name__)

@home.route("/", methods=["GET"])
def index():
    return os.environ.get("ROOT_MSG"), 200