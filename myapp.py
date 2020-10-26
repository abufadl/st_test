import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title('My first app')
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# chart
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

#map
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

#widgets
if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
    
"""
# My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# place in sidebar
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

st.sidebar.markdown("""
## My great app
"""
)
#st.sidebar.slider(0,10) # error sytax?

#columns
left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("You pressed my neighbor!")
    pressed = False
 else:
    right_column.write("Dare you press my neighbor!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")
