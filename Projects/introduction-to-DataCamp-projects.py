###############################
## First Project on DataCamp ##
###############################

# A Jupyter notebook is a document that contains text cells (what you're reading right now) and code cells. What is special with a notebook is that it's interactive: You can change or add code cells, and then run a cell by first selecting it and then clicking the run cell button above ( ▶| Run ) or hitting ctrl + enter.

# Projects allow you to practice and apply the skills you've learned in the DataCamp courses. In each project you carry out an end-to-end analysis, on a real-world task, using real-world tools and workflows. The exception is this project, which is just an introduction to the DataCamp project interface.

# On the side, you have a Jupyter notebook, a free, open-source web application that is great for interactive data analysis. A DataCamp project consists of a number of tasks, and here, you have the task instructions. Your first task is easy:

# I'm a code cell, click me, then run me!
256 * 60 * 24 # Children × minutes × hours
# Ouptut : 368640

# The Jupyter notebook in a DataCamp project will contain an analysis, data exploration, or other narrative combining code, data, and text. But, and here is the catch, some of the code is missing, and it's up to you to get it right! Sometimes you will only need to fix small things with the code, but in some projects, you will get to write a whole analysis yourself.

# However, in this project you won't have to do much — the notebook on the side is almost complete — there are just some minor issues that you need to deal with:


def greet(first_name, last_name):
    greeting = 'My name is ' + last_name + ', ' + first_name + ' ' + last_name + '!'
    return greeting

# Replace with your first and last name.
# That is, unless your name is already Kiko Mann.
greet('Kiko', 'Mann')

# Output : 'My name is Mann, Kiko Mann!'

# Importing the pandas module
import pandas as pd

# Reading in the global temperature data
global_temp = pd.read_csv('datasets/global_temperature.csv')

# Take a look at the first datapoints
global_temp.head()

# Setting up inline plotting using jupyter notebook "magic"
%matplotlib inline

import matplotlib.pyplot as plt

# Plotting global temperature in degrees celsius by year
plt.plot(global_temp['year'], global_temp['degrees_celsius'])

# Adding some nice labels 
plt.xlabel('Year') 
plt.ylabel('°C') 


# Making a map using the folium module
import folium
phone_map = folium.Map()

# Top three smart phone companies by market share in 2016
companies = [
    {'loc': [37.4970,  127.0266], 'label': 'Samsung: 20.5%'},
    {'loc': [37.3318, -122.0311], 'label': 'Apple: 14.4%'},
    {'loc': [22.5431,  114.0579], 'label': 'Huawei: 8.9%'}] 

# Adding markers to the map
for company in companies:
    marker = folium.Marker(location=company['loc'], popup=company['label'])
    marker.add_to(phone_map)

# The last object in the cell always gets shown in the notebook
phone_map