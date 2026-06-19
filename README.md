# 🔐 AI Digital Legacy Guardian

**An AI-powered Streamlit app that helps you organize, classify, and protect your digital assets — and plan what happens to them after you're gone.**

[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org)
[![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> Most of us leave behind a sprawling digital footprint — bank accounts, crypto wallets, social media, legal documents — with no plan for who should manage it or how secure it actually is. **Digital Legacy Guardian** uses machine learning to classify, risk-score, and protect those assets, and helps you generate a simple digital will so the right people know what to do with them.

---

## ✨ Features

- **📊 Dashboard** — A live overview of all tracked assets: total count, critical assets, protection status, and a category breakdown chart.
- **🤖 AI Asset Analyzer** — Paste in a description of any digital asset and an SVM classifier (trained with TF-IDF text vectorization) automatically categorizes it as *Financial*, *Legal*, *Social*, or *Personal*, with a confidence score and risk rating.
- **⚖️ Priority Engine** — A KMeans clustering model groups assets by urgency, flagging *Critical*, *Important*, and *Normal* priority levels so high-stakes assets never get overlooked.
- **📜 Digital Will Generator** — Generate a simple, downloadable digital will that names a nominee for each asset.
- **🔒 Encryption Center** — Encrypt sensitive notes or credentials on the spot using Fernet (AES-based symmetric encryption), with a generated key you control.
- **📄 Reports** — Export a summary report of your digital estate, ready to download or share.

---

## 🖥️ Demo

🔗 **Live app:** [Add your Streamlit Community Cloud link here]
📷 **Screenshots:**

| Dashboard | Asset Analyzer |
|---|---|
| *Add screenshot here* | *Add screenshot here* |

---

## 🧠 How It Works

| Component | Technique | Purpose |
|---|---|---|
| Asset Classifier | `TfidfVectorizer` + `SVC` (SVM) | Categorizes free-text asset descriptions into Financial / Legal / Social / Personal |
| Priority Engine | `KMeans` clustering | Groups assets into priority tiers based on category and risk |
| Risk Scoring | Rule-based keyword scoring | Flags high-risk terms (bank, crypto, wallet, password, passport) to produce a 0–100 risk score |
| Encryption | `cryptography.fernet` | Encrypts/decrypts sensitive text using AES under the hood |

---

## 🛠️ Tech Stack

- **Frontend / App Framework:** [Streamlit](https://streamlit.io)
- **Data Handling:** Pandas
- **Visualization:** Altair
- **Machine Learning:** scikit-learn (SVM, KMeans, TF-IDF)
- **Security:** `cryptography` (Fernet / AES)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/fatimahnasir/digital-legacy-guardian.git
cd digital-legacy-guardian

# (Recommended) Create a virtual environment
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate   # On Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 📁 Project Structure

```
DigitalLegacyGuardian/
├── app.py                  # Main Streamlit application
├── assets.csv              # Sample asset dataset
├── requirements.txt        # Python dependencies
├── style.css                # Custom UI styling
├── images/
│   └── bg.jpg               # App background image
└── modules/
    ├── classifier.py        # SVM-based asset classifier
    ├── clustering.py        # KMeans priority engine
    ├── risk.py               # Risk scoring logic
    └── encryption.py         # AES (Fernet) encryption utilities
```

---

## 🗺️ Roadmap

- [ ] Persistent database instead of static CSV
- [ ] User authentication and multi-user support
- [ ] Email-based nominee notifications
- [ ] Expanded, larger training dataset for the classifier
- [ ] Dark/light theme toggle

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com/fatimahnasir/digital-legacy-guardian/issues) or open a pull request.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Fatima Nasir**
GitHub: [@fatimahnasir](https://github.com/fatimahnasir)

---

⭐ If you found this project interesting, consider giving it a star on GitHub!
