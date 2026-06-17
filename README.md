# 🛒 E-Commerce Customer Churn Prediction System

An intelligent Machine Learning web application that predicts whether an e-commerce customer is likely to stay with the platform or churn (leave). The system helps businesses identify at-risk customers and take proactive actions to improve customer retention.

## 🌐 Live Demo

🔗 https://e-commerce-customer-churn-prediction-cf5a.onrender.com/

---

## 📌 Project Overview

Customer churn is one of the biggest challenges faced by e-commerce businesses. Losing existing customers can significantly impact revenue and growth.

This project uses a Machine Learning model (Gaussian Naive Bayes) to analyze customer behavior and predict whether a customer is likely to churn based on demographics, purchasing history, subscription type, and support interactions.

---

## 🎯 Project Objective

The primary goal of this project is to:

- Identify customers at risk of leaving
- Improve customer retention strategies
- Reduce revenue loss
- Support data-driven business decisions
- Enhance customer engagement and satisfaction

---

## ✨ Features

- Predict customer churn in real time
- Modern and responsive user interface
- Easy-to-use web application
- Machine Learning-powered predictions
- Business-focused insights
- Render cloud deployment

---

## 📊 Input Features

The model uses the following customer attributes:

- Age
- Gender
- City
- Tenure Months
- Average Order Value
- Total Orders
- Last Purchase Days Ago
- Support Tickets
- Subscription Type

---

## 🤖 Prediction Output

### Customer Will Stay
The customer is likely to continue using the platform.

### Customer Will Churn
The customer is likely to leave the platform and may require retention efforts.

---

## 🛠️ Technologies Used

- Python
- Flask
- Scikit-Learn
- Pandas
- NumPy
- HTML
- CSS
- Gunicorn
- Render

---

## 🧠 Machine Learning Model

### Algorithm Used
Gaussian Naive Bayes

### Problem Type
Classification

### Target Variable
Customer Churn

---

## 📂 Project Structure

```text
E-Commerce-Customer-Churn-Prediction/
│
├── app.py
├── naive_model.pkl
├── requirements.txt
├── README.md
│
└── templates/
