# 📦 Supply Chain Risk Predictor

An AI-powered web application that analyzes real-world events and predicts their impact on supply chains using LLMs and rule-based risk scoring.

---

## 🚀 Features

* 🔍 **Event Extraction (LLM-based)**
  Extracts structured information (event, location, industry, severity) from unstructured news text.

* ⚠️ **Risk Prediction Engine**
  Computes risk score based on severity and affected industry.

* 🛠️ **Mitigation Suggestions (LLM-based)**
  Generates actionable steps to reduce supply chain disruption.

* 🎨 **Interactive UI (Streamlit)**
  Clean and user-friendly interface for real-time analysis.

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
├── app.py                 # Streamlit UI
├── llm.py                 # LLM configuration
├── event_extraction.py    # Extract event details
├── risk_predictor.py      # Compute risk score
├── mitigation.py          # Suggest mitigation actions
├── .env                   # API keys
├── requirements.txt       # Dependencies
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/supply-chain-risk-predictor.git
cd supply-chain-risk-predictor
```

2. Create environment (recommended):

```bash
conda create -n sc_env python=3.10 -y
conda activate sc_env
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🧪 Example Input

```
A major port strike in Los Angeles has halted cargo operations, causing severe delays in global shipments.
```

---

## 📊 Sample Output

* **Event:** Port Strike
* **Location:** Los Angeles
* **Industry:** Logistics
* **Risk Score:** 90/100 (High Risk)
* **Actions:**

  1. Monitor supply chain disruptions
  2. Diversify suppliers
  3. Prepare for delays

---

## 🔥 Future Improvements

* 📊 Dashboard with charts
* 🌍 Geographical visualization (maps)
* 📂 Batch processing (CSV upload)
* 🌐 Real-time news integration

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/your-username
