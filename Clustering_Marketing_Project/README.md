# Mall Customer Segmentation Analysis

## Overview

This project analyzes customer data from a shopping mall to perform customer segmentation using clustering techniques. The goal is to identify distinct customer groups based on their demographics and shopping behavior to enable targeted marketing strategies.

## Project Author

**M. FURQAN KHAN**  
*Data Scientist & Machine Learning Engineer*

### Connect & Explore
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/furqank73)  
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/fkgaming)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/furqan-khan-256798268/)

## Dataset

The Mall Customer dataset contains information about individual shoppers with the following features:

### Column Descriptions

| Column Name               | Description                                                        |
|---------------------------|--------------------------------------------------------------------|
| **CustomerID**            | Unique identifier assigned to each customer                        |
| **Gender**                | Customer's gender (Male or Female)                                 |
| **Age**                   | Age of the customer (in years)                                     |
| **Annual Income (k$)**    | Customer's annual income in thousands of dollars                   |
| **Spending Score (1-100)**| Score assigned based on customer behavior and spending nature      |

## Analysis Approach

1. **Exploratory Data Analysis (EDA)**
   - Dataset summary statistics
   - Data visualization
   - Feature distribution analysis

2. **Data Preprocessing**
   - Feature scaling

3. **Clustering**
   - K-Means clustering
   - Optimal cluster number determination using the elbow method
   - Cluster visualization

## Why [K-Means](.K-Means_Clustering) Was Chosen

Several clustering algorithms were considered for this project, including DBSCAN and Hierarchical Clustering. However, **K-Means** was selected for the final implementation due to the following reasons:

- **Interpretability and Simplicity:** K-Means produces clear, spherical clusters that are easy to interpret, especially when visualizing in 2D using features like Annual Income and Spending Score.
- **Scalability:** K-Means is highly scalable and computationally efficient, making it suitable for larger datasets and real-time applications.
- **Well-defined Centroids:** Business stakeholders can easily understand the concept of cluster centroids, which represent customer segment "averages".
- **DBSCAN Limitations:** DBSCAN is sensitive to parameter tuning (`eps`, `min_samples`) and struggled with identifying well-separated clusters due to uniform data density. It also classified many points as noise in this dataset.
- **Hierarchical Clustering Challenges:** Hierarchical methods (like Agglomerative Clustering) are computationally more expensive and not scalable to larger datasets. Additionally, dendrogram interpretation becomes less useful with increasing sample size.

For the goals of this marketing analysis—quick segmentation, visual interpretability, and ease of integration into a web app—**K-Means provided the most balanced solution**.

## Key Findings

1. Customers can be segmented into distinct groups based on:
   - Age and spending patterns
   - Income and spending behavior
   - Combined demographic and behavioral characteristics

2. These segments enable:
   - Personalized marketing strategies
   - Improved product targeting
   - Enhanced customer experience and satisfaction

## Streamlit App Implementation

A Streamlit web application has been created to make the customer segmentation analysis interactive and accessible. The app allows users to:

### Features

1. **Data Exploration**
   - Explore statistical summaries
   - Interactive visualizations of customer characteristics

2. **Cluster Analysis**
   - Visualize customer segments
   - Compare different clustering approaches

3. **Customer Insights**
   - Profile analysis of each segment
   - Marketing strategy recommendations per segment
   - Demographic breakdowns

### How to Run the Streamlit App

1. Install required packages:
   ```bash
   pip install streamlit pandas numpy matplotlib seaborn scikit-learn
