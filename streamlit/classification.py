import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

@st.cache
def load_data():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = pd.Series(iris.target, name='target')
    return X, y

df, target = load_data()

model = RandomForestClassifier()
model.fit(df, target)
st.title("Iris Flower Classification")
st.write("Input the features of the iris flower to classify its species.")
sepal_length = st.slider("Sepal Length (cm)", float(df.sepal length.min()), float(df.sepal length.max()), float(df.sepal length.mean()))
sepal_width = st.slider("Sepal Width (cm)", float(df.sepal width.min()), float(df.sepal width.max()), float(df.sepal width.mean()))
petal_length = st.slider("Petal Length (cm)", float(df.petal length.min ()), float(df.petal length.max()), float(df.petal length.mean()))
petal_width = st.slider("Petal Width (cm)", float(df.petal width.min   ), float(df.petal width.max()), float(df.petal width.mean()))        
input_data = pd.DataFrame({
    'sepal length (cm)': [sepal_length],
    'sepal width (cm)': [sepal_width],
    'petal length (cm)': [petal_length],
    'petal width (cm)': [petal_width]
})
prediction = model.predict(input_data)
species = ['setosa', 'versicolor', 'virginica']
if st.button("Classify"):
    st.write(f"The predicted species is: {species[prediction[0]]}")
st.write("Here is the dataset used for training:")
st.dataframe(df)    
st.write("You can adjust the sliders to input different values for classification.")
st.write("The model uses a Random Forest Classifier trained on the Iris dataset.")  
st.write("This app demonstrates how to use Streamlit for building a simple classification app.")
import streamlit as st
st.title("Iris Flower Classification App")
st.write("This app classifies iris flowers based on their features using a Random Forest Classifier
trained on the Iris dataset.")
st.write("Adjust the sliders to input the features of the iris flower and click 'Classify' to see the predicted species.")          
st.write("The app uses Streamlit to create an interactive web application for classification tasks.")
st.write("You can explore the dataset and see how the model performs with different inputs.")   
st.write("This app is a simple demonstration of using Streamlit for machine learning applications.")
st.write("You can also visualize the dataset and the model's predictions.")
st.write("The app is built using Streamlit, a powerful framework for creating data applications.")
