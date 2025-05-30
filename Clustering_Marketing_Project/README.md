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
   - Gaussian Mixture Models
   - Optimal cluster number determination using the elbow method and BIC/AIC
   - Cluster visualization

## Clustering Algorithm Performance

After evaluating multiple clustering approaches, we found the following results:

### 1. **K-Means (Best Performing)**  
- Achieved the highest silhouette score (**0.55**)  
- Produced well-separated, interpretable clusters  
- Optimal for marketing segmentation with clear centroids  

### 2. **Gaussian Mixture Models (Second Best)**  
- Achieved competitive silhouette score (**0.52**)  
- Provided probabilistic cluster assignments  
- Better at handling overlapping distributions than K-Means  

### 3. DBSCAN  
- Struggled with parameter tuning  
- Classified many points as noise  

## Why K-Means Was Chosen

Several clustering algorithms were considered for this project. While **Gaussian Mixture Models** showed strong results as the second-best approach, **K-Means** was ultimately superior because:

1. **Business Interpretability**  
   - Hard cluster assignments are easier for marketing teams to implement  
   - Clear centroid-based profiles for each customer segment  

2. **Visual Clarity**  
   - Spherical clusters are more intuitive to visualize in 2D/3D plots  

3. **Computational Efficiency**  
   - Faster to train and predict compared to GMM  

4. **Stability**  
   - Less sensitive to initialization than GMM  

5. **Scalability**  
   - Highly efficient for larger datasets and real-time applications  

6. **Well-defined Centroids**  
   - Business stakeholders easily understand cluster "averages"  

GMM remains a powerful alternative when:
- You need probability scores for cluster membership  
- Your data has non-spherical cluster shapes  
- You suspect overlapping customer segments  

For the goals of this marketing analysis—quick segmentation, visual interpretability, and ease of integration into a web app—**K-Means provided the best combination of performance and business utility**, with GMM as a close second for more probabilistic analysis.

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
   - Compare different clustering approaches (K-Means vs GMM)
   - View probabilistic assignments for GMM

3. **Customer Insights**
   - Profile analysis of each segment
   - Marketing strategy recommendations per segment
   - Demographic breakdowns

### How to Run the Streamlit App

1. Install required packages:
   ```bash
   pip install streamlit pandas numpy matplotlib seaborn scikit-learn
   ```

2. Run the app:
   ```bash
   streamlit run mall_segmentation_app.py
   ```

The app provides interactive controls to adjust clustering parameters and visualize the results in real-time, making it a powerful tool for marketing analysts to explore customer segments.