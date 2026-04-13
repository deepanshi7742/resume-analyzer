# 🚀 AI Resume Analyzer

## 📌 Overview

AI Resume Analyzer is a web-based application that evaluates a resume against a job description using Natural Language Processing (NLP). It calculates a match score and identifies missing skills to help improve job applications.

---

## ✨ Features

* 📄 Upload Resume (PDF)
* 📝 Enter Job Description
* 📊 Match Score Calculation (%)
* 🔍 Missing Skills Detection
* 📈 Visual Graph Representation

---

## 🛠️ Tech Stack

* Python
* Flask
* Scikit-learn
* SpaCy
* PyPDF2
* HTML, CSS
* Chart.js

---

## ⚙️ How It Works

1. Extracts text from the uploaded resume
2. Cleans and processes text using NLP
3. Converts text into numerical form using TF-IDF
4. Calculates similarity score using cosine similarity
5. Identifies missing skills by comparing job description with resume

---

## 📂 Project Structure

```
resume-analyzer/
│── app.py
│── resume_model.py
│── requirements.txt
│
├── templates/
│     └── index.html
│
├── static/
│     └── style.css
```

---

## ▶️ Installation & Run

### Step 1: Clone the repository

```
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
```

### Step 2: Install dependencies

```
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### Step 3: Run the app

```
python app.py
```

### Step 4: Open in browser

```
http://127.0.0.1:5000/
```

---

## 📊 Output Example

* Match Score: 78%
* Missing Skills: SQL, Machine Learning

---

## 🎯 Future Improvements

* 🤖 AI-based resume suggestions
* 📑 Support for multiple file formats
* 🌐 Deployment on cloud

---

## 👩‍💻 Author

**Deepanshi Sharma**

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
