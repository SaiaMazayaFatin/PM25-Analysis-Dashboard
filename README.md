# 🌫️ PM2.5 Analysis Dashboard  

This **PM2.5 Analysis Dashboard** is built using **Streamlit** to visualize and analyze air pollution trends based on PM2.5 concentration data. The project covers data wrangling, exploratory data analysis (EDA), data visualization, clustering (binning), and dashboard development.  

---

## 📌 Project Workflow  

### 1️⃣ Data Wrangling  
- Cleaning and preparing the dataset for analysis.  
- Handling missing values and ensuring data consistency.  
- Converting date and time fields for proper analysis.  

### 2️⃣ Exploratory Data Analysis (EDA)  
- Understanding air pollution trends over time.  
- Analyzing PM2.5 concentration across different hours, months, and years.  
- Detecting seasonal patterns in air quality.  

### 3️⃣ Data Visualization  
- Line charts for monthly and hourly PM2.5 trends.  
- Bar charts to show categorized PM2.5 pollution levels.  
- Interactive filtering for better insights.  

### 4️⃣ Clustering using Binning  
- Categorizing PM2.5 levels into different pollution levels:  
  - **Low (Rendah)**: 0 - 35 µg/m³  
  - **Moderate (Sedang)**: 36 - 75 µg/m³  
  - **High (Tinggi)**: 76 - 115 µg/m³  
  - **Very High (Sangat Tinggi)**: >115 µg/m³  
- Analyzing the frequency of each pollution category.  

### 5️⃣ Dashboard Development  
- Building an interactive dashboard using Streamlit to display the analysis results.  
- Allowing users to explore air pollution trends dynamically.  

---

## 🌟 Key Features  
✅ **Trend Analysis**: Monthly and daily PM2.5 concentration trends.  
✅ **Hourly Distribution**: How PM2.5 levels fluctuate throughout the day.  
✅ **Pollution Categories**: Distribution of air quality levels using clustering (binning).  
✅ **Interactive Dashboard**: Users can explore the data with filters.  

---

## 📂 Dataset  
This project uses the cleaned dataset:  

- **`PRSA_Data_Aotizhongxin_Cleaned.csv`**: Contains air pollution data from 2013-2017.  

Ensure this dataset is placed in the project directory before running the dashboard.  

---

## 🛠️ Installation & Setup  

### 1️⃣ Activate Virtual Environment  
Since a virtual environment **`dashboard-env`** already exists, activate it before running the project.  

#### **🔹 Windows**  
```bash
dashboard-env\Scripts\activate
```
#### **🔹 MacOS**  
```bash
source dashboard-env/bin/activate
```
### 2️⃣ Install Required Libraries 
Ensure all dependencies are installed by running:

```bash
pip install -r requirements.txt
```
### 3️⃣ Run Streamlit Dashboard

```bash
streamlit run dashboard.py
```

