import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
from collections import Counter
import re

df = pd.read_csv("data/Womens Clothing E-Commerce Reviews.csv")
df = df[["Review Text", "Rating", "Class Name"]].dropna()

def get_sentiment(text):
    return TextBlob(str(text)).sentiment.polarity

df["Sentiment"] = df["Review Text"].apply(get_sentiment)
df["Sentiment_Label"] = df["Sentiment"].apply(
    lambda x: "Positive" if x > 0.1 else ("Negative" if x < -0.1 else "Neutral")
)

summary = df.groupby("Class Name").agg(
    Avg_Rating=("Rating", "mean"),
    Avg_Sentiment=("Sentiment", "mean"),
    Total_Reviews=("Review Text", "count"),
    Positive_Pct=("Sentiment_Label", lambda x: (x == "Positive").mean() * 100)
).round(3).sort_values("Avg_Sentiment", ascending=False)

print("=== Category-wise Summary ===")
print(summary)

plt.figure(figsize=(10, 6))
summary["Avg_Sentiment"].plot(kind="bar", color="skyblue")
plt.title("Average Sentiment by Category")
plt.ylabel("Average Sentiment Score")
plt.xlabel("Category")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("data/sentiment_by_category.png")
print("\nChart saved to data/sentiment_by_category.png")

negative = df[df["Sentiment_Label"] == "Negative"]["Review Text"].str.lower()
words = []
for text in negative:
    words.extend(re.findall(r"\b[a-z]{4,}\b", str(text)))
stop = {"this", "that", "with", "have", "from", "they", "were", "been", "very", "just", "like", "dress", "would", "could"}
filtered = [w for w in words if w not in stop]
print("\n=== Top words in Negative reviews ===")
print(Counter(filtered).most_common(15))

df.to_csv("data/reviews_with_sentiment.csv", index=False)
summary.to_csv("data/category_summary.csv")
print("\nAll results saved.")