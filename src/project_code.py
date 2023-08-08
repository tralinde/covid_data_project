import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

def load_data():

    # This code provides the starting point for EDA and testing by combining data
    # and presenting it for use
        
    df_deaths = pd.read_csv('data/COVID DEATHS.csv')
    df_vaccines = pd.read_csv('data/COVID_VACCINATIONS.csv')

    merged_df = pd.merge(df_deaths, df_vaccines, left_index=True, right_index=True)

    columns_to_drop = ['iso_code_y', 'continent_y', 'location_y', 'date_y',
    'total_cases', 'new_cases', 'new_deaths',
    'total_cases_per_million', 'new_cases_per_million',
    'new_deaths_per_million',
    'icu_patients', 'hosp_patients', 'weekly_icu_admissions', 'weekly_hosp_admissions',
    'total_tests', 'new_tests', 'total_tests_per_thousand', 'new_tests_per_thousand',
    'new_tests_smoothed', 'new_tests_smoothed_per_thousand',
    'positive_rate', 'tests_per_case', 'tests_units',
    'total_boosters', 'new_vaccinations', 'new_vaccinations_smoothed',
    'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
    'total_boosters_per_hundred', 'new_vaccinations_smoothed_per_million',
    'new_people_vaccinated_smoothed', 'new_people_vaccinated_smoothed_per_hundred',
    'stringency_index', 'handwashing_facilities',
    'excess_mortality_cumulative_absolute', 'excess_mortality_cumulative']

    main_df = merged_df.drop(columns = columns_to_drop).copy()

    #Specify the countries to be considered for any analysis

    countries_of_interest = ['Brazil', 'China', 'United States', 'Russia', 'India']
    
    #Adjust dataframe to only consider the countries of interest.

    filtered_df = main_df[main_df['location_x'].isin(countries_of_interest)].copy()

    # Convert 'date' column to datetime format
    filtered_df.loc[:, 'date'] = pd.to_datetime(filtered_df['date_x']) 
    filtered_df = filtered_df.set_index('date')

    """
    filtered_df will provide information for the selected countries indexed by the date.  
    This means that all date is included from 1/3/2020 to 4/12/2023.  This contains
    several NaN values and so some columns are best considered taking a total value
    from the column, which will be done with later data.  Otherwise, filtered_df can 
    be used to consider data from a specific range of time
    """

    return filtered_df



# def visualize_new_cases_weekly_average(filtered_df):

#     """
#     This code will visualize initial stage of EDA which plots the new_cases_smoothed_per_million
#     column for the desired countries.  Countries of interest and desired column can be modified
#     here to adjust EDA.
#     """

#     # Convert 'date' column to datetime format
#     filtered_df['date'] = pd.to_datetime(filtered_df['date_x'])  
    
#     # Can be altered to change what it plotted
#     column_to_plot = 'new_cases_smoothed_per_million'

#     countries_of_interest = ['Brazil', 'China', 'United States', 'Russia', 'India']
    
#     # Set 'date' as the DataFrame's index
#     filtered_df = filtered_df.set_index('date')  

#     for country in countries_of_interest:
#         country_data = filtered_df[filtered_df['location_x'] == country]
#         plt.plot(country_data.index, country_data[column_to_plot], label=country)

#     # Set plot title and labels
#     plt.title('New Cases per Million Weekly Average')
#     plt.xlabel('Date')
#     plt.ylabel('New Cases per Million')

#     # Customize the x-axis tick labels to show every week
#     plt.gca().xaxis.set_major_locator(plt.MaxNLocator(15))  # Max 20 tick labels on the x-axis

#     # Rotate the x-axis tick labels for better visibility
#     plt.xticks(rotation=45)

#     # Add a legend to distinguish the lines
#     plt.legend()

#     # Show the plot
#     plt.tight_layout()
#     plt.show()

# def visualize_new_deaths_per_million_weekly(filtered_df):

#     #Setting up another variable here allows me to create a new visualization without breaking previous code
#     column_to_plot_a = 'new_deaths_smoothed_per_million'
#     countries_of_interest = ['Brazil', 'China', 'United States', 'Russia', 'India']

#     for country in countries_of_interest:
#         country_data = filtered_df[filtered_df['location_x'] == country]
#         plt.plot(country_data.index, country_data[column_to_plot_a], label=country)

