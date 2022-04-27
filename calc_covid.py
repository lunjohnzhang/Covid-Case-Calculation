import numpy as np
import pandas as pd

if __name__ == '__main__':
    cases = pd.read_csv("covid_confirmed_usafacts.csv")
    deaths = pd.read_csv("covid_deaths_usafacts.csv")
    # print(cases)

    start_date = '2022-01-01'
    end_date = '2022-04-16'

    total_cases = np.sum(cases[end_date].to_numpy()) - \
                  np.sum(cases[start_date].to_numpy())
    total_deaths = np.sum(deaths[end_date].to_numpy()) - \
                   np.sum(deaths[start_date].to_numpy())

    print(f"Total cases from {start_date} to {end_date}: {total_cases}")
    print(f"Total deaths from {start_date} to {end_date}: {total_deaths}")
