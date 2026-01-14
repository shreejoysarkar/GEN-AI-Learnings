import streamlit as st

st.title("text input")

name = st.text_input("Enter your name")

age = st.slider("Select your age", 0, 100, 25)

st.write(f"You are {age} years old.")

if name:
    st.write(f"Hello, {name}!")