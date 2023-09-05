from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials

import dotenv
import os

project_dir = os.path.join(os.path.dirname(__file__), os.pardir)
dotenv_path = os.path.join(project_dir, '.env')
dotenv.load_dotenv(dotenv_path)

from dotenv import dotenv_values
config = dotenv_values(dotenv_path)

cog_key = config["cog_key"]
cog_endpoint = config["cog_endpoint"]

# Get a client for your text analytics cognitive service resource
text_analytics_client = TextAnalyticsClient(endpoint=cog_endpoint,
                                            credentials=CognitiveServicesCredentials(cog_key))

list_theme = ['']*1
count = 0
list_theme[count] = {}
list_theme[count]["id"] = "1"
list_theme[count]["text"] = "I love you"

sentiment = text_analytics_client.sentiment(documents=list_theme)
sentiment.documents[0].score