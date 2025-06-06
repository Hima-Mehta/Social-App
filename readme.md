# Social Support AI Workflow Automation

This project implements a fully automated AI pipeline for evaluating social support applications. It ingests multimodal applicant data, validates it, assesses eligibility using a machine learning model, and recommends upskilling or financial support options. It also has GenAI backed chatbot.

---

## 🚀 Features

* Document ingestion from PDFs, images, Excel
* OCR and form field parsing
* Data validation and consistency checks
* Eligibility prediction via scikit-learn model
* Decision and recommendation agenta
* Conversational chatbot (Streamlit)
* Local LLM integration via Ollama

---

## 🛠️ Tech Stack

| Layer         | Tools                                     |
| ------------- | ----------------------------------------- |
| Programming   | Python 3.10                               |
| ML/Modeling   | scikit-learn, joblib                      |
| Data          | pandas, openpyxl, pdfplumber, pytesseract |
| Frontend      | Streamlit                                                          |
| LLM/GenAI     | Ollama                                    |

---

## 📂 Project Structure

```
social_support_ai/
├── ui/                     # Streamlit chatbot
├── pipelines/              # Ingestion, validation, features, decision
├── training/               # Model training script
├── models/                 # Saved eligibility model
├── data/                   # Sample input files
├── README.md
├── environment.yml         # Conda environment definition
└── SocialSupportApp.docx # Design and architecture
```

---

## 🧪 How to Run

### 1. Set Up Environment

```bash
conda env create -f environment.yml
conda activate social-support-ai
```

### 2. Train ML Model

```bash
python main.py
```

### 3. Launch Chatbot

```bash
streamlit run genai_chatbot.py
```

---

## 📝 API Endpoint

**POST /predict**

* `multipart/form-data`: resume, bank statement, ID, Excel
* Form fields: income, employment, family size, liabilities, etc.
* Returns: eligibility decision, confidence, recommendation

---

## 📈 Future Enhancements

* Auto extract structured data from ID/Excel using NER/LLM
* Feedback loop for retraining
* RAG integration for document-based chat
* Arabic support and OCR enhancement like using AzureAI readApi
* Cloud deployment with Docker
* Agent orchestration with CrewAI or LangGraph

---

## 📄 License

MIT License

---

## 👨‍💻 Author

\[Hima mehta] – \[[hima.p.mehta@gmail.com](mailto:hima.p.mehta@gmail.com)]

