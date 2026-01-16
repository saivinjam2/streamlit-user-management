import streamlit as st
st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit application.")
x = st.text_input("Enter some text:")
st.write("You entered:", x)
