# 📊 Business Analytics & Visualization: KPI Dashboard

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B)](https://streamlit.io/)  
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-yellow)](https://pandas.pydata.org/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  

An interactive **Streamlit** dashboard for **business KPI analytics and visualization**,  
featuring **dynamic filters**, **time-based aggregations**, and **automated charting**  
to help you explore your sales data and uncover actionable insights.  

---

## 🚀 Features

- **CSV Upload & Data Processing**
  - Upload sales data in CSV format with required fields.
  - Automatic date parsing with error handling.
  - Derived fields for **Month**, **Quarter**, **Year**, and **Shipping Duration**.

- **KPI Selection**
  - Pick any numeric column (e.g., `Sales`, `Profit`, `Quantity`) for analysis.
  - Choose from **Sum**, **Mean**, **Max**, or **Min** aggregations.

- **Dynamic Filtering**
  - Filter by Region, Category, Segment, and Order Date range.
  - Multi-select filters with default “All” selection.

- **Visual Insights**
  - KPI trends over time (line charts).
  - KPI breakdown by Region and Category (bar charts).
  - Summary statistics for the selected KPI.

---

## 📊 KPI Aggregation Behavior

This dashboard dynamically calculates and visualizes KPIs using your selected **aggregation function**:  

- **Sum**: Adds up all KPI values within each group.  
- **Mean**: Calculates the average KPI value.  
- **Max**: Shows the highest KPI value in the group.  
- **Min**: Shows the lowest KPI value in the group.  

### Why use different aggregations?

- **Sum** helps track total sales or profit trends.  
- **Mean** can highlight performance consistency.  
- **Max/Min** are useful for spotting outliers or best/worst performance periods.  

### Tips for meaningful analysis:

- Use **Month** granularity for short-term trends.  
- Use **Quarter** or **Year** for strategic, high-level comparisons.  
- Filter by **Segment** or **Region** to focus on specific markets.  

---

## 📂 CSV Format

Your input CSV **must** include at least these columns:  

- **Order Date** — The date when the order was placed.  
- **Ship Date** — The date when the order was shipped.  
- **Region** — Geographic region (e.g., East, West, Central).  
- **Category** — Product category (e.g., Furniture, Technology).  
- **Sales** — Numeric KPI representing sales amount.  
- **Segment** — Customer segment (e.g., Corporate, Consumer).  

Example table:

| Order Date | Ship Date | Region | Category       | Sales  | Segment   |
|------------|-----------|--------|----------------|--------|-----------|
| 2024-01-01 | 2024-01-04| West   | Furniture      | 250.50 | Corporate |
| 2024-01-03 | 2024-01-06| East   | OfficeSupplies | 120.00 | Consumer  |

---

## 🛠 Installation

1. Clone the repository:  
   `git clone git@github.com:Kumar-gaurav-rvce/business-analytics.git`  
   `cd business-analytics`  

2. Install Python dependencies:  
   `pip install -r requirements.txt`  

---

## ▶ Run Locally

Run the app with:  
`streamlit run app.py`  

Then open your browser at **http://localhost:8501**.  

---

## 📊 Quick Start with Example Data

Example table:

| Order Date | Ship Date | Region | Category       | Sales  | Segment   |
|------------|-----------|--------|----------------|--------|-----------|
| 2024-01-01 | 2024-01-04| West   | Furniture      | 250.50 | Corporate |
| 2024-01-03 | 2024-01-06| East   | OfficeSupplies | 120.00 | Consumer  |

Upload it via the **📂 Upload CSV** option in the app.  

---

## ☁ Deployment on Streamlit Cloud

1. Push the code to your GitHub repository.  
2. Go to [Streamlit Cloud](https://share.streamlit.io/) and create a **New App** from your repo.  
3. Deploy 🚀  

---

## 📦 Project Structure

kpi-dashboard/
│
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── sample_data.csv # Example sales data (optional)


---
## 🔄 Workflow Diagram (ASCII)

+----------------------+
| Upload Sales CSV |
+----------+-----------+
|
v
+----------------------+
| Data Processing & |
| Feature Engineering |
+----------+-----------+
|
v
+----------------------+
| Apply Filters & KPI |
| Aggregation |
+----------+-----------+
|
v
+----------------------+
| Visualize KPI Trends |
| & Breakdowns |
+----------------------+


---

## 📜 License

This project is licensed under the [MIT License](LICENSE).  
