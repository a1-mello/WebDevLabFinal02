# This creates the page for displaying data visualizations.

import streamlit as st
import json
import pandas as pd
import altair as alt


# PAGE CONFIGURATION
#graph from data.json
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)


# PAGE TITLE
st.title(":red[Data Visualizations 📈]")


# PART 1: GRAPHS FROM data.json
# --- YOUR CODE GOES HERE ---

with open("data.json", encoding="utf-8") as f:
    data = json.load(f)

df = pd.DataFrame(data["data_points"])
df = df.sort_values("passengers", ascending=False)


st.subheader(":blue[トップ 3 Top 3 Busiest Stations]")

col1, col2, col3 = st.columns(3)

col1.image("images/shinjuku.webp")
col1.markdown("#### 🥇 Shinjuku 新宿 🏙️")

col2.image("images/shibuya.webp")
col2.markdown("#### 🥈 Shibuya 渋谷 🍡🍥 ")

col3.image("images/ikebukuro.jpeg")
col3.markdown("#### 🥉 Ikebukuro 池袋 🛍️")



#static visual

st.subheader(":blue[Map of Japan's Busiest Train Stations]")
st.map(df)

#dynamic visual 

st.subheader(":blue[Busiest Stations by Daily Passengers]")

if "top_n" not in st.session_state:
    st.session_state.top_n = 10

st.slider("How many stations would you like to see?", 1, len(df), key="top_n")


shown = df.head(st.session_state.top_n)

chart = alt.Chart(shown).mark_bar().encode(
    x=alt.X("name", sort="-y", title="駅　Station"),
    y=alt.Y("passengers", title="　乗降客数　Daily Passengers"),
).properties(
    title="日本の駅の乗降客数/Daily Passengers at Japan's Busiest Stations",
    height=400,
    padding={"top": 20},
)

st.altair_chart(chart)


# PART 2: GRAPHS FROM data.csv
st.header(":red[Survey Results]")
survey = pd.read_csv("data.csv")

#Static
st.subheader(":blue[Favorite Way to Travel]")

transport_counts = survey["favorite_transport"].value_counts()
st.bar_chart(transport_counts)

#dynamic visual
st.subheader("blue[Favorite Cities by Commute Length]")

max_minutes = int(survey["commute_minutes"].max())

if "min_minutes" not in st.session_state:
    st.session_state.min_minutes = 0
st.slider("Minimum commute (minutes)", 0, max_minutes, key = "min_minutes")
filtered = survey[survey["commute_minutes"] >= st.session_state.min_minutes]

pie = alt.Chart(filtered).mark_arc().encode(
    theta = alt.Theta("count()", title = "Number of Responses"),
    color = alt.Color("favorite_city", title = "City"),
).properties(
    title = "Favorite Cities Among People With Longer Commutes",
    height = 400
)
st.altair_chart(pie)

#Extra Credit

mean_2 = filtered["commute_minutes"].mean()
median_2 = filtered["commute_minutes"].median()

if "prev_mean_2" not in st.session_state:
    st.session_state.prev_mean_2 = mean_2
    st.session_state.prev_median_2 = median_2

col_c, col_d = st.columns(2)
col_c.metric("Mean Commute (min) 平均", int(mean_2), int(mean_2 - st.session_state.prev_mean_2))
col_d.metric("Median Commute (min) 中央値", int(median_2), int(median_2 - st.session_state.prev_median_2))

st.session_state.prev_mean_2 = mean_2
st.session_state.prev_median_2 = median_2

