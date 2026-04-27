import json
import re
from llm import llm

def suggest_actions_llm(event, risk):
    prompt = f"""
    You are an API that returns JSON only.

    No explanation. No extra text.

    Event: {event}
    Risk Score: {risk}

    Output:
    {{
        "actions": ["", "", ""]
    }}
    """

    try:
        response = llm.invoke(prompt)
        content = response.content.strip()

        matches = re.findall(r"\{.*?\}", content, re.DOTALL)

        for m in matches:
            try:
                data = json.loads(m)
                return {"actions": data.get("actions", [])[:3]}
            except:
                continue

        raise ValueError("No valid JSON")

    except Exception as e:
        print("ERROR:", e)
        return {
            "actions": [
                "Monitor situation",
                "Increase inventory",
                "Diversify suppliers"
            ]
        }