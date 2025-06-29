import streamlit as st
import boto3

st.title("🧠 Sentiment Analyzer")

# Get AWS credentials from secrets.toml
aws_access_key = st.secrets["aws"]["aws_access_key_id"]
aws_secret_key = st.secrets["aws"]["aws_secret_access_key"]
region = st.secrets["aws"]["region"]

# Create AWS Comprehend client
comprehend = boto3.client(
    "comprehend",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=region
)

# User input
user_input = st.text_area("Enter text to analyze")

if st.button("Analyze Sentiment") and user_input:
    with st.spinner("Analyzing..."):
        response = comprehend.detect_sentiment(Text=user_input, LanguageCode="en")
        st.write("**Sentiment:**", response["Sentiment"])
        st.write("**Details:**", response["SentimentScore"])