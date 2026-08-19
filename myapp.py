#import files
import pandas as pd
import streamlit as st
import plotly.express as px

#for page configuration
st.set_page_config(
    page_title="Analytics Application",
    page_icon="🔍"
)
#tile
st.title(":rainbow[Data Analytics Portal]")
#header
st.subheader(":rainbow[Explore Your data set]",divider='rainbow')
#file upload
file=st.file_uploader("Add Your File here",type=['csv','xlsx'])

if(file!=None):
    if (file.name.ends_with('csv')):
        data=pd.read_csv(file)
    else:
        data=pd.read_excel(file)
#to show the file use
st.dataframe(data)
#to provide a message to end user
st.info('File is uploaded')

#statistical Summary of Data
st.subheader(":rainbow[Statistical Information of Data ]",divider="rainbow")
tab1,tab2,tab3,tab4=st.tabs(['Summary','Top and Bottom Rows','Data Types','Columns'])

with tab1:
    st.write(f'There are {data.shape[0]} rows in the dataset and {data.shape[1]} columns in the dataset')
    st.subheader(':gray[Statistical Summary of Data]')
    st.dataframe(data.describe())
with tab2:
    st.subheader(":gray[Top Rows]")
    toprows=st.slider('Number of First Few Rows',1,data.shape[0],key='topslider')
    st.dataframe(data.head(toprows))
    st.subheader(':gray[Bottom Rows]')
    bottomrows=st.slider('Number of Last few Rows',1,data.shape[0],key="bottomslider")
    st.dataframe(data.tail(bottomrows))