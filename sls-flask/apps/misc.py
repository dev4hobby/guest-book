from settings import WOKEUP_TIME
from utils.timer import calc_uptime
from flask import Blueprint, jsonify, make_response

misc = Blueprint("misc", __name__, url_prefix="/misc")


@misc.route("/uptime", methods=["GET"])
def get_uptime():
    return make_response(jsonify(uptime=calc_uptime(WOKEUP_TIME)), 200)
