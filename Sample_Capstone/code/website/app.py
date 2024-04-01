import streamlit as st
import os

# Create tabs
with st.sidebar:
    selected_tab = st.radio("Navigation", ["Tab 1", "Tab 2", "Tab 3"])

# Display content based on selected tab
if selected_tab == "Tab 1":
    st.title("General")
    st.write("This is the content of Tab 1.")

    # Plot 1: bar chart of deaths by year and region
    html_file_path = "/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/stacked_bar_chart_of_deaths_by_year_and_region.html" 
    if os.path.exists(html_file_path):
        with open(html_file_path, "r") as f:
            plotly_map_html = f.read()
        st.components.v1.html(plotly_map_html, width=800, height=600)
    else:
        st.error("HTML file not found. Please make sure it exists in the same directory as your app.py.")

    # Plot 2: Deaths Map with year slider
    html_file_path = "/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/deaths_map_with_year_slider" 
    if os.path.exists(html_file_path):
        with open(html_file_path, "r") as f:
            plotly_map_html = f.read()
        st.components.v1.html(plotly_map_html, width=800, height=600)
    else:
        st.error("HTML file not found. Please make sure it exists in the same directory as your app.py.")
        
elif selected_tab == "Tab 2":
    st.title("Temporal and Spatial Analysis")
    st.write("This is the content of Tab 2.")

    # Plot 1: Box plot of Affected by region
    html_file_path = "/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Boxplot_of_Total Affected_by_Region_(without outliers)" 
    if os.path.exists(html_file_path):
        with open(html_file_path, "r") as f:
            plotly_map_html = f.read()
        st.components.v1.html(plotly_map_html, width=800, height=600)
    else:
        st.error("HTML file not found. Please make sure it exists in the same directory as your app.py.")

        # Plot 2: Box plot of Cost by region
    html_file_path = "/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Boxplot_of_Total Damage, Adjusted (US$ (millions)_by_Region_(without outliers)" 
    if os.path.exists(html_file_path):
        with open(html_file_path, "r") as f:
            plotly_map_html = f.read()
        st.components.v1.html(plotly_map_html, width=800, height=600)
    else:
        st.error("HTML file not found. Please make sure it exists in the same directory as your app.py.")
    # Plot 3: Box plot of Deaths by region
    html_file_path = "/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Boxplot_of_Total Damage, Adjusted (US$ (millions)_by_Region_(without outliers)" 
    if os.path.exists(html_file_path):
        with open(html_file_path, "r") as f:
            plotly_map_html = f.read()
        st.components.v1.html(plotly_map_html, width=800, height=600)
    else:
        st.error("HTML file not found. Please make sure it exists in the same directory as your app.py.")

        # Plot 4: Box plot of Deaths by region (asia)
    html_file_path = "/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Boxplot_of_Total Deaths_by_Subregion(asia)_(without outliers)" 
    if os.path.exists(html_file_path):
        with open(html_file_path, "r") as f:
            plotly_map_html = f.read()
        st.components.v1.html(plotly_map_html, width=800, height=600)
    else:
        st.error("HTML file not found. Please make sure it exists in the same directory as your app.py.")

       # Plot 5: Box plot of Deaths by region (africa)
    html_file_path = "/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Boxplot_of_Total Deaths_by_Subregion(africa)_(without outliers)" 
    if os.path.exists(html_file_path):
        with open(html_file_path, "r") as f:
            plotly_map_html = f.read()
        st.components.v1.html(plotly_map_html, width=800, height=600)
    else:
        st.error("HTML file not found. Please make sure it exists in the same directory as your app.py.")

    

elif selected_tab == "Tab 3":
    st.title("World Bank")
    st.write("This is the content of Tab 3.")

