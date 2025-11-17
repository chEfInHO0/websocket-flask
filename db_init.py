from extensions import db
from app import create_app
from models.payment import Payment

app = create_app()

with app.app_context():
    db.create_all()
    db.session.commit()
