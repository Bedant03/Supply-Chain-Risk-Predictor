# 📦 Supply Chain Risk Predictor

An AI-powered web application that analyzes real-world events and predicts their impact on supply chains using Large Language Models (LLMs) and rule-based risk scoring.

---

## 🌐 Live Demo

👉 https://supply-chain-risk-predictor-01.streamlit.app/

---

## 🚀 Features

* 🔍 **Event Extraction (LLM-based)**
  Converts unstructured news into structured data (event, location, industry, severity)

* ⚠️ **Risk Prediction Engine**
  Calculates risk score based on severity and affected industry

* 🛠️ **Mitigation Suggestions (LLM-based)**
  Generates actionable steps to minimize disruption

* 🎨 **Interactive UI (Streamlit)**
  Simple and responsive interface for real-time analysis

---

## 🧠 Tech Stack

* Python
* Streamlit
* LangChain
* Groq API (LLMs)
* Regex + JSON parsing

---

## 📁 Project Structure

```
supply_chain_app/
│
├── app.py
├── llm.py
├── event_extraction.py
├── risk_predictor.py
├── mitigation.py
├── .env
├── requirements.txt
```

---

## ⚙️ Installation

```bash
git clone : https://github.com/Bedant03/Supply-Chain-Risk-Predictor.git
cd supply-Chain-Risk-Predictor

conda create -p venv python==3.14 -y
conda activate venv

pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push your project to GitHub
2. Go to https://share.streamlit.io
3. Click **New App**
4. Select your repository and set:

   * Main file: `app.py`

### 🔐 Add Secrets

In Streamlit Cloud → Settings → Secrets:

```
GROQ_API_KEY = "your_api_key_here"
```

---

## 🧪 Example Input

```
A major port strike in Los Angeles has halted cargo operations, causing delays in global shipments.
```

---

## 📊 Sample Output

* **Event:** Port Strike
* **Location:** Los Angeles
* **Industry:** Logistics
* **Risk Score:** 90/100 (High Risk)

**Suggested Actions:**

1. Monitor supply chain disruptions
2. Diversify suppliers
3. Prepare for delays

---

## 🔥 Future Improvements

* 📊 Dashboard with charts
* 🌍 Map-based visualization
* 📂 Batch processing (CSV upload)
* 🌐 Real-time news integration

---

## 👨‍💻 Author

Bedant Behera
GitHub: https://github.com/bedant03

---
