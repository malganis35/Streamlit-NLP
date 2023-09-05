import streamlit as st

from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

import dotenv
import os

# Define project directories and load environment variables from .env file
project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
dotenv_path = os.path.join(project_dir, '.env')
dotenv.load_dotenv(dotenv_path)

from dotenv import dotenv_values
config = dotenv_values(dotenv_path)

# Retrieve the Cognitive Services API key and endpoint from environment variables
cog_key = config["cog_key"]
cog_endpoint = config["cog_endpoint"]

# Get a client for your text analytics cognitive service resource
text_analytics_client = TextAnalyticsClient(endpoint=cog_endpoint,
                                            credentials=CognitiveServicesCredentials(cog_key))

# Function to predict sentiment
def predict_sentiment(text):
    
    # Prepare the input data for sentiment analysis
    list_theme = ['']*1
    count = 0
    list_theme[count] = {}
    list_theme[count]["id"] = "1"
    list_theme[count]["text"] = text

    # Perform sentiment analysis using the Azure Cognitive Service
    sentiment_scores = text_analytics_client.sentiment(documents=list_theme)
    compound_score = sentiment_scores.documents[0].score
    
    # Determine the sentiment and color based on the sentiment score
    if compound_score > 0.6:
        sentiment = "Positive 😊"
        color = "green"
    elif compound_score < 0.4:
        sentiment = "Negative 😡"
        color = "red"
    else:
        sentiment = "Neutral 😐"
        color = "black"
    return sentiment, compound_score, color

# Title of the application
st.title("Sentiment Analysis with Azure Cognitive Service")

# Text area for user input
user_input = st.text_area("Enter your text here in English:")

if user_input:
    # Predict sentiment
    sentiment, score, color = predict_sentiment(user_input)
    
    # Display the result with the appropriate text size and color
    st.markdown(f"<p style='font-size: 32px; color: {color};'>{sentiment} <span style='font-size: 18px; color: {color};'>({score:.2f})</span></p>", unsafe_allow_html=True)
    
    # Display the score on a scale from 0 to 1 with a progress bar
    st.write(f"Score: {score}")
    st.progress(score / 2 + 0.5)  # The progress bar displays the score on a scale from 0 to 1
