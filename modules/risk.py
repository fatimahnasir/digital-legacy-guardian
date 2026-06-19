def calculate_risk(text):

    risk = 0

    text = text.lower()

    if "bank" in text:
        risk += 30

    if "crypto" in text:
        risk += 30

    if "wallet" in text:
        risk += 20

    if "password" in text:
        risk += 20

    if "passport" in text:
        risk += 15

    return min(risk, 100)


def risk_level(score):

    if score >= 70:
        return "High"

    elif score >= 40:
        return "Medium"

    return "Low"