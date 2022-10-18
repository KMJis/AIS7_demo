import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import koreanize_matplotlib
import plotly.express as px 

st.set_page_config(
    page_title="Likelion AI School 자동차 연비 App",
    page_icon="🚗",
    layout="wide",
)

st.markdown("# 자동차 연비 🚗")
st.sidebar.markdown("# 자동차 연비 🚗")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"


@st.cache
def load_data():
    data = pd.read_csv(url)
    return data

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache)")

st.sidebar.header('검색')
selected_year = st.sidebar.selectbox('Year',
   list(reversed(range(data.model_year.min(),data.model_year.max())))
   )

# Sidebar - origin
sorted_unique_origin = sorted(data.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)

if selected_year > 0 :
   data = data[data.model_year == selected_year]

if len(selected_origin) > 0:
   data = data[data.origin.isin(selected_origin)]

st.dataframe(data)

st.line_chart(data["mpg"])

st.bar_chart(data["mpg"])

st.bar_chart(data["mpg"])

st.markdown("## sns")
fig, ax = plt.subplots()
sns.countplot(data=data, x="origin").set_title("origin 별 갯수")
st.pyplot(fig)

fig, ax = plt.subplots()
sns.violinplot(data=data, x="cylinders", y="mpg").set_title("cylinders 별 자동차 연비")
st.pyplot(fig)

fig, ax = plt.subplots()
sns.lineplot(data=data, x="weight", y="mpg",hue="origin").set_title("국가별 weight와 자동차 연비 관계")
st.pyplot(fig)

st.markdown("## plotly")
pxh = px.histogram(data, x="origin")
st.plotly_chart(pxh)

st.markdown("## subplots 3개")

fig, ax = plt.subplots(nrows=3, ncols=1,figsize=(30,30))

sns.barplot(data=data, x="origin", y="mpg",ax=ax[0]).set_title("origin 별 자동차 연비")

sns.boxplot(data=data, x="cylinders", y="mpg",ax=ax[1]).set_title("cylinders 별 자동차 연비")

sns.scatterplot(data=data, x="horsepower", y="mpg",ax=ax[2]).set_title("horsepower 와 자동차 연비 관계")

st.pyplot(fig)

