def compute_risk(event):
    score = 0

    severity = event.get("severity", "low").lower()
    industry = event.get("industry", "").lower()

    if severity == "high":
        score += 70
    elif severity == "medium":
        score += 40
    else:
        score += 10

    if "logistics" in industry:
        score += 20
    elif "manufacturing" in industry:
        score += 15
    elif "energy" in industry:
        score += 25

    return min(score, 100)