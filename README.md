# Myntra Fashion Analytics

Python + KNIME project analyzing fashion product reviews (sentiment) and product images (color analysis).

## Python Analysis

### Sentiment Analysis
- Used TextBlob for polarity scoring
- Classified reviews as Positive / Neutral / Negative
- Category-wise average sentiment

### Key Findings
- Trend category has the lowest sentiment
- Negative reviews frequently mention: size, fabric, thin, quality
- Most categories have 80%+ positive reviews

### Image Analysis
- Downloaded 47 fashion product images
- Extracted dominant colors
- Most common colors: Blue, White, Yellow, Gray

## Files
- `python/nlp_analysis.py` — Sentiment analysis + visualization
- `python/image_analysis.py` — Image color analysis
- `python/combined_insights.py` — Combined summary
- `data/` — Datasets and results

## Screenshots
![Sentiment Chart](data/sentiment_by_category.png)
![KNIME Workflow](screenshots/knime_workflow.png)
![KNIME Bar Chart](screenshots/knime_barchart.png)

## How to Run
```bash
python -m pip install pandas textblob matplotlib pillow requests
python python/nlp_analysis.py
python python/image_analysis.py
python python/combined_insights.py