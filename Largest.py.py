# -*- coding: utf-8 -*-
"""Untitled18.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vZfP8mOmvvSDdnQd_BAiH-Sw8LFoqgHG
"""

!pip install -q streamlit

import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import pickle



#importing required libraries

import streamlit as st



#adding a number input widget

num1 = st.number_input('Enter the first number : ')
num2 = st.number_input('Enter the first number : ')
num3 = st.number_input('Enter the first number : ')

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3


#displaying the largest number

st.write("The largest number is", largest)

"""
To run the app, either create an appname.py file with the above code using any text editor, or if you are using a jupyter notebook, you need to download your .ipynb notebook as a
Python
(.py) file and run the same using the "streamlit run appname.py" command. Once you run the command, the app will automatically open in your default browser.

view run code

"""
