# Customer Churn Prediction System

An end-to-end customer churn analytics and machine learning project that transforms raw transactional data into actionable churn risk insights using SQL Server, Power BI, and Python-based machine learning.

This project demonstrates how data engineering, analytics, and ML can work together to support proactive customer retention decisions.

---

## 📌 Problem Statement

Customer churn leads to direct revenue loss and increased acquisition costs. The objective of this project is to identify customers at high risk of churn using historical transaction and behavior data so that retention actions can be taken before disengagement becomes permanent.

---

## 🎯 Business Objective

- Predict whether a customer is likely to churn in a defined future time window
- Prioritize churn recall over accuracy to minimize missed at-risk customers
- Provide probability-based churn scores instead of rigid binary predictions

---

## 🧱 Project Architecture

This project follows a full analytics pipeline:

### SQL Data Warehouse (Medallion Architecture)
- **Bronze**: Raw sales and customer data
- **Silver**: Cleaned and standardized tables
- **Gold**: Analytics-ready customer behavior tables

### SQL Exploratory Analysis
- Customer behavior trends
- Purchase frequency and recency analysis
- Advanced queries using CTEs and window functions

### Business Dashboard (Power BI)
- Sales and customer KPIs
- Customer segmentation
- Churn indicators for stakeholders

### Machine Learning (Python)
- Feature engineering
- Churn modeling
- Evaluation and threshold tuning

---

## 📂 Repository Structure

```
Customer-Churn-Analytics/
│
├── Churn_Prediction_ML/
│   ├── Customer_Churn_Analysis_and_Prediction.ipynb
│   └── placeholder
│
├── Data_Warehouse_SQL/
│   ├── datasets/
│   │   ├── source_crm/
│   │   │   ├── cust_info.csv
│   │   │   ├── placeholder
│   │   │   ├── prd_info.csv
│   │   │   └── sales_details.csv
│   │   ├── source_erp/
│   │   │   ├── CUST_AZ12.csv
│   │   │   ├── LOC_A101.csv
│   │   │   ├── PX_CAT_G1V2.csv  
│   ├── docs/
│   │   ├── data_architecture.png
│   │   ├── data_catalog.md
│   │   ├── data_flow.png
│   │   ├── data_integration.png
│   │   ├── data_model.png
│   │   ├── etl.png
│   │   ├── naming_conventions.md
│   │   
│   ├── scripts/
│   │   ├── bronze/
│   │   │   ├── ddl_bronze.sql
│   │   │   ├── placeholder
│   │   │   └── proc_load_bronze.sql
│   │   ├── gold/
│   │   │   ├── ddl_gold.sql
│   │   │ 
│   │   ├── silver/
|   |   |    ├──ddl_silver.sql
|   |   |    └──proc_load_silver.sql
│   │   ├── init_database.sql
│   ├── tests/
│   │   ├── placeholder
│   │   ├── quality_checks_gold.sql
│   │   └── quality_checks_silver.sql
├── PowerBI_Dashboard/
│   ├── Power Bi Report.png
│   ├── PowerBi Report Insights.md
├── SQL_Exploratory_Analysis/
│   ├── 00_init_database.sql
│   ├── 01_database_exploration.sql
│   ├── 02_dimensions_exploration.sql
│   ├── 03_date_range_exploration.sql
│   ├── 04_measures_exploration.sql
│   ├── 05_magnitude_analysis.sql
│   ├── 06_ranking_analysis.sql
│   ├── 07_change_over_time_analysis.sql
│   ├── 08_cumulative_analysis.sql
│   ├── 09_performance_analysis.sql
│   ├── 10_data_segmentation.sql
│   ├── 11_part_to_whole_analysis.sql
│   ├── 12_report_customers.sql
│   ├── 13_report_products.sql
├── LICENSE
└── README.md
```
---

## 🛠️ Tools & Technologies

- **Programming**: Python, SQL
- **Machine Learning**: Scikit-learn, Random Forest
- **Data Engineering**: SQL Server, ETL Pipelines, Medallion Architecture
- **Visualization**: Power BI
- **Analysis**: Pandas, NumPy, Matplotlib, Seaborn

---

## 🔧 Feature Engineering

Key behavioral features engineered from transactional data:

- **Recency** (time since last purchase)
- **Total orders** and **total quantity**
- **Customer lifespan**
- **Total sales** and **average order value**
- **Average monthly spend**

These features capture engagement, value, and behavioral change, which are critical for churn prediction.

---

## 🧠 Churn Definition

A customer is labeled as **churned** if they made no purchases within a defined future observation window after the prediction cutoff date.

This time-based definition:
- Prevents data leakage
- Reflects real-world churn behavior
- Enables realistic model evaluation

---

## 🤖 Model Training

- **Model used**: Random Forest Classifier
- **Reason**: Handles non-linear relationships, feature interactions, and correlated features well
- **Class imbalance handled** using `class_weight='balanced'`

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| **Accuracy** | 83% |
| **Recall (Churn class)** | 95% (after threshold tuning) |

### Why Recall Matters

Missing a churned customer is more costly than incorrectly flagging an active one. The model is optimized to catch as many at-risk customers as possible.

---

## 🎚️ Threshold Tuning

Instead of using the default 0.50 threshold:
- The decision threshold was **lowered to 0.30**
- This increased churn recall significantly
- Supports early intervention strategies

---

## 📈 Model Interpretability

Feature importance analysis shows:
- **Recency** is the strongest churn driver
- **Customer lifespan** strongly influences retention
- **Spending and frequency** features provide supporting signals

This aligns with business intuition: recent disengagement matters more than historical value.

---

## 💼 Business Impact

- Enables **proactive retention** instead of reactive churn handling
- Helps teams **prioritize high-risk customers** using churn probabilities
- Supports **smarter allocation** of marketing and retention resources

---

## 🚀 Key Takeaway

This project demonstrates how combining data warehousing, analytics, and machine learning can create a practical churn prediction system that delivers real business value.

---

## 📎 Links

- **GitHub Repository**: [https://github.com/the-noble-analyst/Customer-Churn-Analytics](#)
- **Power BI Dashboard**: [(https://github.com/the-noble-analyst/Customer-Churn-Analytics/blob/main/PowerBI_Dashboard/Power%20Bi%20Report.png](#)

---

## Credits and Attribution

The data warehouse and SQL exploratory analysis components in this repository are based on an educational data warehouse project by Data With Baraa and are used for learning and extension purposes.

All churn modeling, feature engineering, machine learning, Power BI dashboards, and business insights are original work implemented as part of this project.


## 📝 License
This repository is licensed under the MIT License for original code, machine learning models, analytics, and visualizations authored in this project.

Folders containing educational data warehouse and SQL analysis material are credited to their original author and follow their respective usage terms as described in their local README files.


## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👤 Author

**Nabeel Siddiqui**
- GitHub: [https://github.com/the-noble-analyst/](#)
- LinkedIn: [https://www.linkedin.com/in/nabeelsiddiqui468/](#)

---

⭐️ If you found this project helpful, please consider giving it a star!
