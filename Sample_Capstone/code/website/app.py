import streamlit as st
import os

# Function to display HTML file if exists
def display_html(html_file_path):
    if os.path.exists(html_file_path):
        with open(html_file_path, "r") as f:
            plotly_map_html = f.read()
        st.components.v1.html(plotly_map_html, width=800, height=600)
    else:
        st.error("HTML file not found. Please make sure it exists in the same directory as your app.py.")
        st.write("File not found:", html_file_path)  # Debug print

# Create tabs
with st.sidebar:
    selected_tab = st.radio("Navigation", ["Tab 1", "Tab 2", "Tab 3"])

# Display content based on selected tab
if selected_tab == "Tab 1":
    st.title("General")
    st.write("This is the content of Tab 1.")

    # Plot 1: Bar chart of deaths by year and region
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/stacked_bar_chart_of_deaths_by_year_and_region.html")

    # Plot 2: Deaths Map with year slider
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/deaths_map_with_year_slider")
        
elif selected_tab == "Tab 2":
    st.title("Temporal and Spatial Disaster Analysis")
    st.write("This is the content of Tab 2.")

    # Plot 1: Box plot of Affected by region
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Boxplot_of_Total Affected_by_Region_(without outliers)")

    # Plot 2: Box plot of Cost by region
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Boxplot_of_Total Damage, Adjusted (US$ (millions)_by_Region_(without outliers)")

    # Plot 3: Box plot of Deaths by region
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Boxplot_of_Total Deaths_by_Region_(without outliers)")

    # Plot 4: Box plot of Deaths by region (asia)
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Boxplot_of_Total Deaths_by_Subregion(africa)_(without outliers)")

    # Plot 5: Box plot of Deaths by region (africa)
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Boxplot_of_Total Deaths_by_Subregion(asia)_(without outliers)")

elif selected_tab == "Tab 3":
    st.title("World Bank Disaster Analysis")
    st.write("This is the content of Tab 3.")
    # Plot 1: Disasters by Development Map
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/development_map_with_tab.html")

    # Plot 2: Deaths by Development Type and Disaster
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/bar_chart_with_development_category_and_disaster_type.html")

    # Plot 3: Timeline of Deaths by development Type
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/bar_chart_with_start_year_and_development_category.html")