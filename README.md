# Supermart Grocery Sales — Retail Analytics

**Version:** 1.1 (Academic Edition)  
**Authors:** You (with AI assistance)  
**Last updated:** 2025-08-17

## Abstract
This study conducts an end-to-end retail analytics workflow on a multi-year Supermart grocery dataset (50,000 transactions).
We examine category performance, seasonality, customer value (RFM), and simple demand forecasting using feature-driven baselines.
Findings indicate pronounced Q4 seasonality, strong contribution from Beverages and Dairy, and a long-tail product distribution where a small fraction of products explains a large share of sales.

## Introduction
Modern retailers rely on data-driven insights to optimize assortment, promotions, and fulfillment.
We reproduce a reproducible pipeline inspired by typical Kaggle repositories and your prior projects to ensure clarity and portability.

## Dataset
- **File:** `data/raw/supermart_sales.csv` (50,000 rows, 2019–2024)
- **Schema:** Orders with product/category, pricing, discount, and geography; engineered time features (Year, Month, Quarter, Weekday, IsWeekend, FestiveQ4).
- **Data Dictionary:** `data/raw/supermart_data_dictionary.csv`

## Research Questions
1. Which categories and sub-categories drive revenue and profit?  
2. What temporal patterns (seasonality, weekday/weekend) impact sales?  
3. Which customers are most valuable (RFM)?  
4. Can simple time-based features achieve reasonable sales forecasts?  
5. Which product pairs tend to co-occur within the same orders?

## Methodology
1. **Data Preparation:** Deduplicate, sanity checks, and derive calendar features.  
2. **Exploratory Data Analysis:** Category/region mixes, sub-category leaders, weekday effects, Pareto analysis.  
3. **Customer Analytics:** RFM segmentation to rank customers by value.  
4. **Forecasting:** Ridge/Lasso baselines using time indices and calendar features.  
5. **Basket Analysis:** Lightweight co-occurrence over order-level item sets.

## Experiments & Results (Summary)
- **Category Mix:** Beverages and Dairy are top contributors by sales.  
- **Seasonality:** Monthly series show uplift in **Oct–Dec**, visible in the moving average and heatmap.  
- **Customer Value:** RFM reveals skewed Monetary distribution with a small set of high-value customers.  
- **Forecasting:** Linear baselines (Ridge/Lasso) achieve reasonable MAE for category-level monthly sales (see `03_TimeSeries_Features.ipynb`).  
- **Co-occurrence:** Frequently co-ordered pairs include snacks with beverages and bakery items.

## Reproducibility
```
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Generate images and quick stats
python scripts/preprocess.py
python scripts/eda.py
python scripts/model_forecast.py  # baseline forecast & plot
```

## Repository Structure
```
Supermart-Grocery-Sales-Retail-Analytics/
├── configs/
│   └── config.yml
├── data/
│   ├── raw/
│   │   ├── supermart_sales.csv  (50k rows)
│   │   └── supermart_data_dictionary.csv
│   └── processed/
├── dashboards/
│   └── README.md
├── images/
│   ├── sales_by_category.png
│   ├── orders_per_month.png
│   ├── top15_subcategory_sales.png
│   ├── profit_vs_sales_by_category.png
│   ├── monthly_sales_moving_avg.png
│   ├── seasonality_heatmap.png
│   ├── region_category_stacked_share.png
│   ├── rfm_recency_hist.png
│   ├── rfm_frequency_hist.png
│   └── rfm_monetary_hist.png
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Modeling_RFM.ipynb
│   ├── 03_TimeSeries_Features.ipynb
│   └── 04_Basket_Cooccurrence.ipynb
├── reports/
│   └── Executive_Summary.md
├── scripts/
│   ├── preprocess.py
│   ├── eda.py
│   └── model_forecast.py
├── tests/
│   ├── test_shapes.py
│   └── test_time_fields.py
├── requirements.txt
└── README.md
```

## Figures (selected)
- **Top 15 Sub-Categories by Sales** (`images/top15_subcategory_sales.png`)  
- **Profit vs Sales by Category** (`images/profit_vs_sales_by_category.png`)  
- **Monthly Sales with 3M Moving Average** (`images/monthly_sales_moving_avg.png`)  
- **Seasonality Heatmap** (`images/seasonality_heatmap.png`)  
- **Region-wise Category Mix (Share)** (`images/region_category_stacked_share.png`)  
- **RFM Distributions** (`images/rfm_*`)  
- **Pareto of Product Contribution** (`images/pareto_top_products.png`)

## Limitations
Synthetic yet Kaggle-style schema; results are illustrative, not real business indicators.
Advanced models (Prophet/ARIMA, deep learning, true market basket mining) are out of scope for the minimal dependency stack.

## How to Cite
> Supermart Grocery Sales — Retail Analytics (Academic Edition), 2025.