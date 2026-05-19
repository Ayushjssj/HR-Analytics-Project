# HR Analytics Dashboard & Attrition Prediction

An end-to-end HR Analytics project built using Python, SQL, MySQL, Power BI, and Machine Learning to analyze employee attrition, workforce trends, and organizational insights.

This project focuses on identifying key factors affecting employee attrition and generating actionable business insights through data analysis, interactive dashboards, and predictive modeling.

---

# Project Overview

Employee attrition is one of the major challenges faced by organizations. High attrition rates impact productivity, increase recruitment costs, and reduce overall organizational efficiency.

This project aims to:
- Analyze employee attrition patterns
- Identify factors influencing employee turnover
- Generate HR business insights
- Build interactive Power BI dashboards
- Predict attrition using Machine Learning

The project demonstrates a complete analytics workflow from raw data preprocessing to dashboard visualization and predictive analytics.

---

# Tech Stack

- Python
- Pandas
- NumPy
- SQL
- MySQL
- Power BI
- SQLAlchemy
- PyMySQL
- Scikit-learn
- Machine Learning

---

# Project Workflow

```text
Dataset → Data Cleaning → EDA → MySQL Integration → SQL Analysis → Power BI Dashboard → Machine Learning Prediction
```

---

# Business Problem Statement

Organizations often struggle to understand:
- Why employees leave the company
- Which departments experience high attrition
- How salary and overtime affect retention
- Which employee groups are at high attrition risk

This project helps HR teams and management:
- Improve employee retention
- Identify high-risk employees
- Optimize workforce management
- Support data-driven HR decisions

---

# Features

## Data Analysis
- Employee attrition analysis
- Department-wise workforce analysis
- Salary trend analysis
- Overtime impact analysis
- Gender-based workforce insights
- Age distribution analysis

## Dashboard Features
- Total Employees KPI
- Attrition Count KPI
- Average Salary KPI
- Attrition Distribution Pie Chart
- Department vs Attrition Analysis
- Overtime vs Attrition Analysis
- Monthly Income Analysis
- Interactive Slicers & Filters

## Machine Learning
- Employee attrition prediction
- Random Forest Classification Model
- Accuracy Evaluation
- Classification Report & Confusion Matrix

---

# Exploratory Data Analysis (EDA)

Performed EDA using Python and Pandas to:
- Understand employee demographics
- Analyze attrition distribution
- Compare salaries and attrition
- Study overtime patterns
- Detect workforce trends

Visualization libraries used:
- Matplotlib
- Seaborn

---

# SQL Analysis

Performed SQL-based business analysis using MySQL.

## Sample Queries

```sql
-- Total Employees
SELECT COUNT(*) AS Total_Employees
FROM hr_data;

-- Attrition Distribution
SELECT Attrition, COUNT(*) AS Employee_Count
FROM hr_data
GROUP BY Attrition;

-- Department-wise Attrition
SELECT Department, Attrition, COUNT(*) AS Count
FROM hr_data
GROUP BY Department, Attrition;

-- Overtime Analysis
SELECT OverTime, Attrition, COUNT(*) AS Count
FROM hr_data
GROUP BY OverTime, Attrition;
```

---

# Machine Learning Model

Implemented a Random Forest Classifier to predict employee attrition.

## ML Workflow
- Data preprocessing
- Label encoding
- Train-test split
- Model training
- Prediction & evaluation

## Model Performance
- Accuracy Score
- Confusion Matrix
- Classification Report

---

# Power BI Dashboard

Built an interactive HR Analytics dashboard containing:

## KPI Cards
- Total Employees
- Attrition Count
- Average Monthly Income

## Visualizations
- Attrition Distribution
- Department-wise Attrition
- Overtime Impact
- Salary Analysis
- Age Distribution

## Interactive Features
- Department Filters
- Gender Filters
- Job Role Filters
- Overtime Filters

---

# Dashboard Screenshots

## Dashboard Overview
(Add Screenshot Here)

## Attrition Distribution
(Add Screenshot Here)

## Department Analysis
(Add Screenshot Here)

## Overtime Analysis
(Add Screenshot Here)

## Salary Analysis
(Add Screenshot Here)

---

# Folder Structure

```bash
HR-Analytics-Project/
│
├── data/
│   └── hr_data.csv
│
├── output/
│   └── cleaned_hr_data.csv
│
├── scripts/
│   ├── hr_analysis.py
│   ├── hr_mysql_upload.py
│   ├── hr_attrition_prediction.py
│   └── sql_queries.sql
│
├── dashboard/
│   └── HR_Analytics_Dashboard.pbix
│
├── screenshots/
│   ├── dashboard_overview.png
│   ├── attrition_distribution.png
│   ├── department_analysis.png
│   ├── overtime_analysis.png
│   └── salary_analysis.png
│
└── README.md
```

---

# Key Business Insights

- Employees working overtime showed higher attrition rates.
- Certain departments experienced significantly higher employee turnover.
- Salary and job satisfaction influenced employee retention.
- Younger employees had comparatively higher attrition rates.

---

# How to Run Project

## Step 1 — Install Required Libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn sqlalchemy pymysql
```

## Step 2 — Run HR Analysis

```bash
python hr_analysis.py
```

## Step 3 — Upload Data to MySQL

```bash
python hr_mysql_upload.py
```

## Step 4 — Run ML Prediction

```bash
python hr_attrition_prediction.py
```

## Step 5 — Open Power BI Dashboard

Open:
```bash
HR_Analytics_Dashboard.pbix
```

---

# Future Improvements

- Advanced ML models
- Real-time HR analytics
- Employee performance prediction
- Cloud dashboard deployment
- AI-based workforce insights

---

# Learning Outcomes

Through this project, I gained practical experience in:
- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- SQL Querying
- Database Integration
- Dashboard Development
- Business Intelligence
- Machine Learning
- Predictive Analytics

---

## Author
### Ayush Pandey<br>
Aspiring Data Analyst & GenAI Enthusiast
- Python
- SQL
- MySQL
- Power BI
- Data Visualization
- Business Intelligence

### License 
This Project is licensed under the MIT License

---

⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!

# Tags

#Python #SQL #MySQL #PowerBI #MachineLearning #HRAnalytics #DataAnalytics #BusinessIntelligence #EDA #DataScience
