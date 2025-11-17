from flask import Blueprint, jsonify
from .pix import pix_bp
from models.payment import Payment
from schemas.payment import PaymentCreate
from pydantic import ValidationError
from extensions import db

pay_bp = Blueprint("pay", __name__, url_prefix="/pay")
pay_bp.register_blueprint(pix_bp)


mock_payment = {
    "payment_type": "subscription",
}


@pay_bp.route("/", methods=["GET"])
def get():
    payments = Payment.query.all()
    return jsonify({"payments": [p.to_dict() for p in payments]})


@pay_bp.route("/", methods=["POST"])
def create_payment():
    try:
        data = PaymentCreate(**mock_payment)
    except ValidationError as e:
        return jsonify({"message": e.errors()})
    print(data)
    payment = Payment(**data.model_dump())
    db.session.add(payment)
    db.session.commit()
    return jsonify({"message": payment.to_dict()})
    # except Exception as e:
    #     return jsonify({"message": f"[{type(e).__name__}, {e.__cause__}]"})
