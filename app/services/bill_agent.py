from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-your-key"
)

def extract_bill(pages):
    if not pages:
        return {}

    text = "\n".join([p["text"] or "" for p in pages])

    prompt = f"""
    Extract all billing items and their costs.

    Also calculate total amount.

    Return JSON in format:
    {{
        "items": [
            {{"name": "...", "cost": number}}
        ],
        "total": number
    }}

    Document:
    {text}
    """

    try:
        response = llm.invoke(prompt).content
        return response
    except Exception as e:
        print("Error:", e)
        return {}