import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title = "Streamlit Playground",
    page_icon = "favicon.ico",
    layout = "centered",     # centered, wide
    initial_sidebar_state = "expanded",    # expanded, collapsed, auto
    menu_items = {
        "Get Help": "https://docs.streamlit.io/",
        "About": "Streamlit Playground"
    }
)

st.sidebar.title("Uber")

st.title('Uber pickups in NYC')
#st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
local_file_path = 'uber-raw-data-sep14.csv'

# Read the data into a pandas DataFrame
data_local = pd.read_csv(local_file_path)

@st.cache_data
def load_data(nrows, data_url):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
#data = load_data(10000, DATA_URL)
#data.to_csv('uber-raw-data-sep14.csv', index=False)
data = load_data(1000, local_file_path)

data_load_state.text("Done! (using st.cache_data)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)