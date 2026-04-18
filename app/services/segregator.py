from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="sk-your-key"
)

def classify_pages(pages):
    result = {
        "identity_document": [],
        "itemized_bill": [],
        "discharge_summary": [],
        "other": []
    }

    for page in pages:

        # ✅ FIX 1: Handle empty text
        text = page['text'] if page['text'] else "No content"

        prompt = f"""
        You are a medical document classifier.

        Classify this page into ONE of:
        identity_document, itemized_bill, discharge_summary, other

        Page Content:
        {text}

        Return ONLY the category name.
        """

        # ✅ FIX 2: TRY-CATCH HERE
        try:
            response = llm.invoke(prompt).content.strip().lower()
        except Exception as e:
            print("Error:", e)
            response = "other"

        if response in result:
            result[response].append(page)
        else:
            result["other"].append(page)

    return result