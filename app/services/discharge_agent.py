from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-your-key"
)

def extract_discharge(pages):
    if not pages:
        return {}

    text = "\n".join([p["text"] or "" for p in pages])

    prompt = f"""
    Extract the following:

    - diagnosis
    - admission_date
    - discharge_date
    - doctor_name

    Return JSON only.

    Document:
    {text}
    """

    try:
        response = llm.invoke(prompt).content
        return response
    except Exception as e:
        print("Error:", e)
        return {}