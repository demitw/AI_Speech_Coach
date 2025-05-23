from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def get_sentiment(text):
    result = sentiment_pipeline(text[:512])[0]
    return result['label'], result['score']
