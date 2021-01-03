import streamlit as st
import numpy as np
import pandas as pd
import time
from PIL import Image
"""
# My First App
Here's our first attempt at using data to create a table:
"""
#data frame
df=(pd.DataFrame({
    'First Column':[1,2,3,4],
    'Second Column':[10,20,30,40]}))        
df
#chart data
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c'])
st.line_chart(chart_data)
#Map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [17.388, 78.476],
    columns=['lat', 'lon'])
st.map(map_data)
#Check box
if st.checkbox('Show Dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
    st.line_chart(chart_data)
#display image
image = Image.open("TomandJerry.jpg")
st.image(image,use_column_width=True)
#sidebar
option=st.sidebar.selectbox(
    'Which is you best number?',
    df['Second Column'])
'You selected: ',option
#Laying widgets side-by-side and hiding large content
left_column,right_column=st.beta_columns([2,5])
pressed=left_column.button('Press me?')
if (pressed):
    right_column.write('Woohoo!!!!')

expander=st.beta_expander('FAQ')
expander.write('Here you could put in some really, really long explanations...')
latest_iteration=st.empty()
bar=st.progress(0)
for i in range(1,100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'.... and now we\'re done!!!'