import json
import re
from llm import llm

def event_extraction_llm(text):
    prompt = f"""
    You are an API that returns JSON only.

    No explanation. No extra text.

    Text: "{text}"

    Output:
    {{
        "event": "",
        "location": "",
        "industry": "",
        "severity": "low/medium/high"
    }}
    """

    try:
        response = llm.invoke(prompt)
        content = response.content.strip()

        matches = re.findall(r"\{.*?\}", content, re.DOTALL)

        for m in matches:
            try:
                return json.loads(m)
            except:
                continue

        raise ValueError("No valid JSON")

    except Exception as e:
        print("ERROR:", e)
        return {
            "event": "unknown",
            "location": "unknown",
            "industry": "general",
            "severity": "low"
        }