# 🧾 Claim Processing Pipeline using LangGraph

## 🚀 Project Overview

This project is an AI-powered **Claim Processing Pipeline** built using **FastAPI** and **LangGraph**.
It processes medical claim PDFs by classifying document pages and extracting structured information using multiple AI agents.

The system follows a **multi-agent architecture** where each agent is responsible for a specific task such as classification, identity extraction, billing extraction, and discharge summary extraction.

---

## 🧠 Architecture (LangGraph Workflow)

```
START
  ↓
PDF Loader
  ↓
Segregator Agent (AI)
  ↓
 ┌───────────────┬────────────────────┬─────────────────────┐
 ↓               ↓                    ↓
ID Agent   Discharge Agent   Bill Agent
   ↓               ↓                    ↓
        →→→ Aggregator →→→ END
```

---

## ⚙️ Tech Stack

* **FastAPI** → API framework
* **LangGraph** → Workflow orchestration
* **LangChain + OpenAI** → AI agents
* **pdfplumber** → PDF text extraction
* **Python** → Core language

---

## 📌 Features

* 📄 Upload PDF claims via API
* 🧠 AI-based page classification (Segregator Agent)
* 🤖 Multi-agent extraction system:

  * ID Agent → Extracts patient details
  * Discharge Agent → Extracts medical details
  * Bill Agent → Extracts billing information
* 🔄 LangGraph-based orchestration
* 📊 Structured JSON output

---

## 🔍 How It Works

### 1️⃣ PDF Loader

* Reads uploaded PDF
* Splits into pages
* Extracts text from each page

---

### 2️⃣ Segregator Agent (Core AI)

* Classifies each page into:

  * identity_document
  * itemized_bill
  * discharge_summary
  * other
* Routes pages to relevant agents

---

### 3️⃣ Extraction Agents

#### 🪪 ID Agent

Extracts:

* Patient name
* Date of birth
* Policy number
* ID details

---

#### 🏥 Discharge Summary Agent

Extracts:

* Diagnosis
* Admission date
* Discharge date
* Doctor details

---

#### 💰 Itemized Bill Agent

Extracts:

* Billing items
* Individual costs
* Total amount

---

### 4️⃣ Aggregator

* Combines all extracted data
* Returns final structured JSON

---

## 📡 API Endpoint

### 🔹 POST `/api/process`

#### Request:

* `claim_id` → string
* `file` → PDF file

#### Response:

```json
{
  "claim_id": "123",
  "classification": {
    "identity_document": 2,
    "itemized_bill": 3,
    "discharge_summary": 1,
    "other": 0
  },
  "identity_data": {...},
  "discharge_data": {...},
  "bill_data": {...}
}
```

---

## 🛠️ Setup Instructions

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd claim_processor
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Add OpenAI API Key

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

### 5️⃣ Run Server

```bash
python -m uvicorn app.main:app --reload
```

---

### 6️⃣ Open API Docs

```
http://127.0.0.1:8000/docs
```

---

## 📂 Project Structure

```
claim_processor/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── process.py
│   ├── services/
│   │   ├── pdf_loader.py
│   │   ├── segregator.py
│   │   ├── id_agent.py
│   │   ├── discharge_agent.py
│   │   ├── bill_agent.py
│   ├── graph/
│   │   └── workflow.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🎯 Key Highlights

* Multi-agent AI system
* Clean separation of concerns
* Scalable architecture using LangGraph
* Real-world document processing pipeline

---

## 🚧 Limitations

* Works best on structured medical claim PDFs
* Accuracy depends on LLM responses
* OCR not implemented for scanned PDFs

---

## 🚀 Future Improvements

* Add OCR for scanned documents
* Improve classification accuracy
* Add database storage
* Deploy on cloud (Render/Railway)




