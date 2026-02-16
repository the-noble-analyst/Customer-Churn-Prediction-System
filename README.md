# Customer Churn Prediction System

An end-to-end production-ready customer churn analytics and machine learning system that transforms raw CRM and ERP transactional data into actionable churn risk scores using SQL data warehousing, behavioral feature engineering, Random Forest modeling, and real-time deployment with FastAPI, Streamlit, Docker, and AWS EC2.

This project demonstrates the complete ML lifecycle including data engineering, analytics, modeling, and production deployment for proactive customer retention.

---

## 📌 Problem Statement

Customer churn leads to revenue loss and increased acquisition costs. Traditional reporting detects churn after disengagement occurs. The objective of this project is to predict customers at high risk of churn early using historical behavioral data and enable real-time risk assessment for proactive retention.

---

## 🎯 Business Objective

* Predict customers likely to churn using historical transaction and behavior data
* Optimize churn recall to minimize missed at-risk customers
* Generate probability-based churn scores instead of binary predictions
* Deploy real-time inference system for operational use

---

## 🧱 Project Architecture

This project implements a full production ML pipeline:

### SQL Data Warehouse (Medallion Architecture)

* **Bronze Layer**: Raw CRM and ERP data ingestion
* **Silver Layer**: Cleaned and standardized datasets
* **Gold Layer**: Analytics-ready star schema

Tables created:

* fact_sales (60,399 records)
* dim_customers (18,484 records)
* dim_products (295 records)

---

### SQL Exploratory Analysis

* Customer purchase behavior analysis
* Recency and engagement pattern analysis
* Segmentation using joins, CTEs, and window functions
* Feature discovery for churn modeling

---

### Business Intelligence Dashboard (Power BI)

* Customer segmentation dashboard
* Sales and engagement KPIs
* Churn risk indicators
* Executive-level retention insights

---

### Machine Learning Pipeline (Python)

* Behavioral feature engineering
* Churn prediction modeling using Random Forest
* Class imbalance handling using class_weight balancing
* Decision threshold tuning for business optimization

---

### Production Deployment Architecture

The trained model is deployed as a real-time inference system using:

* FastAPI backend REST API
* Streamlit interactive frontend
* Docker containerization for reproducibility
* AWS EC2 cloud deployment for remote access

This converts the model into a usable production system.

---

## 📂 Repository Structure

```
Customer-Churn-Prediction-System/
│
├── Churn_API_Deployment/
│   │
│   ├── app/
│   │   ├── main.py
│   │   ├── best_churn_model.pkl
│   │
│   ├── streamlit/
│   │   ├── streamlit_app.py
│   │
│   ├── docker/
│   │   ├── Dockerfile
│   │   ├── start.sh
│   │
│   ├── deployment/
│   │   ├── aws-ec2.md
│   │   ├── docker.md
│   │
│   ├── requirements.txt
│
├── Data_Warehouse_SQL/
│
├── SQL_Exploratory_Analysis/
│
├── PowerBI_Dashboard/
│
├── Churn_Prediction_ML/
│   ├── Customer_Churn_Analysis_and_Prediction.ipynb
│
├── LICENSE
└── README.md
```

---

## 🛠️ Tools & Technologies

**Programming**  
Python, SQL

**Machine Learning**  
Scikit-learn, Random Forest

**Data Engineering**  
SQL Server, ETL Pipelines, Medallion Architecture, Star Schema

**Backend and Deployment**  
FastAPI, Uvicorn, Docker, AWS EC2

**Frontend**  
Streamlit

**Data Analysis**  
Pandas, NumPy, Matplotlib, Seaborn

**Visualization**  
Power BI

**Version Control**  
Git, GitHub

---

## 🔧 Feature Engineering

Behavioral features engineered from transactional data:

* Recency
* Customer lifespan
* Total orders
* Total quantity
* Total sales
* Average order value
* Average monthly spend

These features capture engagement patterns critical for churn prediction.

---

## 🧠 Churn Definition

A customer is labeled as churned if they made no purchases within a defined future observation window after the prediction cutoff date.

This ensures:

* Realistic churn prediction
* No data leakage
* Production-aligned evaluation

---

## 🤖 Model Training

**Model used**  
Random Forest Classifier

**Configuration**

* n_estimators = 300
* class_weight = balanced

**Reason**

* Handles tabular business data effectively
* Captures non-linear relationships
* Robust to noise and feature interaction

---

## 📊 Model Performance

| Metric               | Score |
| -------------------- | ----- |
| Accuracy             | 83%   |
| Recall (Churn class) | 95%   |

---

## 🎚️ Threshold Optimization

**Default threshold** = 0.50  
**Optimized threshold** = 0.30

**Impact:**

* Increased churn recall from 90% to 95%
* Reduced missed churn customers significantly
* Improved retention decision effectiveness

---

## 📈 Model Interpretability

Feature importance analysis identified key churn drivers:

* Recency
* Customer lifespan
* Monthly spending behavior
* Purchase frequency

Behavioral engagement was more predictive than demographics.

---

## 🚀 Production Deployment

The trained model was deployed as a production inference system:

**Backend**  
FastAPI REST API serving churn prediction

**Frontend**  
Streamlit web interface for real-time prediction

**Containerization**  
Docker container for reproducible deployment

**Cloud Deployment**  
AWS EC2 instance hosting API and frontend

This enables real-time churn prediction via cloud infrastructure.

---

## 💼 Business Impact

This system enables:

* Early detection of at-risk customers
* Probability-based customer risk ranking
* Proactive retention intervention
* Data-driven retention strategy

Transforms static analytics into operational decision system.

---

## 🚀 Key Takeaway

This project demonstrates how combining data warehousing, analytics, machine learning, and cloud deployment creates a production-ready churn prediction system capable of real-world business impact.

---

## 📎 Links

**GitHub Repository**  
[https://github.com/the-noble-analyst/Customer-Churn-Prediction-System](https://github.com/the-noble-analyst/Customer-Churn-Prediction-System)

**Power BI Dashboard**  
[https://github.com/the-noble-analyst/Customer-Churn-Prediction-System/tree/main/PowerBI_Dashboard](https://github.com/the-noble-analyst/Customer-Churn-Prediction-System/tree/main/PowerBI_Dashboard)

---

## 📝 License

MIT License

---

## 👤 Author

**Nabeel Siddiqui**

**GitHub**  
[https://github.com/the-noble-analyst](https://github.com/the-noble-analyst)

**LinkedIn**  
[https://www.linkedin.com/in/nabeelsiddiqui468](https://www.linkedin.com/in/nabeelsiddiqui468)

---

## ⭐ If you found this project helpful, consider giving it a star!
