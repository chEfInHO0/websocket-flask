from pydantic import BaseModel, field_validator, Field
from pydantic_core import PydanticCustomError
from datetime import datetime
from models.payment import PaymentStatus


class PaymentCreate(BaseModel):
    payment_date: str = Field(
        default_factory=lambda: datetime.now().date().isoformat())
    payment_type: str
    payment_status: PaymentStatus = PaymentStatus.PROCESSING

    @field_validator('payment_date')
    def validate_date(cls, v):
        try:
            datetime.strptime(v, "%Y-%m-%d")
        except Exception:
            raise PydanticCustomError("Value must be date like", "Data does not match the expected pattern (%Y-%m-%d)", {
                                      "expected": "%Y-%m-%d (2022-10-31)"})
        return v

    @field_validator('payment_status')
    def validate_status(cls, v):
        if type(v) == PaymentStatus:
            return v
        raise ValueError("Value must be 'processing,success or failed'")
