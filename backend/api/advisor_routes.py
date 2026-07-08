from flask import Blueprint, jsonify, request

from services.advisor_service import get_advisor_response


advisor_bp = Blueprint("advisor", __name__)


@advisor_bp.post("/chat")
def chat():
    payload = request.get_json(silent=True) or {}

    question = payload.get("question")

    if not question:
        return jsonify({
            "error": "question is required"
        }), 400

    response = get_advisor_response(question)

    return jsonify(response)