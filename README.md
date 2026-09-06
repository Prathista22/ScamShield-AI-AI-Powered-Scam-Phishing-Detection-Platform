# ScamShield-AI-AI-Powered-Scam-Phishing-Detection-Platform
An AI-based system for detecting and preventing online scams.

## 📌 Project Overview

ScamShield AI is an AI-powered web-based risk-assessment platform designed to help users identify potentially harmful scam and phishing content. The system analyzes different types of suspicious digital content, including text messages, URLs, screenshots, and QR codes, and provides users with an understandable risk assessment.

The platform combines Natural Language Processing (NLP), machine learning, URL analysis, Optical Character Recognition (OCR), and QR code decoding to detect potential threats. Instead of providing only a simple "scam" or "not scam" result, ScamShield AI aims to provide a risk score, predicted scam category, identified risk factors, explanation, and recommendation.

---

## 🎯 Problem Statement

Online scams and phishing attacks have become increasingly common through SMS, WhatsApp, email, suspicious websites, screenshots, and QR codes. Many users, especially those without technical knowledge, find it difficult to determine whether a message or link is genuine before clicking on it or sharing personal information.

Existing spam filters often provide only a simple spam or not-spam result and may not explain the reasons behind the warning. ScamShield AI addresses this problem by providing a user-friendly platform that analyzes suspicious content and presents a clear risk assessment with understandable explanations.

---

## 🎯 Objectives

1. To detect scam and phishing intent in text messages using Natural Language Processing and machine-learning techniques.
2. To evaluate the risk level of suspicious URLs using structural and lexical characteristics.
3. To analyze screenshots and QR codes by extracting text or embedded URLs and processing them through the appropriate analysis modules.
4. To provide users with a risk score, predicted scam category, explanation, recommendation, and scan history.

---

## 🔬 Methodology

ScamShield AI follows a modular web-based architecture.

### 1. User Input

The React frontend allows users to submit:

* Text messages
* URLs
* Screenshots
* QR code images

### 2. Backend Processing

The submitted request is sent to the FastAPI backend. The backend identifies the input type and routes it to the appropriate analysis module.

### 3. Text Analysis

For text-based scam detection, the system performs:

* Lowercase conversion
* Removal of unnecessary characters
* Tokenization
* Stop-word removal
* TF-IDF vectorization
* Machine-learning classification

Logistic Regression is used as the baseline machine-learning model. Naive Bayes and Linear SVM may also be compared during performance evaluation.

### 4. URL Analysis

Suspicious URLs are evaluated using structural and lexical characteristics such as:

* URL length
* HTTPS usage
* Number of subdomains
* IP-based hosts
* URL shorteners
* `@` symbols
* Punycode

These characteristics are used to identify potentially suspicious URLs.

### 5. Screenshot Analysis

OCR technology is used to extract text from uploaded screenshots. The extracted content is then passed to the appropriate analysis module for further processing.

### 6. QR Code Analysis

The QR decoder extracts embedded information, particularly URLs, from QR code images. Extracted URLs are then analyzed using the URL risk-analysis module.

### 7. Risk Assessment

The available analysis results are combined to generate:

* Risk score
* Risk level
* Predicted scam category
* Identified risk factors
* Explanation
* Recommendation

### 8. Database Storage

MySQL is used to store relevant information such as scan history, categories, risk scores, and timestamps. This information can be used to display dashboard analytics.

---

## 🛠️ Technologies Used

### Frontend

* React
* JavaScript
* HTML
* CSS

### Backend

* Python
* FastAPI

### Machine Learning & NLP

* Natural Language Processing
* TF-IDF Vectorization
* Logistic Regression
* Naive Bayes
* Linear SVM

### Image & QR Processing

* Tesseract or EasyOCR
* QR Code Decoding Library

### Database

* MySQL

### Development & Testing

* Git
* GitHub
* pytest
* API Testing

---

## ⭐ Key Features

* 🔍 Scam and phishing text detection
* 🔗 Suspicious URL risk analysis
* 📷 Screenshot analysis using OCR
* 📱 QR code analysis
* 📊 Risk score generation
* ⚠️ Risk-level classification
* 🏷️ Scam category prediction
* 💡 Explainable risk factors
* 🛡️ User recommendations
* 📜 Scan history
* 📈 Dashboard analytics

---

## 🏗️ Proposed Project Structure

```text
ScamShield-AI/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   └── main.py
│
├── ml/
│   ├── datasets/
│   ├── preprocessing/
│   ├── models/
│   └── training/
│
├── ocr/
│
├── qr_analysis/
│
├── database/
│
├── tests/
│
├── screenshots/
│
├── requirements.txt
│
└── README.md
```

> The project structure will be updated as development progresses.

---

## 🧪 Testing & Performance Evaluation

The machine-learning dataset will be divided into training, validation, and testing sets using a **70:15:15 ratio**, with stratification by category.

The machine-learning models will be evaluated using:

* Accuracy
* Precision
* Recall
* Macro F1-score
* Confusion Matrix
* Per-category performance

The application will also undergo:

### Unit Testing

Testing individual components such as preprocessing and feature extraction.

### API Testing

Testing FastAPI backend endpoints to ensure correct request processing and responses.

### Integration Testing

Testing complete workflows such as:

```text
Screenshot Upload
       ↓
OCR Extraction
       ↓
Text Processing
       ↓
Classification
       ↓
Risk Assessment
       ↓
Database Storage
       ↓
Result Display
```

These tests will help evaluate both prediction quality and overall system reliability.

---

## 📊 Expected Outcomes

The expected outcome is a functional web application capable of analyzing suspicious messages, URLs, screenshots, and QR codes.

The system is expected to provide:

* Risk score
* Predicted scam category
* Risk level
* Identified risk factors
* Explanation
* Recommendation
* Scan history
* Dashboard analytics

The dashboard will provide basic analytics such as:

* Total number of scans
* Scam category distribution
* Risk trends

The project is intended to act as a practical risk-assessment tool that helps users make informed decisions before interacting with potentially harmful digital content.

---

## 🚧 Current Project Status

**Status:** Under Development

The initial project repository contains the project documentation and structure. Source code, machine-learning models, database components, testing modules, and other features will be added and updated regularly throughout the development process.

---

## 🔮 Future Enhancements

Future versions of ScamShield AI may include:

* Multilingual scam detection
* Browser extension integration
* Live threat-intelligence services
* Real-time URL reputation checking
* Advanced deep-learning models
* Mobile application
* Improved explainable AI features
* Automated threat database updates

---

## 📚 Project Scope

The initial scope of the project is an English-language prototype capable of analyzing text, URLs, screenshots, and QR codes.

The system focuses on providing understandable risk assessments rather than replacing professional cybersecurity or threat-intelligence services.

---

## 👥 Team Members

| Name          | Role        |
| ------------- | ----------- |
| Prathista    | Team Member |
| Jayavardini | Team Member |
| Sushmitha | Team Member |
| Ayesha | Team Member |

---

## 🎓 Academic Project

**Course:** BCA Mini Project (CSA7200)
**University:** Presidency University
**Program:** Bachelor of Computer Applications (BCA) – Data Science

---

## 📌 Disclaimer

ScamShield AI is an academic project developed for educational and research purposes. The risk assessment provided by the system should be considered an aid for identifying potentially suspicious content and should not be treated as a guarantee that a message, URL, screenshot, or QR code is safe or malicious.
