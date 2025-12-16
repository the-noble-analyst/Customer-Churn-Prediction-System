# Customer Churn Prediction System

An end-to-end customer churn analytics and machine learning project that transforms raw transactional data into actionable churn risk insights using SQL Server, Power BI, and Python-based machine learning.

This project demonstrates how data engineering, analytics, and ML can work together to support proactive customer retention decisions.

## 📌 Problem Statement

Customer churn leads to direct revenue loss and increased acquisition costs.
The objective of this project is to identify customers at high risk of churn using historical transaction and behavior data so that retention actions can be taken before disengagement becomes permanent.

## 🎯 Business Objective

Predict whether a customer is likely to churn in a defined future time window \\
Prioritize churn recall over accuracy to minimize missed at-risk customers //
Provide probability-based churn scores instead of rigid binary predictions

## 🧱 Project Architecture
This project follows a full analytics pipeline:

### SQL Data Warehouse (Medallion Architecture)
Bronze: Raw sales and customer data

Silver: Cleaned and standardized tables

Gold: Analytics-ready customer behavior tables

### SQL Exploratory Analysis
Customer behavior trends
Purchase frequency and recency analysis
Advanced queries using CTEs and window functions

### Business Dashboard (Power BI)
Sales and customer KPIs
Customer segmentation
Churn indicators for stakeholders

### Machine Learning (Python)
Feature engineering
Churn modeling
Evaluation and threshold tuning

📂 Repository Structure
Customer-Churn-Analytics/
│
├── 01_Data_Warehouse_SQL/
│   ├── Bronze_Raw_Load.sql
│   ├── Silver_Cleaned_Tables.sql
│   ├── Gold_Analytics_Tables.sql
│
├── 02_SQL_Exploratory_Analysis/
│   ├── Customer_Behavior_Analysis.sql
│   ├── Advanced_SQL_Queries.sql
│
├── 03_PowerBI_Dashboard/
│   ├── Customer_Churn_Dashboard.pbix
│   └── dashboard_screenshots/
│
├── 04_Churn_Prediction_ML/
│   ├── Customer_Churn_Prediction_Retail.ipynb
│   └── requirements.txt
│
└── README.md

## 🛠️ Tools & Technologies
Programming: Python, SQL
Machine Learning: Scikit-learn, Random Forest
Data Engineering: SQL Server, ETL Pipelines, Medallion Architecture
Visualization: Power BI
Analysis: Pandas, NumPy, Matplotlib, Seaborn

## 🔧 Feature Engineering
Key behavioral features engineered from transactional data:
Recency (time since last purchase)
Total orders and total quantity
Customer lifespan
Total sales and average order value
Average monthly spend

These features capture engagement, value, and behavioral change, which are critical for churn prediction.

## 🧠 Churn Definition
A customer is labeled as churned if they made no purchases within a defined future observation window after the prediction cutoff date.

This time-based definition:
Prevents data leakage
Reflects real-world churn behavior
Enables realistic model evaluation

## 🤖 Model Training
Model used: Random Forest Classifier
Reason: Handles non-linear relationships, feature interactions, and correlated features well
Class imbalance handled using class_weight='balanced'

## 📊 Model Performance
Accuracy: 83%
Recall (Churn class): 95% (after threshold tuning)

## Why Recall Matters
Missing a churned customer is more costly than incorrectly flagging an active one.
The model is optimized to catch as many at-risk customers as possible.

## 🎚️ Threshold Tuning
Instead of using the default 0.50 threshold:
The decision threshold was lowered to 0.30
This increased churn recall significantly
Supports early intervention strategies

## 📈 Model Interpretability
Feature importance analysis shows:
Recency is the strongest churn driver
Customer lifespan strongly influences retention
Spending and frequency features provide supporting signals
This aligns with business intuition: recent disengagement matters more than historical value.

## 💼 Business Impact
Enables proactive retention instead of reactive churn handling
Helps teams prioritize high-risk customers using churn probabilities
Supports smarter allocation of marketing and retention resources

## 🚀 Key Takeaway
This project demonstrates how combining data warehousing, analytics, and machine learning can create a practical churn prediction system that delivers real business value.

## 📎 Links
GitHub Repository: (add link here)
Power BI Dashboard: (add link or screenshots)
