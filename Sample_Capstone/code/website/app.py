import streamlit as st
import os

# Function to display HTML file if exists
def display_html(html_file_name):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    html_file_path = os.path.join(current_directory, html_file_name)
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
    selected_tab = st.radio("Navigation", ["Overview", "Temporal and Spatial Exploratory Analysis", "World Bank"])

# Display content based on selected tab
if selected_tab == "Overview":
    st.title("Contextualizing Disasters: Analyzing Disaster Events by Development")
    st.subheader("Introduction and Objective:")

    st.write("Since 2000, 1.7 million deaths have occurred from disaster events around the world. \
             Often, disasters are overlooked as random events that wreak havoc on populations and are uncontrollable. \
             However, despite disasters being almost impossible to entirely prevent due to their inherent randomness, \
             disasters' impact on population can be mitigated through effective response, recovery, and preparedness efforts.")
    
    st.write( "This analysis aims to combine world disaster event data with World Bank country indicator data \
             to place historical disasters events in a given country's developmental context. \
             Understanding historical disasters by their type, impact, and development level is crucial \
             to gain information about how different disasters affect different countries. From this information, \
             officials can set goals for disaster management and adequately assess disaster risk comparatively by country. \
             The goal of this analysis is to mitigate disasters' impact by increasing awareness about disasters and providing relevant resources \
             to disaster management officials.")
    
    st.subheader("Datasets:")

    st.write("Two datasets are used in this analysis: the Emergency Events Database (EM-DAT) and the World Bank’s World Development Indicators Database. \
            The EM-DAT contains tabular data with 15,573 rows of disaster events around the world from 2000 onward. \
            There are 46 columns in the dataset ranging from disaster type, region, start year and month, latitude and longitude, magnitude, \
            total damage, number affected, and total deaths. The dataset is comprehensive in providing basic information about each disaster event. \
            The World Bank’s World Development Indicators Database contains relevant indicator statistics by country since 2000. Statistics used in this analysis \
            include GDP per Capita, infant mortality rate, life expectancy, electricity percentage, and tonnes of CO2 emitted. \
            These statistics were chosen because they give a good overview of a given country's development while also being widely available for almost every country. \
            Combining the World Bank data with the disaster data places each disaster event in the context of the \
            given country’s economic, technological, and health conditions.")
    
    st.subheader("EM DAT Data:")


    st.write("To get an idea about how we can use the EM DAT data to visualize disasters impact, consider the bar chart below which shows \
            deaths by year and region. Specifcally, \
            it highlights large mass casualty years in both the Americas and Asia.")
    # Plot 1: Bar chart of deaths by year and region
    display_html("stacked_bar_chart_of_deaths_by_year_and_region.html")

    st.write("Next, we can take it a step further and create an interactive map showing disaster deaths by country and year. In addition, the map highlights the disaster \
             type that caused the most deaths in a given year.")

    # Plot 2: Deaths Map with year slider
    display_html("deaths_map_with_year_slider")

    st.write("The map represents a good way to parse the EM DAT data spatially and temporally. Before combining the \
             the EM DAT data with the world bank indicator variables, let's further analyze the EM DAT data \
             spatially and temporally in the next section to better understand disaster events in the 21st century more broadly.")
        
elif selected_tab == "Temporal and Spatial Exploratory Analysis":
    st.title("Spatial Anlaysis:")
    st.write("To visualize the impact of disasters spatially, it still could be useful to show total deaths by reigon. \
             However, due to outlier disaster events (like the 2004 Boxing Day Tsunami), these measures may be inflated to extent where they are not useful \
             for meausuring the typical disaster in the region. For this reason, violin/box plots are shown below \
             to visualize the distrubution of typical disasters (with major outliers dropped). ")
    
    st.write("The first plot shows \
             the number of total affected by reigon. \
             Asia particulary stands out with more disasters affecting large amounts of people than any other reigon.")

    # Plot 1: Box plot of Affected by region
    display_html("Violinplot_of_Total Affected_by_Region_(without_outliers)")

    st.write("The next plot shows \
             the adjusted cost for disaster events by reigon. \
             The Americas and Europe in this case seem to have higher costs for disaster events. \
             However, because there are more than 10,000 missing values for cost, it is easy to determine that there is a bias in \
             in the data where only counties with insurance are reporting these cost statistics. Thus, cost will not be used \
             in further discussions about disaster events. ")
    
    # Plot 2: Box plot of Cost by region
    display_html("Violinplot_of_Total Damage, Adjusted (US$ (millions)_by_Region_(without_outliers)")

    st.write("Finally, the last plot by region shows the distribution of deaths in disaster events. We can see that Asia, Africa, and the Americas have the highest median disaster events. We break it down further by subregion next to learn more.")
    
    # Plot 3: Box plot of Deaths by region
    display_html("Violinplot_of_Total Deaths_by_Region_(without_outliers)")

    # Plot 4: Box plot of Deaths by region (asia)
    display_html("Violinplot_of_Total Deaths_by_Subregion(asia)_(without_outliers)")

    # Plot 5: Box plot of Deaths by region (africa)
    display_html("Violinplot_of_Total Deaths_by_Subregion(africa)_(without_outliers)")

    # Plot 6: Box plot of Deaths by region (americas)
    display_html("Violinplot_of_Total Deaths_by_Subregion(americas)_(without_outliers)")

    # Plot 7: Deaths by Month
    display_html("disasters_by_month")

    # Plot 8: Lengths of Disaster
    display_html("length_of_disaster_plot")

elif selected_tab == "World Bank":
    st.title("World Bank Disaster Analysis")
    st.write("Disaster analysis based on EM DAT Data and World Bank variables.")
    # Plot 1: Individual Variables with Death
    display_html("Subplots_WB")

    # Plot 2: Disasters by Development Map
    display_html("development_map_with_tab.html")

    # Plot 3: Deaths by Development Type and Disaster
    display_html("bar_chart_with_development_category_and_disaster_type.html")

    # Plot 4: Timeline of Deaths by development Type
    display_html("line_plot_with_start_year_and_development_category.html")

    # Plot 5: Number of disasters by development type
    display_html("number_of_disaster_development_category.html")

    # Plot 6: Median Deaths by Development scores 
    display_html("median_total_deaths_by_dev_score.html")

    # Plot 7: Risk Score
    display_html("risk_score_map.html")

