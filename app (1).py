# app.py
import streamlit as st

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Blog"])

# Home Page
if page == "Home":
    st.title("Welcome to My Portfolio!")
    st.write("Hi, I'm **sarah**, a passionate developer and data scientist.")
    st.write("This is my personal portfolio website where I showcase my work and share my thoughts.")
    
    st.header("Skills")
    st.write("- Python")
    st.write("- Machine Learning")
    st.write("- Web Development")
    st.write("- Data Visualization")

    st.header("Contact Me")
    st.write("Email: sara.123@example.com")
    st.write("LinkedIn: [Sara](www.linkedin.com/in/sararajput)")
    st.write("GitHub: [Sara](https://github.com/SaraRajput21)")

# Projects Page
elif page == "Projects":
    st.title("My Projects")
    st.write("Here are some of the projects I've worked on:")

    st.subheader("Project 1: Sentiment Analysis Tool")
    st.write("A machine learning model that analyzes the sentiment of text data.")
    st.write("Technologies: Python, TensorFlow, Streamlit")
    st.write("[GitHub Repo](https://github.com/SaraRajput21)")

    st.subheader("Project 2: Personal Finance Tracker")
    st.write("A web app to track personal expenses and income.")
    st.write("Technologies: Python, Flask, SQLite")
    st.write("[GitHub Repo](https://github.com/SaraRajput21)")

    st.subheader("Project 3: Weather Forecast App")
    st.write("A real-time weather forecasting app using OpenWeatherMap API.")
    st.write("Technologies: Python, Streamlit, API Integration")
    st.write("[GitHub Repo](https://github.com/SaraRajput21)")

# Blog Page
elif page == "Blog":
    st.title("My Blog")
    st.write("Welcome to my blog! Here, I share my thoughts on technology, programming, and more.")

    st.subheader("Post 1: Introduction to Machine Learning")
    st.write("In this post, I explain the basics of machine learning and its applications.")
    st.write("[Read More](#)")

    st.subheader("Post 2: Building a Streamlit App in 10 Minutes")
    st.write("A step-by-step guide to building a web app using Streamlit.")
    st.write("[Read More](#)")

    st.subheader("Post 3: Data Visualization with Python")
    st.write("Learn how to create stunning visualizations using Matplotlib and Seaborn.")
    st.write("[Read More](#)")