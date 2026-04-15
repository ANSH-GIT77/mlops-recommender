# 🎬 AI Recommendation System with MLOps Pipeline

## 🚀 Overview
This project is an AI-based Hybrid Recommendation System designed to provide personalized suggestions using user behavior and item features. It integrates a complete MLOps pipeline including model building, deployment, monitoring, and retraining.

---

## 🎯 Problem Statement
Modern platforms like Netflix, Amazon, and Spotify have massive content, making it difficult for users to find relevant items. Traditional systems suffer from low accuracy and cold-start problems.

---

## 💡 Solution
We developed a **Hybrid Recommendation System** combining:
- Collaborative Filtering (User-User)
- Content-Based Filtering

This improves accuracy and handles cold-start issues effectively.

---

## ⚙️ System Architecture

1. Data Collection (User ratings, movie data)
2. Data Preprocessing
3. Model Training (Hybrid Model)
4. ONNX Model Conversion
5. API Deployment using FastAPI
6. Docker Containerization
7. Monitoring & Logging
8. Automated Retraining

---

## 🧠 Technologies Used

- Python
- FastAPI
- Pandas, NumPy, Scikit-learn
- Docker
- ONNX
- Uvicorn

---

## 🔥 Features

- ✅ Hybrid Recommendation Model
- ✅ Real-time API-based recommendations
- ✅ Interactive Dashboard UI
- ✅ Logging & Monitoring System
- ✅ Automated Model Retraining
- ✅ Docker-based Deployment
- ✅ ONNX Model Conversion (Cross-platform)

---

## 🖥️ Project Structure
mlops-recommender/
│
├── api/ # FastAPI backend
├── src/ # ML model & logic
├── data/ # Dataset
├── logs/ # Log files
├── models/ # ONNX model
├── index.html # Frontend UI
├── Dockerfile # Container setup
├── .gitignore
└── README.md

