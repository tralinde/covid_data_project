# covid_data_project
Exploratory Data Analysis for Covid Data
Data Set from Kaggle:
https://www.kaggle.com/datasets/tohidkhanbagani/covid-19-deaths-and-vaccinations-dataset

This dataset contains two files that provide detailed information on Covid-19 deaths and vaccinations worldwide. The first file contains data on the number of Covid-19 deaths, including total deaths and new deaths, across different locations and time periods. The second file contains data on Covid-19 vaccinations, including total vaccinations, people vaccinated, people fully vaccinated, and total boosters, across different locations and time periods. By analyzing this data, you can uncover insights into the global impact of Covid-19 and explore the relationship between vaccinations and deaths. This dataset is a valuable resource for researchers, data analysts, and anyone interested in understanding the ongoing pandemic.

COVID DEATHS

iso_code: The ISO 3166-1 alpha-3 code of the country or territory.
continent: The continent of the location.
location: The name of the country or territory.
date: The date of the observation.
population: The population of the country or territory.
total_cases: The total number of confirmed cases of Covid-19.
new_cases: The number of new confirmed cases of Covid-19.
new_cases_smoothed: The 7-day smoothed average of new confirmed cases of Covid-19.
total_deaths: The total number of deaths due to Covid-19.
new_deaths: The number of new deaths due to Covid-19.
new_deaths_smoothed: The 7-day smoothed average of new deaths due to Covid-19.
total_cases_per_million: The total number of confirmed cases of Covid-19 per million people.
new_cases_per_million: The number of new confirmed cases of Covid-19 per million people.
new_cases_smoothed_per_million: The 7-day smoothed average of new confirmed cases of Covid-19 per million people.
total_deaths_per_million: The total number of deaths due to Covid-19 per million people.
new_deaths_per_million: The number of new deaths due to Covid-19 per million people.
new_deaths_smoothed_per_million: The 7-day smoothed average of new deaths due to Covid-19 per million people.
reproduction_rate: The estimated average number of people each infected person infects (the "R" number).
icu_patients: The number of patients in intensive care units (ICU) with Covid-19 on the given date.
icu_patients_per_million: The number of patients in intensive care units (ICU) with Covid-19 on the given date, per million people.
hosp_patients: The number of patients in hospital with Covid-19 on the given date.
hosp_patients_per_million: The number of patients in hospital with Covid-19 on the given date, per million people.
weekly_icu_admissions: The weekly number of patients admitted to intensive care units (ICU) with Covid-19.
weekly_icu_admissions_per_million: The weekly number of patients admitted to intensive care units (ICU) with Covid-19, per million people.
weekly_hosp_admissions: The weekly number of patients admitted to hospital with Covid-19.
weekly_hosp_admissions_per_million: The weekly number of patients admitted to hospital with Covid-19, per million people.
COVID VACCINATIONS

total_tests: The total number of tests for Covid-19.
new_tests: The number of new tests for Covid-19.
total_tests_per_thousand: The total number of tests for Covid-19 per thousand people.
new_tests_per_thousand: The number of new tests for Covid-19 per thousand people.
new_tests_smoothed: The 7-day smoothed average of new tests for Covid-19.
new_tests_smoothed_per_thousand: The 7-day smoothed average of new tests for Covid-19 per thousand people.
positive_rate: The share of Covid-19 tests that are positive, given as a rolling 7-day average.
tests_per_case: The number of tests conducted per confirmed case of Covid-19, given as a rolling 7-day average.
tests_units: The units used by the location to report its testing data.
total_vaccinations: The total number of doses of Covid-19 vaccines administered.
people_vaccinated: The total number of people who have received at least one dose of a Covid-19 vaccine.
people_fully_vaccinated: The total number of people who have received all doses prescribed by the vaccination protocol.
total_boosters: The total number of booster doses administered (doses administered after the prescribed number of doses for full vaccination).
new_vaccinations: The number of doses of Covid-19 vaccines administered on the given date.
new_vaccinations_smoothed: The 7-day smoothed average of new doses of Covid-19 vaccines administered.
total_vaccinations_per_hundred: The total number of doses of Covid-19 vaccines administered per hundred people in the total population.
people_vaccinated_per_hundred: The total number of people who have received at least one dose of a Covid-19 vaccine per hundred people in the total population.
people_fully_vaccinated_per_hundred: The total number of people who have received all doses prescribed by the vaccination protocol per hundred people in the total population.
total_boosters_per_hundred: The total number of booster doses administered per hundred people in the total population.
new_vaccinations_smoothed_per_million: The 7-day smoothed average of new doses of Covid-19 vaccines administered per million people in the total population.
stringency_index: A composite measure based on nine response indicators including school closures, workplace closures, and travel bans, rescaled to a value from 0 to 100 (100 = strictest).
population_density: The number of people divided by land area, measured in square kilometers.
median_age: The median age of the population, UN projection for 2020.