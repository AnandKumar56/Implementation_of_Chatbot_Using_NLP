import os
import json
import datetime
import csv
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Ensure NLTK can download necessary resources
ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('punkt')

# Load intents.json file (ensure it's in the same directory as this script)
file_path = os.path.abspath("D://vs_code//Implementation_of_chatbot_using_NLP//intents.json")

try:
    with open(file_path, "r", encoding="utf-8") as file:
        intents = json.load(file)
except FileNotFoundError:
    st.error(f"Error: The intents.json file was not found at {file_path}. Please check the path.")
    intents = []

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer()
clf = LogisticRegression(random_state=0, max_iter=10000)

# Preprocess the data
tags = []
patterns = []
for intent in intents.get('intents', []):
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Train the model if data is available
if patterns and tags:
    X = vectorizer.fit_transform(patterns)
    y = tags
    clf.fit(X, y)

def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    for intent in intents.get('intents', []):
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "Sorry, I don't understand."

counter = 0

def main():
    global counter
    st.title("Chatbot")

    # Sidebar menu
    menu = ["Home", "Conversation History", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Define chat log file path
    chat_log_file = "chat_log.csv"

    # Home Menu
    if choice == "Home":
        st.write("Welcome to the chatbot. Type a message below:")

        if not os.path.exists(chat_log_file):
            with open(chat_log_file, 'w', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(["Timestamp", "User Input", "Bot Response"])

        user_input = st.text_input("You: ")
        if user_input:
            response = chatbot(user_input)
            st.write(f"Bot: {response}")

            # Log the conversation
            with open(chat_log_file, 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow([datetime.datetime.now(), user_input, response])

    # Conversation History Menu
    elif choice == "Conversation History":
        st.write("### Conversation History")
        if os.path.exists(chat_log_file):
            with open(chat_log_file, 'r', newline='', encoding='utf-8') as csvfile:
                csv_reader = csv.reader(csvfile)
                next(csv_reader)  # Skip the header row
                for row in csv_reader:
                    st.text(f"User: {row[1]}")
                    st.text(f"Chatbot: {row[2]}")
                    st.text(f"Timestamp: {row[0]}")
                    st.markdown("---")
        else:
            st.warning("No conversation history found.")

    # About Section
    elif choice == "About":
        st.write("### Intent-Based Chatbot using NLP and Logistic Regression")
        st.write("This chatbot uses Natural Language Processing (NLP) and Machine Learning to understand and respond to user queries.")

        st.subheader("How It Works:")
        st.write("""
        - **Data Collection**: The chatbot is trained on predefined intents stored in `intents.json`.
        - **NLP Processing**: It converts user input into numerical features using TF-IDF Vectorization.
        - **Classification**: The Logistic Regression model predicts the intent of the user input.
        - **Response Generation**: The chatbot selects a response based on the detected intent.
        """)

        st.subheader("Future Enhancements:")
        st.write("""
        - Integrate deep learning models for better responses.
        - Add more intents and responses to improve the chatbot's versatility.
        - Implement a feedback mechanism to learn from user interactions.
        """)

if __name__ == "__main__":
    main()
