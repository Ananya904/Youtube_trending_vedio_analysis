import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

# ------------------ TITLE ------------------
st.set_page_config(page_title="YouTube Analysis", page_icon="📊")
st.title(" YouTube Trending Videos Analysis")

# ------------------ LOAD DATA ------------------
@st.cache_data
def load_data():
    return pd.read_csv("trending_videos.csv")

df = load_data()
#st.write(df.columns)

# ------------------ DATA PREVIEW ------------------
st.subheader("Dataset Preview")
st.write(df.head())

# ------------------ SIDEBAR FILTER ------------------
st.sidebar.title("Filter")

if "country" in df.columns:
    selected_country = st.sidebar.selectbox(
        "Select Country",
        df["country"].unique()
    )
    df = df[df["country"] == selected_country]

# ------------------ VIEWS VS LIKES ------------------
st.subheader("Views vs Likes")

fig, ax = plt.subplots()
ax.scatter(df['view_count'], df['like_count'], alpha=0.3)
ax.set_xlabel("Views")
ax.set_ylabel("Likes")
ax.set_title("Views vs Likes")

st.pyplot(fig)

# ------------------ LOG-LOG PLOT ------------------
st.subheader("Log-Log Relationship (Views vs Likes)")

fig, ax = plt.subplots()
ax.scatter(df['view_count'], df['like_count'], alpha=0.3)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("Views (log)")
ax.set_ylabel("Likes (log)")
ax.set_title("Log-Log Plot")

st.pyplot(fig)

# ------------------ CATEGORY ANALYSIS ------------------
st.subheader("Category-wise Average Views")

if "category_name" in df.columns:
    category = df.groupby('category_name')['view_count'].mean()

    fig, ax = plt.subplots()
    category.plot(kind='bar', ax=ax)
    plt.xticks(rotation=45)
    ax.set_ylabel("Average Views")
    ax.set_title("Category Performance")

    st.pyplot(fig)

# ------------------ INSIGHTS ------------------
st.subheader("Key Insights")

st.markdown("""
-  Strong positive relationship between **views and likes**
-  Log-log plot shows **power-law distribution**
-  Category impacts video performance significantly
""")

# ------------------ FOOTER ------------------
st.markdown("---")
st.caption("Built with Streamlit | Data Source: Kaggle YouTube Trending Dataset")