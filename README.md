# 🥔 Potato Production, Climate Impact & Disease Risk Analysis (Maritimes, Canada)

# Python 3.13.9

## 📌 Overview
This project analyzes potato production trends in Atlantic Canada and evaluates how climate conditions influence agricultural output and disease risk.

The analysis integrates:
- Data Processing
- Machine Learning
- Generative AI

---

## 🎯 Objectives
- Analyze potato production trends (2015–2025)
- Integrate climate data (temperature and precipitation)
- Predict production using machine learning
- Estimate disease risk using a proxy model
- Generate automated insights using AI

---

## 📊 Data Sources
- Statistics Canada (Potato production dataset)
- Environment and Climate Change Canada (Climate data)

---

## 🧠 Methods

### Data Processing
- Data cleaning and filtering (Maritime provinces)
- Unit conversion (acres → hectares, cwt → tonnes)
- Data transformation (long → wide format)
- Feature engineering (lag, rolling averages, deviations)

---

### Machine Learning

#### Regression Model
- Algorithm: Random Forest Regressor
- Purpose: Predict potato production
- Performance:
  - R²: **0.88**
  - MAE: **~97,000 tonnes**

### Classification Model
- Algorithm: Random Forest Classifier  
- Purpose: Estimate disease risk (proxy based on rainfall and yield drop)

#### Performance:
- Accuracy: ~67%

#### Key Observations:
- The model performed well in identifying low-risk years but struggled to detect high-risk disease cases.
- This is due to class imbalance, where high-risk events are relatively rare in the dataset.

#### Modeling Decision:
- Techniques such as SMOTE (Synthetic Minority Over-sampling Technique) were considered but not applied.
- Given the small dataset size, introducing synthetic data could lead to overfitting and reduce model reliability.

#### Future Improvements:
- Apply resampling techniques (e.g., SMOTE) with larger datasets
- Collect real disease incidence data
- Explore alternative evaluation metrics (recall, F1-score) and models

---

### Generative AI
- Automated report generation using OpenAI API
- Produces human-readable agricultural insights

---

## 📈 Key Insights
- Potato production is strongly influenced by land area and climate variables
- Rainfall variability plays a significant role in yield fluctuations
- Class imbalance affects risk prediction and requires careful handling

---

## ⚠️ Limitations
- Disease risk is based on a proxy, not real disease data
- Dataset size is relatively small
- External variables (soil, pests, farming practices) not included

---

## 🚀 How to Run

### 1. Clone repository
```bash
git clone https://github.com/YOUR_USERNAME/maritimes-potato-production-analysis.git
cd maritimes-potato-production-analysis

### 2. Setup environment
