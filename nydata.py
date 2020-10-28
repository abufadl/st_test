import streamlit as st
import pandas as pd
import numpy as np

# title
st.title('Uber pickups in NYC')

st.write(f" Streamlit version:{st.__version__}")
# get data
DATE_COLUMN = 'date/time'
DATA_URL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz'

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
    
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

# display
if st.sidebar.checkbox('Show raw data'):
    st.subheader('Raw data')
    #write or magic interactive
    st.write(data)
    # custom style interactive
    st.dataframe(data.style.highlight_max(axis=0))
    # static table (all rows displayed)
    #st.table(data)

st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

st.subheader('Map of all pickups')
st.map(data)

# see also st.pydeck_chart
#hour_to_filter = 17 # hard coded
# use slider
hour_to_filter = st.sidebar.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

# widgets
x = st.sidebar.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# Add a selectbox to the sidebar:
how_contact = st.sidebar.selectbox(
    'Contact method:',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
my_range = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.beta_columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
