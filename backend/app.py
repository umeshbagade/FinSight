from flask import Flask

from api.health_routes import health_bp
from api.cashflow_routes import cashflow_bp
from api.advisor_routes import advisor_bp


def create_app():
    app = Flask(__name__)

    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(cashflow_bp, url_prefix="/api/cashflow")
    app.register_blueprint(advisor_bp, url_prefix="/api/advisor")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=5000)