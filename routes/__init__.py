from flask import Blueprint, jsonify
from .payment import pay_bp


routes_bp = Blueprint("routes", __name__, url_prefix="/")


routes_bp.register_blueprint(pay_bp)


@routes_bp.route("/", methods=["GET"])
def get():
    return jsonify({"message": "This is a test endpoint"})
