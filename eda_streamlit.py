import numpy as np
import pandas as pd
import streamlit as st 
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report



# web app title
st.markdown('''
 # **Exploratory Data Analysis web application**
  This app is developed by codanics youtube channel called **EDA app**
  ''')

# How to upload a file from PC

with st.sidebar.header("Upload your dataset(.csv)"):
    uploaded_file = st.sidebar.file_uploader("Upload your file", type=['csv'])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](https://raw.githubusercontent.com/tlemenestrel/GDP_and_Employment_Rates_Prediction/master/Employment_Rates_Prediction.csv)")
    
# Profiling report for pandas
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative=True)
    st.header('**Input Df**')
    st.write(df)
    st.write('---')
    st.header('**Profiling report with pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file')
    if st.button('Press to use example data'):
        #example dataset
        @st.cache_data   
        def load_data():
            a = pd.DataFrame(np.random.rand(100,5),
                             columns=['age','ball','cat','dog','elephant'])
            return a
        df = load_data()          
        pr = ProfileReport(df, explorative=True)
        st.header('**Input Df**')
        st.write(df)
        st.write('---')
        st.header('**Profiling report with pandas**')
        st_profile_report(pr)  