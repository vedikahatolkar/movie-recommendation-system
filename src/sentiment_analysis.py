def analyze_sentiment(text):

    positive_words = ["good", "great", "amazing", "excellent"]
    negative_words = ["bad", "boring", "worst"]

    score = 0

    for word in positive_words:
        if word in text.lower():
            score += 1

    for word in negative_words:
        if word in text.lower():
            score -= 1

    return score