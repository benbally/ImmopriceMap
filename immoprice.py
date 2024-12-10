# Import the streamlit library

import streamlit as st


# Define two different pages for the USA Map and the Property Price Estimator

map_page = st.Page(
    page="pages/us_map.py",
    title="USA Map",
    icon=":material/map:",
    default=True
)

estimator_page = st.Page(
    page="pages/streamlitapp.py",
    title="Property Price Estimator",
    icon=":material/apartment:",
)


# Set up the navigation menu

pg = st.navigation([map_page, estimator_page])

st.logo("assets/immoprice_logo.png")


# Run the navigation menu

pg.run()
