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
            """001""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Year":
            """2024""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Semester":
            """Spring""",
        # -----------------------------------------------------------------------------------------------------------------------
        "project_name":
            """Analyzing Disaster Trends and Predicting Death Toll""",
        # -----------------------------------------------------------------------------------------------------------------------
        "Objective":
            """ 
            The first goal of this project is to analyze and understand disaster event statistics in comparison with world 
            development indicators by country since 2000. The second goal is to build a regression model that uses features 
            from each disaster event and world development indicators to predict the total death toll. This project will help 
            to understand how disasters impact rich and poor countries differently while also providing a methodology to aid 
            in future disaster management and response. The UN underscores the importance of understanding disaster risk through 
            key agendas like the SENDAI Framework for Disaster Risk Reduction (SFDRR).
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Dataset":
            """
            Two databases will be used, the Emergency Events Database (EM-DAT) and the World Bank’s World Development Indicators 
            Database. The EM-DAT contains tabular data with 15,573 rows of disaster events around the world from 2000 onward. 
            There are 46 columns in the dataset ranging from disaster type, region, start year and month, latitude and longitude, 
            magnitude, total damage, number affected, and total deaths. The dataset is comprehensive in providing basic 
            information about each disaster event. The World Bank’s World Development Indicators Database contains relevant 
            indicator statistics by country since 2000. These include statistics like GDP per Capita and infant mortality
            along with other technological and poverty indicators. The plan is to append the World Bank data to the disaster 
            data to place each disaster in the context of the given country’s economic, social, and health conditions. 
            Combining the datasets will allow for more grouping and aggregating and ultimately reveal more complicated patterns
            with disaster events. The World Bank Data will also add relevant features to predict the target variable of total 
            deaths in a regression model.  

            Dataset 1- Emergency Events Database: Disaster Data since 2000: 
            https://doc.emdat.be/docs/data-structure-and-content/emdat-public-table/

            Dataset 2- World Bank: World Development Indicators since 2000:
            https://databank.worldbank.org/indicator/NY.GDP.PCAP.CD/1ff4a498/Popular-Indicators#
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Rationale":
            """
            The rationale of this project is to provide a complex understanding of the impacts of past disasters around the 
            world and help countries stay prepared for disasters in the future.
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Approach":
            """
            I plan on approaching this capstone through several steps.  

            1. Finding data and data loading (Python)
            2. Data cleaning/wrangling and data analysis (R/Python) 
            3. Mapping and visualizations of analysis (R/Python) 
            4. Build/test models + feature engineering (ML with scikit-learn in Python)
            5. Produce final predictive results and combine them with historical results
 
            """,
        # -----------------------------------------------------------------------------------------------------------------------
        "Timeline":
            """
            This is a rough timeline for this project:  

            - (1 Weeks) Data Loading
            - (3 Weeks) Data Processing and Analysis
            - (2 Weeks) Visualizations and Mapping
            - (6 Weeks) Modeling + Feature Engineering 
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
            More challenges will exist in feature engineering and training an effective model.
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
