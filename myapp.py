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
with tab3:
    st.subheader(':gray[Data Types]')
    st.dataframe(data.types)
with tab4:
    st.subheader(':gray[Columns In Dataset]')
    st.dataframe(list(data.columns))
    #if not in dataframe then st.write(list(data.columns))

#visual Representation in the form of bar chart , line graph and bar chart
st.subheader(':rainbow[Data Visualization]',divider='gray')
with st.expander('Value Count'):
 cols1,cols2=st.columns(2)
 with cols1:
     column=st.selectbox('Choose Column Name',options=list(data.column))
 with cols2:
     toprows=st.number_input('Top_Rows',min_value=1,step=1)
     
count=st.button('Count')
if(count==True):
    result=data[column].value_counts().reset_index().head(toprows)
    st.dataframe(result)
    st.subheader('Visulaization',divider='gray')
    fig=px.bar(data_frame=result,x=column,y='count',text='count')
    st.plotly_chart(fig)
    fig=px.line(data_frame=result,x=column,y='count',text='count')
    st.plotly_chart(fig)
    fig=px.pie(data_frame=result,names=column,values='count')
    st.plotly_chart(fig)

#Group By 
# Group By
st.subheader(':rainbow[lets Have More detailed analysis]', divider='rainbow')
st.write('Categories Data')

with st.expander('Group By your columns'):
    col1, col2, col3 = st.columns(3)
    
    with col1:
        group_by = st.multiselect("Select the category to groupby", options=list(data.columns))
    with col2:
        operation_col = st.selectbox('Select column for operation', options=list(data.columns))
    with col3:
        operation = st.selectbox('Select operation', options=['sum', 'max', 'mean', 'min'])
    
    # Check that both group_by and operation_col are selected
    if group_by and operation_col:
        # Perform aggregation
        result = data.groupby(group_by).agg(
            newcol=(operation_col, operation)
        ).reset_index()
        
        st.dataframe(result)
        st.subheader('Visualization', divider='gray')
        
        # Use the first selected group_by column for the X-axis / categories
        x_axis = group_by[0]
        
        # Bar Chart
        fig_bar = px.bar(data_frame=result, x=x_axis, y='newcol', text='newcol', labels={'newcol': f'{operation.upper()} of {operation_col}'})
        st.plotly_chart(fig_bar, use_container_width=True)
        
        # Line Chart
        fig_line = px.line(data_frame=result, x=x_axis, y='newcol', text='newcol', labels={'newcol': f'{operation.upper()} of {operation_col}'})
        st.plotly_chart(fig_line, use_container_width=True)
        
        # Pie Chart
        fig_pie = px.pie(data_frame=result, names=x_axis, values='newcol', labels={'newcol': f'{operation.upper()} of {operation_col}'})
        st.plotly_chart(fig_pie, use_container_width=True)

    





