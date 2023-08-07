import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

def load_data():
    
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

    filtered_df = main_df[main_df['location_x'].isin(countries_of_interest)]

    
    
    return main_df


def visualize_new_cases_weekly_average():

    # Convert 'date' column to datetime format
    filtered_df['date'] = pd.to_datetime(filtered_df['date_x'])  
    
    # Set 'date' as the DataFrame's index
    filtered_df = filtered_df.set_index('date')  

    for country in countries_of_interest:
        country_data = filtered_df[filtered_df['location_x'] == country]
        plt.plot(country_data.index, country_data[column_to_plot], label=country)

    # Set plot title and labels
    plt.title('New Cases per Million Weekly Average')
    plt.xlabel('Date')
    plt.ylabel('New Cases per Million')

    # Customize the x-axis tick labels to show every week
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(15))  # Max 20 tick labels on the x-axis

    # Rotate the x-axis tick labels for better visibility
    plt.xticks(rotation=45)

    # Add a legend to distinguish the lines
    plt.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()

"""
Continue working here to get this code to work.  
Needs some significant troubleshooting.
"""

def main():

    #Call the load_data function to load data into data frames

    load_data()
    visualize_new_cases_weekly_average()

if __name__ == '__main__':
    main()
    