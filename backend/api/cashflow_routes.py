from flask import Blueprint, jsonify

from services.cashflow_service import get_cashflow_forecast


cashflow_bp = Blueprint("cashflow", __name__)


@cashflow_bp.get("/forecast")
def forecast():
    result = get_cashflow_forecast()

    return jsonify(result)