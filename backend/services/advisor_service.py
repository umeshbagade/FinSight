def get_advisor_response(question):
    # Later this service can call an LLM.

    return {
        "question": question,
        "answer": (
            "Your projected cash flow is currently stable. "
            "However, supplier expenses increased compared "
            "with the previous month."
        )
    }