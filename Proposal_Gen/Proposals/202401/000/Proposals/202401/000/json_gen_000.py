#%%
import json
import os
import shutil

#%%

def save_to_json(data, output_file_path):
    with open(output_file_path, 'w') as output_file:
        json.dump(data, output_file, indent=2)

semester2code = { "sp":"01", "spr":"01", "spring":"01", "su":"02", "sum":"02", "summer":"02", "fa":"03", "fall":"03"}
thisfilename = os.path.basename(__file__) # should match _ver for version, ideally 3-digit string starting as "000", up to "999"

data_to_save = \
    {
        # -----------------------------------------------------------------------------------------------------------------------
        "Version":
            """000""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2024""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Spring""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Mapping and Predicting Natural Disasters and Their Cost""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The first goal of this project is to develop interactive map(s) of disaster data using FEMA (Federal Emergency
            Management Agency) time series data of over 4800+ data points labeled by state from 1953 to 2023. The second 
            goal is to merge the FEMA data with NOAA (National Oceanic and Atmospheric Administration) historical state 
            temperature and precipitation data and disaster cost data to build a predictive model. Ideally, two predictive 
            models will use features from historical climate data to try and predict disaster classification and 
            disaster cost. The mapping of historical data and effective predictive models will help state officials use 
            predicted climate data to produce relevant disaster risk predictions. The main objective is for this project to 
            underscore past disasters while also helping officials make data-driven preparations for future climate disasters.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
           At this initial stage, three US government datasets will be used: time series data containing individual natural 
           disasters from FEMA, tabular data containing average temperature and precipitation statistics by state from the NOAA, 
           and billion-dollar disaster cost data by state from the NOAA. The first dataset is “FEMA Web Disaster Declarations” 
           and contains “a list of FEMA declaration types and the types of assistance authorized.” More specifically, it has 
           4800 rows containing columns like ‘Disaster Name’, ‘Declaration Date,’ ‘Incident Type’, and ‘State Name.’ Dates span 
           from 1953 to 2023. This data will be foundational for initial exploratory data analysis and mapping of historical 
           disasters in the US by state. The second dataset is statewide NOAA climate data containing columns like temperature 
           and precipitation from 1895 to 2023. This data can be specified so it is by month and state. I plan to extract average 
           climate data from at least five different states every month since 1953. The next stage with this data is to merge it 
           with the FEMA dataset and obtain climate data matched with disaster data to build a predictive model for disaster type. 
           The initial idea is to use a random forest algorithm to build the classification model. Finally, the last dataset is 
           statewide NOAA disaster cost data which contains disaster cost data by month and year from 1980-2023. It also contains 
           columns for the name of the disaster and the type of disaster. Again, I plan to merge this data with the NOAA climate data 
           and obtain disaster cost data matched with climatic data to build a predictive model for disaster cost. The initial idea 
           is to use regression to build this predictive model for disaster cost. Links to the data can be found below.

           Dataset 1- Disaster Time Series: 
           https://www.fema.gov/openfema-data-page/fema-web-disaster-declarations-v1
           Dataset 2- Climatic Data: 
           https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/statewide/time-series/41/tavg/1/12/1895-2023
           Dataset 3- Disaster Cost Data:
           https://www.ncei.noaa.gov/access/billions/state-summary/TX
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
             The rationale of this project is to provide a complex understanding of past disasters in US states and help 
             specified states stay prepared for natural disasters in the future. This project should provide an idea 
             about the quantity of funds and resources that should be devoted to natural disasters as human-caused climate
             change continues. 
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps.  

            1. Data cleaning/wrangling and exploratory data analysis with FEMA data (R/Python) 
            2. Mapping and plotting FEMA data (R)   
            3. Data wrangling and cleaning to combine data sets (Python)
            4. Build/test models + feature engineering (ML with scikit-learn in Python)
            5. Produce final predictive results and combine them with historical results  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This a rough time line for this project:  

            - (2 Weeks) Data Processing and Analysis
            - (2 Weeks) Mapping and Plotting
            - (2 Weeks) Combine Datasets via Data Wrangling
            - (5 Weeks) Modeling + Feature Engineering 
            - (1 Weeks) Combining Results  
            - (1 Weeks) Writing Up a paper and submission
            - (1 Weeks) Final Presentation  

            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Expected Number Students":
            """
            The expected number of students is one.  
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Possible Issues":
            """
            The challenge will be data wrangling and effectively combining the datasets using dates and locations. 
            More challenges will exist in creating good predictive models since there are a limited number of 
            climatic features and these features are not guaranteed to be good predictors.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Proposed by": "Samuel Harris",
        "Proposed by email": "samharris@gwu.edu",
        "instructor": "Edwin Lo",
        "instructor_email": "edwinlo@gwu.edu",
        "github_repo": "https://github.com/harrissamuel/24Spr_-S-Harris-_-projectName-.git",
        # -----------------------------------------------------------------------------------------------------------------------
    }
os.makedirs(
    os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}',
    exist_ok=True)
output_file_path = os.getcwd() + f'{os.sep}Proposals{os.sep}{data_to_save["Year"]}{semester2code[data_to_save["Semester"].lower()]}{os.sep}{data_to_save["Version"]}{os.sep}'
save_to_json(data_to_save, output_file_path + "input.json")
shutil.copy(thisfilename, output_file_path)
print(f"Data saved to {output_file_path}")
