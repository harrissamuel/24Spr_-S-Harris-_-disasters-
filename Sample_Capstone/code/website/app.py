import streamlit as st
import os

# Function to display HTML file if exists
def display_html(html_file_path):
    if os.path.exists(html_file_path):
        with open(html_file_path, "r") as f:
            plotly_map_html = f.read()
        # Apply custom CSS to remove white space
        st.markdown(
            f"""
            <style>
                .stComponent.e1e1i5i31 {{
                    width: 100%;
                    height: 100%;
                    margin: 0;
                    padding: 0;
                }}
            </style>
            """,
            unsafe_allow_html=True,
        )
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

    st.write("The following bar chart shows significant deaths by year and region. Specifcally, \
            it highlights large mass casualty events in both the Americas and Asia.")
    # Plot 1: Bar chart of deaths by year and region
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/stacked_bar_chart_of_deaths_by_year_and_region.html")

    st.write("Next, the following map shows disaster deaths by country and year. In addition, it highlights the disaster \
             type that caused the most deaths")

    # Plot 2: Deaths Map with year slider
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/deaths_map_with_year_slider")
        
elif selected_tab == "Tab 2":
    st.title("Temporal and Spatial Disaster Analysis")
    st.write("This is the content of Tab 2.")

    # Plot 1: Box plot of Affected by region
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Violinplot_of_Total Affected_by_Region_(without_outliers)")

    # Plot 2: Box plot of Cost by region
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Violinplot_of_Total Damage, Adjusted (US$ (millions)_by_Region_(without_outliers)")

    # Plot 3: Box plot of Deaths by region
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Violinplot_of_Total Deaths_by_Region_(without_outliers)")

    # Plot 4: Box plot of Deaths by region (asia)
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Violinplot_of_Total Deaths_by_Subregion(africa)_(without_outliers)")

    # Plot 5: Box plot of Deaths by region (africa)
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Violinplot_of_Total Deaths_by_Subregion(asia)_(without_outliers)")

    # Plot 6: Box plot of Deaths by region (americas)
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Violinplot_of_Total Deaths_by_Subregion(americas)_(without_outliers)")

    # Plot 7: Deaths by Month
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/disasters_by_month")

    # Plot 8: Lengths of Disaster
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/length_of_disaster_plot")

elif selected_tab == "Tab 3":
    st.title("World Bank Disaster Analysis")
    st.write("This is the content of Tab 3.")
    # Plot 1: Individual Variables with Death
    display_html('/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/Subplots_WB')

    # Plot 2: Disasters by Development Map
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/development_map_with_tab.html")

    # Plot 3: Deaths by Development Type and Disaster
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/bar_chart_with_development_category_and_disaster_type.html")

    # Plot 4: Timeline of Deaths by development Type
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/line_plot_with_start_year_and_development_category.html")

    # Plot 5: Number of disasters by development type
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/number_of_disaster_development_category.html")

    # Plot 6: Median Deaths by Development scores 
    display_html('/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/median_total_deaths_by_dev_score.html')

    # Plot 7: Risk Score
    display_html("/Users/samharris/Desktop/Capstone/24Spr_-S-Harris-_-disasters-/Sample_Capstone/code/website/risk_score_map.html")