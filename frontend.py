import streamlit as st
import boto3

# Set up Comprehend client
comprehend = boto3.client('comprehend')

st.title("🧠 Sentiment Analyzer")
st.subheader("Type a sentence and find out how it *feels*!")

# User input
user_input = st.text_area("Enter your text below:", height=150)

if st.button("Analyze Sentiment") and user_input:
    with st.spinner("Analyzing..."):
        response = comprehend.detect_sentiment(Text=user_input, LanguageCode='en')
        sentiment = response['Sentiment']
        st.success(f"Detected Sentiment: **{sentiment}**")
        st.json(response)