#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import joblib
import numpy as np


# In[6]:


model = joblib.load('model.pkl')
st.title("House Price Prediction")

f1 = st.number_input("Enter House Size:",value=0.0)
f2 = st.number_input("Enter Bedrooms:",value=0.0)
f3 = st.number_input("Enter Bathrooms:",value=0.0)
f4 = st.number_input("Enter Age of House:",value=0.0)
f5 = st.number_input("Enter Distance to City:",value=0.0)

if st.button("Predict Price"):
    features = np.array([[f1,f2,f3,f4,f5]])
    prediction = model.predict(features)
    st.success(f"Predicted Pice: {prediction[0]:.2f}")
    
    


# In[ ]:





# In[ ]:




