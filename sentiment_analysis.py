# Imports necessary libraries needed for sentiment analysis 
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import pandas as pd

# Loads the English language model
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("spacytextblob")

# Function to clean and preprocess text
def clean_text(text):
    # Tokenize the text
    doc = nlp(text)
    # Remove stopwords and punctuation, and lowercase the tokens
    cleaned_tokens = [str(token.text).lower().strip() for token in doc if not token.is_stop and not token.is_punct]
    # Join the cleaned tokens back into a single string
    cleaned_text = " ".join(cleaned_tokens)
    return cleaned_text

# Function for sentiment analysis
def sentiment_analysis(cleaned_data):
    for key, value in cleaned_data.items():
        # Preprocess the text
        cleaned_text = clean_text(value)  
        doc = nlp(cleaned_text)
        # Displays the cleaned text
        print(f"\nReview: {key, cleaned_text}")  
        print(f"Sentiment: {doc._.blob.sentiment}")

# Reads the CSV file into a DataFrame
amazon_reviews = pd.read_csv("amazon_product_reviews.csv", sep=",")
# Removes nan values from "reviews.text" column
amazon_reviews = amazon_reviews.dropna(subset=["reviews.text"])
# Selects specific reviews
reviews_data = amazon_reviews["reviews.text"].iloc[[1, 20, 68, 167, 546, 902, 1678, 2599, 3456, 9876, 15623]]

# Performs sentiment analysis on "reviews_data"
sentiment_analysis(reviews_data)


# Loads the medium-sized English language model
nlp = spacy.load("en_core_web_md")

# Function to test similarity between 2 reviews
def similarity(one, two):
    similarity_score = nlp(one).similarity(nlp(two))
    return similarity_score

# Select two specific reviews for comparison
my_review_of_choice = amazon_reviews["reviews.text"][1]
my_second_review_of_choice = amazon_reviews["reviews.text"][687]

# Calculates and then displays the similarity score between the two processed reviews
print(f"\nReview 1: {my_review_of_choice}")
print(f"Review 2: {my_second_review_of_choice}")
print(f"Similarity score between the two reviews is: {similarity(my_review_of_choice, my_second_review_of_choice):.2f}")