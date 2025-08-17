# Supermart Grocery Sales Retail Analytics

## 📘 Project Overview

This project presents a **comprehensive retail analytics case study** on a supermarket dataset. The primary goal is to **analyze customer purchasing behavior, perform exploratory data analysis (EDA), apply RFM segmentation, and develop forecasting models** to derive actionable insights for business growth. Additionally, the project explores the construction of dashboards for effective visualization of retail performance indicators.

The study follows a rigorous data science workflow, encompassing **data preprocessing, descriptive analytics, predictive modeling, and visualization techniques** to support managerial decision-making in the retail sector.

---

## 📂 Repository Structure

```
Supermart-Grocery-Sales-Retail-Analytics/
│── data/
│   └── raw/
│       ├── supermart_sales.csv
│       └── supermart_data_dictionary.csv
│
│── notebooks/
│   ├── 01_EDA.ipynb
│   └── 02_Modeling_RFM.ipynb
│
│── scripts/
│   ├── preprocess.py
│   ├── eda.py
│   └── model_forecast.py
│
│── dashboards/
│   └── README.md
│
│── images/
│   ├── sales_by_category.png
│   └── orders_per_month.png
│
│── configs/
│   └── config.yml
│
│── tests/
│   └── test_shapes.py
│
└── README.md
```

---

## 📊 Dataset Description

* **File:** `supermart_sales.csv`
* **Size:** \~10,000+ records
* **Scope:** Covers transactional data for grocery sales, customer details, and order metadata.

### Key Variables

* **Order ID** → Unique identifier for each transaction
* **Customer ID** → Encoded customer identifier
* **Product Category** → Category of purchased product
* **Order Date** → Date of transaction
* **Quantity** → Units purchased
* **Sales** → Total sales value
* **Profit** → Profit contribution per order

### Data Dictionary

A separate file (`supermart_data_dictionary.csv`) provides semantic definitions of each variable, ensuring transparent interpretation.

---

## 🔍 Methodology

### 1. Data Preprocessing

* Cleaning of missing values and duplicates
* Standardization of categorical variables
* Derivation of new features (e.g., order month, profit ratio)

### 2. Exploratory Data Analysis (EDA)

Implemented in `01_EDA.ipynb`:

* Sales and profit trends across categories
* Seasonal analysis of order frequency
* Customer purchasing distribution
* Outlier detection and impact analysis



### 3. RFM Segmentation

Implemented in `02_Modeling_RFM.ipynb`:

* **Recency (R):** Days since last purchase
* **Frequency (F):** Number of purchases
* **Monetary (M):** Total spending
* Segmentation of customers into tiers: *Champions, Loyal Customers, At-Risk, Hibernating*.

### 4. Forecasting Models

Implemented in `scripts/model_forecast.py`:

* Time-series forecasting of monthly sales
* Evaluation of ARIMA / Prophet approaches
* Assessment of model performance using RMSE

### 5. Dashboarding

The `dashboards/` folder outlines instructions for constructing interactive BI dashboards (Tableau / Power BI) for management-level reporting.

---

## 🛠️ Technologies Used

* **Python** (>=3.8)
* **Libraries:**

  * pandas, numpy → data manipulation
  * matplotlib, seaborn → visualization
  * scikit-learn → preprocessing and modeling
  * statsmodels / fbprophet → forecasting
  * jupyter → interactive notebooks
* **Others:** YAML configs, Pytest for testing

---

## 📈 Key Findings

* **Sales Distribution:** Office Supplies and Beverages are the largest revenue contributors.
* **Seasonality:** Orders peak in Q4, indicating seasonal promotions.
* **Customer Segmentation:** \~20% of customers contribute >60% of revenue (Pareto principle).
* **Forecasting:** Prophet-based models demonstrate improved adaptability to seasonal spikes.

---

## ⚙️ How to Run

1. Clone the repository:

```bash
git clone https://github.com/username/Supermart-Grocery-Sales-Retail-Analytics.git
cd Supermart-Grocery-Sales-Retail-Analytics
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run preprocessing:

```bash
python scripts/preprocess.py
```

4. Explore EDA and modeling:

```bash
jupyter notebook notebooks/01_EDA.ipynb
```

5. Execute forecasting model:

```bash
python scripts/model_forecast.py
```

---

## 🧪 Testing

Unit tests are available under `tests/` to ensure structural consistency of data transformations:

```bash
pytest tests/
```

---

## 📌 Future Work

* Expand dataset with multi-year sales records
* Incorporate advanced ML models (XGBoost, LSTM) for forecasting
* Deploy dashboards using Streamlit for real-time analytics
* Customer churn prediction modeling

---


