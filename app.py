import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page Configuration
st.set_page_config(page_title="Wine Quality Analyzer", page_icon="🍷", layout="wide")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Overview", "Analysis & Visualization"])

# Load Dataset from Local File
def load_data():
    df = pd.read_csv("winequality-red.csv", sep=';')
    return df

# Home Page
if page == "Home":
    st.title("🍷 Wine Quality Analyzer")
    st.write("Analyze and visualize key metrics from a wine quality dataset.")
    st.image("https://picsum.photos/800/400", use_column_width=True)
    st.markdown("""
    ### Features
    - Quick overview of wine chemistry
    - Visualize relationships between variables
    - Identify patterns in quality and alcohol content
    """)
    st.image("https://picsum.photos/600/300")

# Data Overview Page
elif page == "Data Overview":
    st.title("Dataset Overview 📄")
    st.image("https://picsum.photos/800/300")

    df = load_data()

    st.write("### Preview")
    st.dataframe(df)

    st.write("### Summary Statistics")
    st.write(df.describe())

    st.write("### Correlation Matrix")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(df.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# Analysis and Visualization Page
elif page == "Analysis & Visualization":
    st.title("Data Analysis & Visualization 📊")
    st.image("https://picsum.photos/800/300")

    df = load_data()

    col_x = st.selectbox("Select X-axis", df.columns)
    col_y = st.selectbox("Select Y-axis", df.columns)
    hue = st.selectbox("Color by (hue)", [None] + list(df.columns))

    fig, ax = plt.subplots()
    if hue and hue != col_x and hue != col_y:
        sns.scatterplot(data=df, x=col_x, y=col_y, hue=hue, palette="viridis", ax=ax)
    else:
        sns.scatterplot(data=df, x=col_x, y=col_y, ax=ax)
    st.pyplot(fig)

    st.write("### Quality Distribution")
    fig2, ax2 = plt.subplots()
    sns.countplot(data=df, x="quality", palette="Set2", ax=ax2)
    st.pyplot(fig2)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("### Built with 🍷 using Streamlit")