#     # Set plot title and labels
#     plt.title('New Deaths per Million Weekly Average')
#     plt.xlabel('Date')
#     plt.ylabel('New Deaths per Million')

#     # Customize the x-axis tick labels to show every week
#     plt.gca().xaxis.set_major_locator(plt.MaxNLocator(15))  # Max 20 tick labels on the x-axis

#     # Rotate the x-axis tick labels for better visibility
#     plt.xticks(rotation=45)

#     # Add a legend to distinguish the lines
#     plt.legend()

#     # Show the plot
#     plt.tight_layout()
#     plt.show()

# def visualize_people_fully_vaccinated_percent(filtered_df):

#     #Setting up another variable here allows me to create a new visualization without breaking previous code
#     column_to_plot_b = 'people_fully_vaccinated_per_hundred'
#     countries_of_interest = ['Brazil', 'China', 'United States', 'Russia', 'India']

#     for country in countries_of_interest:
#         country_data = filtered_df[filtered_df['location_x'] == country]
#         plt.plot(country_data.index, country_data[column_to_plot_b], label=country)

#     # Set plot title and labels
#     plt.title('People Fully Vaccinated Percent')
#     plt.xlabel('Date')
#     plt.ylabel('Vaccinated Percent')

#     # Customize the x-axis tick labels to show every week
#     plt.gca().xaxis.set_major_locator(plt.MaxNLocator(15))  # Max 20 tick labels on the x-axis

#     # Rotate the x-axis tick labels for better visibility
#     plt.xticks(rotation=45)

#     # Add a legend to distinguish the lines
#     plt.legend()

#     # Show the plot
#     plt.tight_layout()
#     plt.show()

def narrow_dataframe(filtered_df):

    df_deaths = pd.read_csv('data/COVID DEATHS.csv')
    df_vaccines = pd.read_csv('data/COVID_VACCINATIONS.csv')

    merged_df = pd.merge(df_deaths, df_vaccines, left_index=True, right_index=True)

    columns_to_drop = ['iso_code_y', 'continent_y', 'location_y', 'date_y',
    'total_cases', 'new_cases', 'new_deaths',
    'total_cases_per_million', 'new_cases_per_million',
    'new_deaths_per_million',
    'icu_patients', 'hosp_patients', 'weekly_icu_admissions', 'weekly_hosp_admissions',
    'total_tests', 'new_tests', 'total_tests_per_thousand', 'new_tests_per_thousand',
    'new_tests_smoothed', 'new_tests_smoothed_per_thousand',
    'positive_rate', 'tests_per_case', 'tests_units',
    'total_boosters', 'new_vaccinations', 'new_vaccinations_smoothed',
    'total_vaccinations_per_hundred', 'people_vaccinated_per_hundred',
    'total_boosters_per_hundred', 'new_vaccinations_smoothed_per_million',
    'new_people_vaccinated_smoothed', 'new_people_vaccinated_smoothed_per_hundred',
    'stringency_index', 'handwashing_facilities',
    'excess_mortality_cumulative_absolute', 'excess_mortality_cumulative']

    main_df = merged_df.drop(columns = columns_to_drop).copy()
    
    narrow_df = main_df.groupby('location_x').agg({
    'total_deaths_per_million': max,
    'people_fully_vaccinated_per_hundred': max,
    'extreme_poverty': max,
    'aged_65_older': max,
    'aged_70_older': max,
    'gdp_per_capita': max,
    'life_expectancy': max,
    'human_development_index': max,
    'median_age': max
    })

    return narrow_df

def correlation_matrix(narrow_df):

    correlation_matrix = narrow_df.corr()

    # Create a heatmap to visualize the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Matrix')
    plt.show()

def main():

    # Call load_data function
    filtered_df = load_data()

    #visualize_new_cases_weekly_average(filtered_df)

    #visualize_new_deaths_per_million_weekly(filtered_df)

    #visualize_people_fully_vaccinated_percent(filtered_df)

    #narrow_df = narrow_dataframe(filtered_df)

    #correlation_matrix(narrow_df)

# Continue to work here, add testing and remaining plots


    
if __name__ == '__main__':
    
    main()
    