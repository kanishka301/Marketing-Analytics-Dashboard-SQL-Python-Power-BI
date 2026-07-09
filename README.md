# Marketing Analytics Insights Project

## Overview

This project presents an end-to-end marketing analytics solution for **ShopEasy**, an online retail company facing declining customer engagement and conversion rates despite increased marketing investments.

Using **SQL, Python, and Power BI**, the project analyzes customer journeys, marketing campaign performance, engagement metrics, and customer feedback to uncover key business insights and provide actionable recommendations for improving marketing effectiveness and customer satisfaction.

---

## Business Problem

ShopEasy has been experiencing a decline in customer engagement and conversion rates despite significant investments in marketing campaigns. The marketing and customer experience teams require a comprehensive analysis to understand campaign effectiveness, identify customer pain points, and optimize marketing strategies using data-driven insights.

### Key Challenges

- Declining customer engagement across marketing channels.
- Reduced website conversion rates despite steady traffic.
- Marketing investments delivering lower-than-expected returns.
- Need to analyze customer reviews to identify improvement opportunities.

---

## Project Objectives

- Optimize website conversion rates by identifying factors affecting customer purchases.
- Improve customer engagement by analyzing content performance across marketing channels.
- Analyze customer feedback using sentiment analysis to uncover customer satisfaction trends.
- Deliver actionable business recommendations through interactive dashboards and visual storytelling.

---

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| **SQL** | Data cleaning, preprocessing, transformation, and feature engineering |
| **Python (Pandas, NLTK VADER)** | Sentiment analysis and customer review classification |
| **Power BI** | Interactive dashboard development and business visualization |

---

# Methodology

## 1. Data Cleaning & Preparation (SQL)

Raw marketing data from the **PortfolioProject_MarketingAnalytics** database was cleaned and transformed using SQL.

### Key preprocessing tasks

### Customer Journeys
- Removed duplicate records.
- Replaced missing **Duration** values using the daily average.

### Engagement Data
- Standardized inconsistent content types (e.g., *Socialmedia → Social Media*).
- Split combined engagement metrics into separate **Views** and **Clicks** columns.
- Removed unnecessary **Newsletter** records.

### Customer Reviews
- Cleaned review text by removing extra spaces and formatting inconsistencies.

### Dimension Tables
- Created customer and product dimension tables.
- Generated **Price Category** for product segmentation.

---

## 2. Sentiment Analysis (Python)

Customer reviews were analyzed using **Python** and the **NLTK VADER** sentiment analysis library.

The workflow included:

- Loading the cleaned customer review dataset.
- Calculating sentiment scores using VADER.
- Combining sentiment scores with customer ratings.
- Classifying reviews into:
  - Positive
  - Negative
  - Mixed Positive
  - Mixed Negative
  - Neutral
- Exporting the enriched dataset for visualization in Power BI.

---

## 3. Interactive Dashboard (Power BI)

The processed datasets were integrated into Power BI to build an interactive dashboard that visualizes marketing performance and customer behavior.

The dashboard focuses on:

- Conversion performance
- Customer engagement
- Marketing channel effectiveness
- Customer sentiment
- Business recommendations

---

# Key Insights

## Conversion Performance

- Overall website conversion rate: **8.5%**
- Highest conversion observed in **January (19.6%)**
- Lowest conversion observed in **May (4.3%)**
- Products such as **Ski Boots, Kayaks, and Baseball Gloves** recorded the highest conversion rates.

---

## Customer Engagement

- Social media engagement peaked during **February** and **July**, followed by a noticeable decline from **August onwards**.
- Overall Click-Through Rate (CTR): **15.37%**
- Blog content generated the highest customer engagement and views.

---

## Customer Feedback

- Average customer rating: **3.7 / 5**, below the business target of **4.0**.
- Sentiment analysis identified:
  - **275 Positive Reviews**
  - **82 Negative Reviews**
  - Multiple Mixed Sentiment reviews indicating improvement opportunities.
- Mixed customer feedback highlights areas where service improvements could significantly increase customer satisfaction.

---

# Business Recommendations

## Increase Conversion Rates

- Increase promotional investment in high-converting products such as **Kayaks** and **Ski Boots**.
- Launch seasonal campaigns during historically high-performing months.
- Introduce targeted promotions during low-conversion periods to improve sales performance.

---

## Improve Customer Engagement

- Refresh content strategy with interactive content and user-generated media.
- Optimize Calls-to-Action (CTAs) across blogs and social media channels.
- Increase content publishing during periods of declining engagement.

---

## Enhance Customer Satisfaction

- Implement a structured feedback analysis process for mixed and negative reviews.
- Address recurring customer concerns to improve satisfaction and retention.
- Encourage satisfied customers to update ratings after successful issue resolution.

---

# Project Outcome

This project demonstrates an end-to-end marketing analytics workflow by combining **SQL**, **Python**, and **Power BI** to transform raw marketing data into actionable business insights. The analysis helps identify opportunities to improve conversion rates, enhance customer engagement, optimize marketing strategies, and strengthen customer satisfaction through data-driven decision-making.

---

## Project Structure

```
Marketing-Analytics-Insights/
│
├── SQL/
│   ├── fact_customer_journeys.sql
│   ├── fact_engagement_data.sql
│   ├── fact_customer_reviews.sql
│   ├── dim_products.sql
│   └── dim_customers.sql
│
├── Python/
│   └── Marketing_analytics_insights.ipynb
│
├── Power BI/
│   └── Marketing Analytics Dashboard.pbix
│
├── Presentation/
│   └── Final Presentation.pdf
│
├── Report/
│   └── Final Report.pdf
│
├── Dataset/
│
└── README.md
```

---
