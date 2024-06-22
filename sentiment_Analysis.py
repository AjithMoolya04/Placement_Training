from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)

    # Get polarity and subjectivity
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity

    # Determine sentiment
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, polarity, subjectivity

text = input("Enter text to analyze sentiment: ")
sentiment, polarity, subjectivity = analyze_sentiment(text)
print(f"Sentiment: {sentiment}")
print(f"Polarity: {polarity}")
print(f"Subjectivity: {subjectivity}")