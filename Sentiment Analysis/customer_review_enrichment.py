import pandas as pd 
import numpy as np 
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sqlalchemy import create_engine

# Download VADER lexicon only if not already available
try:
    nltk.data.find("sentiment/vader_lexicon.zip")
except LookupError:
    nltk.download("vader_lexicon")

# SQL Server Connection (Using SQLAlchemy)
SERVER = r"Kanishka\SQLEXPRESS"
DATABASE = "PortfolioProject_MarketingAnalytics"

connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

# Read Customer Reviews
query = """
SELECT
    ReviewID,
    CustomerID,
    ProductID,
    ReviewDate,
    Rating,
    ReviewText
FROM dbo.customer_reviews;
"""

customer_reviews_df = pd.read_sql(query, engine)

# Initialize Sentiment Analyzer

sia = SentimentIntensityAnalyzer()

# Calculate Sentiment Score

def calculate_sentiment(review):

    if pd.isna(review):
        return 0

    return sia.polarity_scores(str(review))["compound"]

customer_reviews_df["SentimentScore"] = (
    customer_reviews_df["ReviewText"]
    .apply(calculate_sentiment)
)

# Categorize Sentiment

def categorize_sentiment(score, rating):

    if score > 0.05:

        if rating >= 4:
            return "Positive"

        elif rating == 3:
            return "Mixed Positive"

        else:
            return "Mixed Negative"

    elif score < -0.05:

        if rating <= 2:
            return "Negative"

        elif rating == 3:
            return "Mixed Negative"

        else:
            return "Mixed Positive"

    else:

        if rating >= 4:
            return "Positive"

        elif rating <= 2:
            return "Negative"

        else:
            return "Neutral"

customer_reviews_df["SentimentCategory"] = customer_reviews_df.apply(
    lambda row: categorize_sentiment(
        row["SentimentScore"],
        row["Rating"]
    ),
    axis=1
)

# Sentiment Buckets

def sentiment_bucket(score):

    if score >= 0.5:
        return "0.5 to 1.0"

    elif 0.0 <= score < 0.5:
        return "0.0 to 0.49"

    elif -0.5 <= score < 0.0:
        return "-0.49 to 0.0"

    else:
        return "-1.0 to -0.5"


customer_reviews_df["SentimentBucket"] = (
    customer_reviews_df["SentimentScore"]
    .apply(sentiment_bucket)
)

   
# Display Sample

print(customer_reviews_df.head())

# Save to SQL Server

customer_reviews_df.to_sql(
    "fact_customer_reviews_sentiment",
    con=engine,
    if_exists="replace",
    index=False
)

# Optional CSV Backup
customer_reviews_df.to_csv(
    "fact_customer_reviews_with_sentiment.csv",
    index=False
)

print("\nSentiment Analysis Completed Successfully")