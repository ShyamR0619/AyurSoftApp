# AyurSoftApp: Ayurvedic Drug & Formulation Recommender System

[![Publication](https://img.shields.io/badge/Journal-IJSREM-blue.svg)](https://ijsrem.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An AI-driven software recommendation engine designed to bridge traditional Ayurvedic medicine with modern technological advancements. Built with Python and Flask, **AyurSoftApp** utilizes Natural Language Processing (NLP) and Machine Learning (Multinomial Naive Bayes) to interpret natural-language symptom descriptions, predict Ayurvedic symptom categories, recommend suitable herbal formulations, and locate nearby certified Ayurvedic practitioners.

> **Published Work:** Published in the *International Journal of Scientific Research in Engineering & Management (IJSREM)*, Vol. 09, Issue 05, May 2025 (DOI: 10.55041/IJSREM47138). Full certificates and project report documentation are located in the [`/docs`](./docs) directory.

---

## 📌 Executive Summary

Ayurvedic texts like *Charaka Samhita* and *Sushruta Samhita* contain vast and complex formulation details, making manual cross-referencing time-consuming for practitioners and students. **AyurSoftApp** addresses this challenge by:
1. **Symptom Interpretation:** Processing free-form, plain-language symptom descriptions using TF-IDF vectorization.
2. **Formulation Retrieval:** Querying structured datasets to recommend classical Ayurvedic formulations with relevant indications and usage guidelines.
3. **Safety & Contraindication Alerts:** Flagging contraindications (e.g., avoiding fermented or jaggery-based preparations for diabetic patients).
4. **Practitioner Integration:** Providing nearby certified Ayurvedic doctor recommendations to encourage professional consultation.

---

## 🛠 Tech Stack

- **Backend:** Python 3, Flask, Flask-CORS
- **Machine Learning & NLP:** Scikit-Learn (Multinomial Naive Bayes, TF-IDF Vectorizer), Pandas, Joblib
- **Frontend:** HTML5, CSS3, Jinja2 Templates, Bootstrap 5, FontAwesome
- **Datasets:** Custom CSV datasets (`Ayurvedic_Symptoms_Desc.csv` and `Formulation-Indications.csv`)

---

## 📊 Key Results & Metrics

- **Retrieval Speed:** Reduced formulation retrieval time from **30–60 minutes** (manual text lookup) to **2–5 seconds**.
- **Model Accuracy:** **85–90% accuracy** in identifying clinically relevant formulations as validated by Ayurvedic practitioners.
- **Safety Impact:** Achieved a **70% reduction** in potential contraindication risks during clinical evaluation.
- **User Satisfaction:** **85%** positive user rating across usability and workflow efficiency tests.

---

## 📁 Project Structure

```text
├── docs/
│   ├── Project_Report.pdf
│   └── IJSREM_Publication_Certificates.pdf
├── static/
│   ├── css/
│   └── images/
├── templates/
│   └── index.html
├── Ayurvedic_Symptoms_Desc.csv
├── Formulation-Indications.csv
├── app.py
├── README.md
└── requirements.txt

git clone [https://github.com/ShyamR0619/ayursoftapp.git](https://github.com/ShyamR0619/ayursoftapp.git)
cd ayursoftapp

pip install -r requirements.txt
python app.py


👥 Project Team
Harika Y (20211COM0001)
Shyam R (20211COM0018)
Samuel R (20211COM0037)
Praveen Kumar G S (20211COM0038)
Guided by: Dr. Sukruth Gowda M A, Department of Computer Engineering, Presidency University, Bengaluru.
