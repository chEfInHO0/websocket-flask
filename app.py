from flask import Flask
from routes import routes_bp
from extensions import db
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.config.from_object('config.Config')
    db.init_app(app)

    app.register_blueprint(routes_bp)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=3333)
