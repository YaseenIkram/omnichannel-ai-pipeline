import json
import requests
from config import API_URL, MODEL_NAME, GROQ_API_KEY


def extract_structured_data(raw_text: str) -> dict:
    """Sends unstructured corporate communications to Llama 3.

    Forces a strict, normalized extraction format.
    """
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    system_prompt = (
        "You are an elite data intelligence agent. Analyze the unstructured text "
        "and return ONLY a JSON object containing these specific keys:\n"
        "1. 'sender_name' (Full name, default to 'Unknown')\n"
        "2. 'organization' (Company name, default to 'Individual')\n"
        "3. 'contact_channel' (Email, Phone, or WebForm)\n"
        "4. 'intent' (Refund Request, Sales Lead, or Feedback)\n"
        "5. 'financial_value' (Pure integer extraction if money is mentioned, else 0)\n"
        "6. 'priority' (High, Medium, Low based on context and urgency)\n"
        "Do not output any introductory or conversational text. Output raw JSON only."
    )

    payload = {
        "model": MODEL_NAME,
        "response_format": {"type": "json_object"},
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": raw_text}
        ]
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        if response.status_code == 200:
            result = response.json()
            
            # Print metrics to terminal for real-time monitoring
            usage = result.get("usage", {})
            print(f"  [METRICS] Tokens Used -> Prompt: {usage.get('prompt_tokens')} | Completion: {usage.get('completion_tokens')}")
            
            ai_string = result["choices"][0]["message"]["content"]
            return json.loads(ai_string)
        else:
            print(f"  [API ERROR] Server rejected request. Status: {response.status_code}")
            return {}
    except Exception as e:
        print(f"  [SYSTEM EXCEPTION] Failed to process payload: {e}")
        return {}