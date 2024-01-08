# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 12:16:25 2024

@author: uresha
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def dataset():
    """
     Read and return the data File
     """
    raw_data = pd.read_csv('Sustainable Energy.csv')
    return raw_data

raw_data=dataset()

#Check the Quality of the data set
#To get a summary of data set 

raw_data.info()
raw_data.describe()

#Return the number of missing values in dataset

raw_data.isnull().sum()

#Copy of dataset
data = raw_data.copy()

column_names_mapping = {
    'Time': 'Year',
    'Total electricity output (GWh) [4.1.1_TOTAL.ELECTRICITY.OUTPUT]': 'Total electricity output (GWh)',
    'Renewable energy consumption (TJ) [3.1_RE.CONSUMPTION]': 'Renewable energy consumption (TJ)',
    'Access to electricity (% of rural population with access) [1.2_ACCESS.ELECTRICITY.RURAL]': 'Access to electricity (% of rural population)',
    'Access to electricity (% of urban population with access) [1.3_ACCESS.ELECTRICITY.URBAN]': 'Access to electricity (% of urban population)',
    'Access to electricity (% of total population) [1.1_ACCESS.ELECTRICITY.TOT]': 'Access to electricity (% of total population)',
    'Energy intensity level of primary energy (MJ/2011 USD PPP) [6.1_PRIMARY.ENERGY.INTENSITY]': 'Energy intensity level of primary energy (MJ/2011 USD PPP)',
    'Renewable electricity output (GWh) [4.1.2_REN.ELECTRICITY.OUTPUT]':'Renewable electricity output (GWh)',
    'Renewable electricity share of total electricity output (%) [4.1_SHARE.RE.IN.ELECTRICITY]': 'Renewable electricity share of total electricity output (%)',
    'Renewable energy share of TFEC (%) [2.1_SHARE.TOTAL.RE.IN.TFEC]': 'Renewable energy share of TFEC (%)',
    'Total final energy consumption (TFEC) (TJ) [1.1_TOTAL.FINAL.ENERGY.CONSUM]':'Total final energy consumption (TJ)',
    'Access to Clean Fuels and Technologies for cooking (% of total population) [2.1_ACCESS.CFT.TOT]': 'Access to Clean Fuels and Technologies for cooking (% of total population)'
}

# Rename the columns using the dictionary
data = data.rename(columns=column_names_mapping)

# Overall electricity production capacity of the country
def elec_output(data, country = 'Country Name', year ='Year', output = 'Total electricity output (GWh)', colormap = 'Spectral'):
    """
    Bar graph to visualize total electricity output in countries year-wise.
    """
    # Pivot the DataFrame
    pivot_data = data.pivot_table(index = country, columns = year, values = output)

    # Plotting
    pivot_data.plot(kind='bar', stacked=False, figsize=(8, 6), colormap=colormap)

    # Add labels and title
    plt.xlabel('Countries')
    plt.ylabel('Total Electricity Output (GWh)')
    plt.title('Total Electricity Output by Country and Year', fontweight='bold', fontsize=12)

# Call the function with your DataFrame
elec_output(data)

########################################

def ren_energ_consum(data, variable_names='Renewable energy consumption (TJ)', colormap='BrBG'):
    
    # Pivot the data for plotting
    df = pd.DataFrame(data)
    df_pivot = df.pivot(index='Country Name', columns='Year')

    # Plot the stacked bar graph with the specified colormap
    fig, ax = plt.subplots()
    df_pivot[variable_names].plot(kind='barh', stacked=False, figsize=(8, 6), ax=ax, colormap=colormap)

    # Customize the plot
    plt.title('Renewable energy consumption of countries by years', fontweight='bold')
    plt.xlabel('Renewable Energy')
    plt.ylabel('Country')
    plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

# Call the function with the sample data and Set3 colormap
ren_energ_consum(data, colormap='BrBG')


def ren_elec_out(data, variable_names='Total final energy consumption (TJ)', colormap='PiYG'):
    
    # Pivot the data for plotting
    df = pd.DataFrame(data)
    df_pivot = df.pivot(index='Country Name', columns='Year')

    # Plot the stacked bar graph with the specified colormap
    fig, ax = plt.subplots()
    df_pivot[variable_names].plot(kind='barh', stacked=False, figsize=(8, 6), ax=ax, colormap=colormap)

    # Customize the plot
    plt.title('Total final energy consumption (TJ) of countries by years', fontweight='bold')
    plt.xlabel('Renewable Energy')
    plt.ylabel('Country')
    plt.legend(title='Year', bbox_to_anchor=(1.05, 1), loc='upper left')

