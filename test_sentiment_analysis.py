import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer1(self):
        self.assertEqual(sentiment_analyzer("I love working with Python")['label'],"SENT_POSITIVE")
    def test_sentiment_analyzer2(self):
        self.assertEqual(sentiment_analyzer("I hate working with Python")['label'],"SENT_NEGATIVE")
    def test_sentiment_analyzer3(self):
        self.assertEqual(sentiment_analyzer("I am neutral on Python")['label'],"SENT_NEUTRAL")

unittest.main()