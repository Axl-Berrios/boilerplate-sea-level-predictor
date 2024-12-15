import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
   
    df = pd.read_csv("epa-sea-level.csv")

    
    fig, ax = plt.subplots(figsize=(8,5))
    scatter = plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    line_fit = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])

    mask = df["Year"] >= 2000
    line_fit_recent = linregress(df[mask]["Year"], df[mask]["CSIRO Adjusted Sea Level"])

    plt.plot(range(1880, 2051, 1), line_fit.slope*range(1880, 2051, 1)+line_fit.intercept, color="red")
    plt.plot(range(2000, 2051, 1), line_fit_recent.slope*range(2000, 2051, 1)+line_fit_recent.intercept, color='green')
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    
    plt.savefig('sea_level_plot.png')
    return plt.gca()