# Call the function with the sample data and Set3 colormap
ren_elec_out(data, colormap='PiYG')

###################

def plot_pie_charts(data):
    # Filter data for the year 2012
    data_2012 = data[data['Year'] == 2010]

    # Filter specific countries (India, Japan, US, and UK)
    selected_countries = ['India', 'Japan', 'United States', 'United Kingdom']
    data_selected_countries = data_2012[data_2012['Country Name'].isin(selected_countries)]

    # Select relevant columns
    selected_columns = [
        'Access to electricity (% of rural population)',
        'Access to electricity (% of urban population)',
        'Access to electricity (% of total population)'
    ]

    # Set up subplots with a horizontal layout
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(8, 15))

    # Define custom colors for the pie charts
    custom_colors = ['#F66D44', '#FEAE65', '#AADEA7', '#2D87BB']

    # Plot each pie chart horizontally with larger font sizes and custom colors
    for i, col in enumerate(selected_columns):
        ax = axes[i]
        ax.pie(data_selected_countries[col], labels=data_selected_countries['Country Name'], autopct='%1.1f%%', startangle=90,
               counterclock=False, wedgeprops=dict(width=0.4), textprops=dict(fontsize=16), colors=custom_colors)
        ax.set_title(col, fontsize=18, fontweight='bold')

    # Add title to the full grid
    plt.suptitle('Access to Electricity Statistics by Country (2012)', fontsize=20, fontweight='bold', y=1.05)

    # Adjust layout
    plt.tight_layout()

# Assuming 'data' is your DataFrame
# Call the function with your data
plot_pie_charts(data)

#####

def plot_pie_charts(data):
    # Filter data for the year 2012
    data_2015 = data[data['Year'] == 2015]

    # Filter specific countries (India, Japan, US, and UK)
    selected_countries = ['India', 'Japan', 'United States', 'United Kingdom']
    data_selected_countries = data_2015[data_2015['Country Name'].isin(selected_countries)]

    # Select relevant columns
    selected_columns = [
        'Access to electricity (% of rural population)',
        'Access to electricity (% of urban population)',
        'Access to electricity (% of total population)'
    ]

    # Set up subplots with a horizontal layout
    fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(8, 15))

    # Define custom colors for the pie charts
    custom_colors = ['#C6D68F', '#9B3192', '#EA5F89', '#F7B7A3']

    # Plot each pie chart horizontally with larger font sizes and custom colors
    for i, col in enumerate(selected_columns):
        ax = axes[i]
        ax.pie(data_selected_countries[col], labels=data_selected_countries['Country Name'], autopct='%1.1f%%', startangle=90,
               counterclock=False, wedgeprops=dict(width=0.4), textprops=dict(fontsize=16), colors=custom_colors)
        ax.set_title(col, fontsize=18, fontweight='bold')

    # Add title to the full grid
    plt.suptitle('Access to Electricity Statistics by Country (2015)', fontsize=20, fontweight='bold', y=1.05)

    # Adjust layout
    plt.tight_layout()

# Assuming 'data' is your DataFrame
# Call the function with your data
plot_pie_charts(data)

############

def plot_energy_intensity(data, country='Country Name', variable='Energy intensity level of primary energy (MJ/2011 USD PPP)'):
    # Set up the line graph
    plt.figure(figsize=(12, 6))

    # Plotting the line graph for each country
    for year, year_data in data.groupby('Year'):
        plt.plot(year_data[country], year_data[variable], label=f'Year {year}')

    # Adding labels and title
    plt.xlabel(country, fontsize=13)
    plt.ylabel('MJ / 2011 USD PPP', fontsize=13)
    plt.title(f'{variable} by Year and Country', fontsize=15, fontweight='bold')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Year', fontsize=12)
    plt.grid(True)

    # Show the plot
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

# Assuming 'data' is your DataFrame
# Call the function with your data
plot_energy_intensity(data)

