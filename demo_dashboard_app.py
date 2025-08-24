import streamlit as st
import pandas as pd
import numpy as np
import time

df = pd.DataFrame({
    'c1': [1, 2, 3, 4],
    'c2': [1, 4, 9, 16]
})


###### * Writing Tables to the app

# * Global table variables
n_cols = 10
n_rows = 5

st.write("Dynamic dataframe using st.write()")
st.write(df)

st.write("Static tabl using st.table()")
st.table(df)

st.write("Using st.dataframe() on random sample")
df = np.random.randn(n_rows,n_cols)
st.dataframe(df)

st.write("Using st.dataframe() with Pandas Styler object on random sample")
df = pd.DataFrame(
    np.random.randn(n_rows, n_cols),
    columns=['col %d' %i for i in range(n_cols)]
)
st.dataframe(df.style.highlight_max(axis=0))


##### * Writing Charts and Maps to app

# * Global chart variables
n_cols_line_df = 3
n_rows_line_df = 20

n_cols_map_df = 2
n_rows_map_df = 1000

st.write("Line Chart")
line_chart_df = pd.DataFrame(
    np.random.randn(n_rows_line_df, n_cols_line_df),
    columns=[f'col {i}' for i in range(n_cols_line_df)]
)
st.line_chart(line_chart_df)

st.write("Map")
map_df = pd.DataFrame(
    np.random.randn(n_rows_map_df, n_cols_map_df) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(map_df)


##### * Writing Widgets to app

# * Global widget variables


st.write("Slider")
x = st.slider('x')
st.write(x, 'squared is', x * x)

# Accessing widgets by key
st.write("Accessing widget by key")
st.text_input("Your name", key="name")
st.session_state.name


##### * Showing and Hiding data on app

# * Global collapsable section variables
n_cols_conditional_df = 3
n_rows_conditional_df = 20

st.write("Show or hide a dataframe")
if st.checkbox('Show Dataframe'):
    conditional_df = pd.DataFrame(
        np.random.randn(n_rows_conditional_df,n_cols_conditional_df),
        columns=['a', 'b', 'c']
    )
    
    conditional_df
    
st.write("Select from a series")
option = st.selectbox(
    'which number do you like best?',
    df.iloc[:, 0]
)

# Render literal to app
'You selected: ', option


##### * Layout

# * Global Layout variables

st.write("Buttons/Columns")
# Sidebar content
sidebar_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

sidebar_slider = st.sidebar.slider(
    'select a range of values',
    min_value=0.0, 
    max_value=100.0,
    value=(25.0, 75.0)
)

# Columns
left_column, right_column = st.columns(2)

left_column.button('Left column button')

# Add content within a specific column
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")


##### * Progress Bar

# * Global Layout variables
sleep_time = .1


latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    # Update progress bar with each iteration
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(sleep_time)