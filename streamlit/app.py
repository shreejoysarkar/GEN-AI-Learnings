import streamlit as st
import pandas as pd
import numpy as np

## title of application

st.title("My First Streamlit App")

## DISPLAY A SIMPLE TEXT

st.write("Hello, welcome to my app!")

## DISPLAY A DATAFRAME  
df = pd.DataFrame({
    'Column 1': np.random.randn(10),
    'Column 2': np.random.randn(10)
})

st.write("Here is a sample dataframe:")
st.write(df)

# create line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)
