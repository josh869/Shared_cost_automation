#Importing relevent libraries for analysis.
import pandas as pd
import numpy as np

def run_analysis(file_name):
    #Import the data into pandas
    df = pd.read_excel(file_name)

    #Grouping by the date and name column to get a clear picture of the data. This also sorts the data as well.
    df1 = df.groupby(['Date', 'Name']).sum(numeric_only = True).reset_index().loc[:,['Date','Name','Morning_trips','Night_trips']]

    #Grouping data by the 'name' column to facilitate the computation of shared costs among individuals.
    df1 = df1.groupby('Name').sum(numeric_only = True).drop(columns = 'Date')

    #Hard cooding the amount to be shared amongst the individuals.
    df1['total_cost'] = 450

    #Calculate the morning and evening costs per trip by simple divisions.
    df1['am_cost'] = round(df1['total_cost']/df1['Morning_trips'])
    df1['pm_cost'] = round(df1['total_cost']/df1['Night_trips'])

    #Calculating the total cost for each individual by simple addition.
    df1['total_individual_cost'] = df1['am_cost'] + df1['pm_cost']

    #Replaceing infinity values within the DataFrame resulting from division by zero.
    df1.replace(np.inf, 0, inplace = True)

    #Saving the outpus of the analysis into excel as the task has been completed
    with pd.ExcelWriter('output1.xlsx') as writer:
        df1.to_excel(writer, sheet_name = 'sheet1')
