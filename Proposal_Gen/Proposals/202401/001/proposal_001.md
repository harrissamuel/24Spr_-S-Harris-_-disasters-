
# Capstone Proposal
## Analyzing Disaster Trends and Predicting Death Toll
### Proposed by: Samuel Harris
#### Email: samharris@gwu.edu
#### Advisor: Edwin Lo
#### The George Washington University, Washington DC  
#### Data Science Program


## 1 Objective:  
 
            The first goal of this project is to analyze and understand disaster event statistics in comparison with world 
            development indicators by country since 2000. The second goal is to build a regression model that uses features 
            from each disaster event and world development indicators to predict the total death toll. This project will help 
            to understand how disasters impact rich and poor countries differently while also providing a methodology to aid 
            in future disaster management and response. The UN underscores the importance of understanding disaster risk through 
            key agendas like the SENDAI Framework for Disaster Risk Reduction (SFDRR).
            

## 2 Dataset:  

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
            

## 3 Rationale:  

            The rationale of this project is to provide a complex understanding of the impacts of past disasters around the 
            world and help countries stay prepared for disasters in the future.
            

## 4 Approach:  

            I plan on approaching this capstone through several steps.  

            1. Finding data and data loading (Python)
            2. Data cleaning/wrangling and data analysis (R/Python) 
            3. Mapping and visualizations of analysis (R/Python) 
            4. Build/test models + feature engineering (ML with scikit-learn in Python)
            5. Produce final predictive results and combine them with historical results
 
            

## 5 Timeline:  

            This is a rough timeline for this project:  

            - (1 Weeks) Data Loading
            - (3 Weeks) Data Processing and Analysis
            - (2 Weeks) Visualizations and Mapping
            - (6 Weeks) Modeling + Feature Engineering 
            - (1 Weeks) Combining Results  
            - (1 Weeks) Writing Up a paper and submission
            - (1 Weeks) Final Presentation  

            

## 6 Expected Number Students:  

            The expected number of students is one.  
            

## 7 Possible Issues:  

            The challenge will be data wrangling and effectively combining the datasets using dates and locations. 
            More challenges will exist in feature engineering and training an effective model.
            


## Contact
- Author: Edwin Lo
- Email: [edwinlo@gwu.edu](Eamil)
- GitHub: [https://github.com/harrissamuel/24Spr_-S-Harris-_-projectName-.git](Git Hub rep)
