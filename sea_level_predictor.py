import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

filepath = "/home/runner/boilerplate-sea-level-predictor-1/epa-sea-level.csv"

def draw_plot():
    # Read data from file
    data = pd.read_csv(filepath,
                      header=0,
                      na_values=['']) # Fill blanks with NaN
    # to check data type of specific column
    # print(data['NOAA Adjusted Sea Level'].dtypes)
    # print(data)
    year = data['Year'].values
    # print(year.dtype)
    # np_year = year.values
    # print(year)
    csiro = data['CSIRO Adjusted Sea Level'].values
    # print(csiro.dtype)
    # np_csiro = csiro.values
    # print(csiro)

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    # Create scatter plot
    ax.scatter(year,csiro)
    # Create first line of best fit
  
    # Linear regression: used to fit a predictive model to an observed data set of values of       the response and explanatory variables
    # involves dependant & independant variables
    years_from_start_extended = np.arange(year[0],2051,1)
    linreg_1 = linregress(year, csiro)
    line_1 = [linreg_1.slope*xi + linreg_1.intercept for xi in years_from_start_extended]
    ax.plot(years_from_start_extended, line_1, color="tab:orange")


    # Create second line of best fit
    years_from_2000_extended = np.arange(2000, 2051,1)
    years_from_2000 = np.arange(2000,year[-1]+1,1)
    i = np.where(year == 2000)[0][0]
    # slice from start and end of years_from_2000
    csiro_slice = csiro[i:]
    # print(len(years_from_2000))
    # print(csiro_slice)
    linreg_2 = linregress(years_from_2000, csiro_slice)
    line_2 = [linreg_2.slope*xi + linreg_2.intercept for xi in years_from_2000_extended]
    ax.plot(years_from_2000_extended, line_2, color="tab:red")
    
  
    # Add labels and title
    ax.set_xticks(np.arange(1850.0, 2100.0, 25))
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    ax.set_title("Rise in Sea Level")

    ax.set_xlim([year[0],2050])
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    # print("Displaying plot:")
    # print(open("scatter.png", "rb").read())
    return plt.gca()