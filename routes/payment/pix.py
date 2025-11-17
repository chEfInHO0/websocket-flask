from flask import Blueprint, jsonify

pix_bp = Blueprint("pix", __name__, url_prefix="/pix")


@pix_bp.route("/", methods=["GET"])
def get():
    return jsonify({"message": "This is a PIX test"})
