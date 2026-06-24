from llm.llama import get_llm
import json


def analyze_news(news, context):

    llm = get_llm()


    prompt = f"""

You are a strict fake news detection AI.

Analyze the news claim using the evidence.

Rules:

- If evidence supports the claim -> REAL
- If evidence contradicts the claim -> FAKE
- If there is insufficient evidence -> FAKE

Do not guess.

News Claim:

{news}


Evidence:

{context}


Return ONLY valid JSON:

{{
    "label": "REAL or FAKE",
    "confidence": number between 0 and 100,
    "explanation": "why the claim is real or fake",
    "key_points": [
        "important point 1",
        "important point 2"
    ]
}}

"""


    response = llm.invoke(prompt)


    try:
        result = json.loads(response.content)
    except:
        result = {
            "label": "UNKNOWN",
            "confidence": 0,
            "explanation": response.content,
            "key_points": []
        }


    return result