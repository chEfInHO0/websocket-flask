from extensions import db
from datetime import datetime
import enum


class PaymentStatus(enum.Enum):
    PROCESSING = "processing"
    SUCCESS = "success"
    FAILED = "failed"


class Payment(db.Model):
    __tablename__ = "payments"

    payment_id = db.Column(db.Integer, primary_key=True)
    payment_date = db.Column(db.String(30), nullable=False,
                             default=lambda: datetime.now().date().isoformat())
    payment_type = db.Column(db.String(80), nullable=False)
    payment_status = db.Column(
        db.Enum(PaymentStatus), nullable=False, default=PaymentStatus.PROCESSING)

    @property
    def id(self):
        return self.payment_id

    def to_dict(self):
        return {
            "payment_id": self.payment_id,
            "payment_date": self.payment_date,
            "payment_type": self.payment_type,
            "payment_status": self.payment_status.value
        }
