import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="IPL 2024 Dashboard", layout="wide")

# Load data
df = pd.read_csv('ipl_batting_2024.csv')
df['Consistency'] = df['Runs'] / df['Matches']

# Sidebar filter
selected_players = st.sidebar.multiselect(
    "🎯 Select Players", df['Player'].unique(), default=df['Player'].unique())

filtered_df = df[df['Player'].isin(selected_players)]

# Main Tabs
tab1, tab2, tab3 = st.tabs(["🏏 Overview", "📊 Visualizations", "📋 Player Stats"])

# ---------------------- TAB 1: Overview ----------------------
with tab1:
    st.markdown("## 🏏 IPL 2024 Batting Overview")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Runs", f"{filtered_df['Runs'].sum()}")
    col2.metric("Avg Strike Rate", f"{filtered_df['SR'].mean():.2f}")
    col3.metric("Total Matches", f"{filtered_df['Matches'].sum()}")
    col4.metric("Avg Consistency", f"{filtered_df['Consistency'].mean():.2f}")

    st.markdown("---")
    st.markdown("### 🔥 Top 5 Run Scorers")
    top5 = filtered_df.sort_values(by='Runs', ascending=False).head(5)
    st.table(top5[['Player', 'Runs', 'SR', 'Matches']])

# ---------------------- TAB 2: Visualizations ----------------------
with tab2:
    st.markdown("## 📊 Visual Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🚀 Strike Rate vs Total Runs")
        fig1, ax1 = plt.subplots(figsize=(8,5))
        sns.scatterplot(data=filtered_df, x='SR', y='Runs', hue='Player', s=150, ax=ax1)
        ax1.set_xlabel("Strike Rate")
        ax1.set_ylabel("Runs")
        ax1.grid(True)
        st.pyplot(fig1)

    with col2:
        st.markdown("### 🎯 Top 5 Consistent Players")
        top_consistent = filtered_df.sort_values(by='Consistency', ascending=False).head(5)
        fig2, ax2 = plt.subplots(figsize=(8,5))
        sns.barplot(data=top_consistent, x='Consistency', y='Player', palette='coolwarm', ax=ax2)
        ax2.set_xlabel("Runs per Match")
        ax2.set_ylabel("Player")
        st.pyplot(fig2)

# ---------------------- TAB 3: Player Stats ----------------------
with tab3:
    st.markdown("## 📋 Player Statistics Table")
    st.dataframe(
        filtered_df[['Player', 'Matches', 'Runs', 'Balls', 'Avg', 'SR', '50s', '100s', 'Consistency']]
        .sort_values(by='Runs', ascending=False),
        use_container_width=True
    )
