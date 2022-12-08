
#### LOCAL APP
#### Sentiment analysis application

#### Import packages
import streamlit as st
from textblob import TextBlob


#### Add header to describe app
st.markdown("# Sentiment Analysis Application!!")

#### Create text input box and save incoming text to variable called text
text = st.text_input("Enter text:", value = "Enter text here")

#### TextBlob to analyze input text
score = TextBlob(text).sentiment.polarity

#### Create label (called sent) from TextBlob polarity score to use in summary below
if score > .15:
    label = "Positive"
elif score < -.15:
    label = "Negative"
else:
    label = "Neutral"
    
##### Show results

#### Print sentiment score, label, and language
st.markdown(f"Sentiment label: **{label}**")

