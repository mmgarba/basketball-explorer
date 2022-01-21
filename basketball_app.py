import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import base64

st.title("NBA Player Stats Explorer")

st.markdown(
    """This performs simple live web scraping of NBA player stats, and offers them to you, the user, for exploration. 
    Libraries used: pandas, streamlit, and base64. 
    Data source: [basketball-reference.com](https://www.basketball-reference.com/)
    """
)

st.sidebar.header("User features: ")

selected_year = st.sidebar.selectbox('Year', list(reversed(range(1950,2021))))


@st.cache 
def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_" + str(year) + "_per_game.html"
    html = pd.read_html(url, header=0)
    df = html[0]
    raw = df.drop(df[df.Age == "Age"].index)
    raw = raw.fillna(0)
    playerstats = raw.drop(['Rk', axis=1])
    return playerstats
playerstats = load_data(selected_year)

# Sidebar - Select Team

sorted_unique_team = sorted(playerstats.Tm.uniqie())
selected_team = st.sidebar.multiselect("Team", sorted_unique_team)

# Sidebar - Select Position


