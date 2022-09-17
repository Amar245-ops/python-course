import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
# import dtale as dt

@st.cache
def load_database():
    df = pd.read_excel('ui/Canada.xlsx',
            sheet_name='Canada by Citizenship',
            skiprows=20,
            skipfooter=2)
    return preprocess(df)

def preprocess(df):
    cols_to_drop = ['Type','Coverage','AREA','REG','DEV']
    df.drop(columns=cols_to_drop, inplace=True)

    # step 2
    df.rename({
       'OdName': 'Country',
       'AreaName': 'Continent',
       'RegName': 'Region',
       'DevName': 'Status'
    },axis=1, inplace=True)

    # step 3
    df.columns = df.columns.astype(str)

    # step 4
    years = list(map(str,range(1980,2014))) # list of years
    df['Total'] = df[years].sum(axis=1)

    #step 5
    df.set_index('Country', inplace=True)
    
    return df

# loading the data
canadadf = load_database()

st.header("Canada Immigrations data analysis of 30 years")

if st.checkbox("View Raw Dataset"):
    st.write(canadadf)

menu_choices = ['Visualize Country Immigrants', 'Compare Countries','About']
choices = st.sidebar.radio('Select an option from the menu', menu_choices)
years = list(map(str,range(1980, 2014)))
if choices == menu_choices[0]:
    country_list = canadadf.index.tolist()
    country = st.selectbox('Select a country', country_list)
    graph = st.radio('Select a graph',['Bar Chart','Line Chart','Area Chart'],horizontal=True)
    
    data = canadadf.loc[country, years]
    if graph == 'Bar Chart':
        st.bar_chart(data)
    elif graph == 'Line Chart':
        st.line_chart(data)
    elif graph == 'Area Chart':
        st.area_chart(data)
    

elif choices == menu_choices[1]:
     country_list = canadadf.index.tolist()
     countries = st.multiselect('Select countries',country_list)
     if not len(countries)>= 1:
        st.warning('Please select select atleast one country')
     else:
        data = canadadf.loc[countries, years].T
        fig = px.line(data, x=years, y=countries, title="Comparing countries")
        st.plotly_chart(fig)
else:
    st.header("About")
    st.markdown('''
    ### this is a data analysis app for Canada
    - this data is from united states
    - its from the year 1980 to 2013
    - it contains 195 countries
    ''')