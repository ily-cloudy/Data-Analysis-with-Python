import numpy as np
import pandas as pd

# numbers are arbitrarily rounded to one decimal place to pass testing; even when it does not comply with best practice. Additionally, some solutions are very bodged because i got bored. 

def calculate_demographic_data(print_data=True):
    # Read data from file
    
    df = pd.read_csv('adult.data.csv')
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    
    
    # What is the average age of men?
    average_age_men = round(df[['sex','age']][df['sex'] == 'Male']['age'].mean(), 1)
    
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(df['education'].value_counts()['Bachelors'] / len(df) * 100, 1)
    
    
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    
    # higher education and salary dataframe 
    hi_e_sal_df = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate'), ['education', 'salary']]
    
    # lower education and salary dataframe
    lo_e_sal_df = df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate'), ['education', 'salary']]
    
    # n of plp with higher education
    hi_e_int = np.sum(df['education'].value_counts()[['Bachelors','Masters','Doctorate']])
    
    # n of plp with low education
    lo_e_int = len(df) - hi_e_int 
    
    # number of higher education plp with sal >50K
    hi_e_rich_int = len(hi_e_sal_df[hi_e_sal_df['salary'] == '>50K'])
    
    # number of lower education plp with sal >50K
    lo_e_rich_int = len(lo_e_sal_df[lo_e_sal_df['salary'] == '>50K'])
    
    # return values
    higher_education_rich = round(hi_e_rich_int / hi_e_int * 100, 1)
    lower_education_rich = round(lo_e_rich_int / lo_e_int * 100, 1)
    
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])
    
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_worker_sal_df = df.loc[df['hours-per-week'] == min(df['hours-per-week']), ['hours-per-week','salary']]
    min_worker_rich_int = len(min_worker_sal_df[min_worker_sal_df['salary'] == '>50K'])
    
    rich_percentage = min_worker_rich_int / len(min_worker_sal_df) * 100
    
    
    # What country has the highest percentage of people that earn >50K?
    country_rich_series = df.loc[df['salary'] == '>50K', ['native-country']].value_counts().sort_index()
    
    countries_list = []
    for i, v in country_rich_series.items():
        country = i[0]
        countries_list.append(country)  
    
    country_ppl_series = df['native-country'].value_counts().sort_index()[countries_list]
    
    country_earning_percent_array = country_rich_series.to_numpy() / country_ppl_series.to_numpy() * 100
    
    highest_percentage_index_int = np.where(country_earning_percent_array == max(country_earning_percent_array))[0][0]
    
    highest_earning_country = countries_list[highest_percentage_index_int]
    highest_earning_country_percentage = round(country_earning_percent_array[highest_percentage_index_int], 1)
    
    
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K'), 'occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
