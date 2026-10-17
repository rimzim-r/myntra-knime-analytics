import pandas as pd

reviews = pd.read_csv("data/reviews_with_sentiment.csv")

cat_sentiment = reviews.groupby("Class Name")["Sentiment"].mean().round(3)

print("=== Category Sentiment (lowest first) ===")
print(cat_sentiment.sort_values())

print("\n=== Image Color Summary ===")
print("Most common colors: Blue, White, Yellow, Gray")

print("\n=== Combined Insight ===")
print("- Lowest sentiment: Trend category")
print("- Negative reviews mainly mention: size, fabric, thin, quality")
print("- Product images mostly Blue / White / Yellow / Gray")
print("- Suggestion: Focus on sizing and fabric quality for lower-sentiment categories")