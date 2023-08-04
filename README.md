# covid_data_project
Exploratory Data Analysis for Covid Data
Data Set from Kaggle:
https://www.kaggle.com/datasets/tohidkhanbagani/covid-19-deaths-and-vaccinations-dataset


## Data Overview

Data set provides information from 1/3/2020 to 4/12/2023 grouped by country about their performance through the pandemic tracking their infections, deaths, and vaccination data in addition to other economic indicators.

## EDA

Conducted EDA trying to gain a sense of which countries performed worse in the covid
pandemic based upon new cases smoothed per million.  "Smoothed" means a seven day average.  From the data set this allowed me to use a weekly average to calculate the intensity of new infections.  

![Alt text](<images\New Cases Per Million.png>)

This plot shows the severe spike in China following the reopening in late 2022 in addition to seasonal spikes in other parts of the world.  But infections are now the whole story, so I looked also at rate of deaths to identify significant comparisons.

![Alt text](<images\New Deaths Per Millionj.png>)

This plot shows a more complicated picture and I decided to look for correlations given the available data to find relationships between the total number of deaths per million and other indicators.  Here I build my initial hypothesis.

## Hypothesis Test and Linear Regression Model

H0: Vaccination rates do not lower the death rate in a country.

HA: An increase in vaccination rates lowers the death rate in a country.


![Alt text](<images\Total Deaths vs People Fully Vaccinated.png>)

I find in my hypothesis test and my linear regression model the following values:

Coefficient: 14.98
p-value: 0.012

This analysis suggests that a unit increase in vaccinations equates to a 14.98 increase in deaths.

However, the p-value of 0.012 suggests that I can reject the null hypothesis.

This contradictory evidence supports looking at other factors for analysis.

## Additional Analysis

I looked next to identify correlations between other factors related to covid deaths.

In full:

![Alt text](<images\Correlation Matrix Full.png>)

Reduced to relevent data fields. 

![Alt text](<images\Correlation Matrix Narrowed.png>)

A surprise in my analysis is that Total Deaths per Million was better predicted by other factors.

GDP:

![Alt text](<images\Deaths v GDP.png>)

Median Age:

![Alt text](<images\Total Deaths per Million vs. Median Age.png>)

Human Development Index:

![Alt text](<images\Total Deaths per Million vs. HDI.png>)

Life Expectancy:

![Alt text](<images\Total Deaths vs. Life Expectancy.png>)

Percent aged 65 or older:

![Alt text](<images\Total Deaths vs Percent Aged 65 or Older.png>)

There are strong correlations with all of these factors.  But median age, HDI, Life Expectancy, and 65+ populations, correlate with wealthier and older societies which were also more likely to receive vaccinations.

GDP:

![Alt text](<images\Vaccinated v GDP.png>)

Median age:

![Alt text](<images\Vaccinated v Median Age.png>)

Human Development Index:

![Alt text](<images\Vaccinated v HDI.png>)

Life Expectancy:

![Alt text](<images\Vaccinated v Life Expectancy.png>)

Percent aged 65 or older:

![Alt text](<images\Vaccinated v aged 65.png>)

## Conclusions

The linear regression model suggests that covid vaccines increased the rates of death.

However, vaccination rates are also consistent with higher deaths according to other factors.  Death rates and vaccination rates are both positively correlated with wealthier, more developed, and older societies.  This masks the relationship between vaccination rates and total deaths per million.

## Way Forward

Assess pandemic intensity overtime as opposed to the total may help to measure the effectiveness of country/regional responses.

Measure according to excess mortality may produce more accurate results given the likelihood of underreporting in poorer, less developed, or autocratic societies.

Missing from this data set is any data about the age of the dead.  Understanding this information would provide more nuance to vulnerable populations and determining how well countries responded to the pandemic.