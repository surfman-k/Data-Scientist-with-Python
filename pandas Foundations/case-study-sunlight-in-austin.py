#####################################
## Case Study - Sunlight in Austin ##
#####################################

# Comparing Observed weather data from two sources (both from the National Oceanic & Atmospheric Administration)
# - Austin, TX from 1981 to 2010
# - Austin, TX Weather Data from 2011

# Import pandas
import pandas as pd

# Read in the data file: df
df = pd.read_csv(data_file)

# Print the output of df.head()
print(df.head())

# Read in the data file with header=None: df_headers
df_headers = pd.read_csv(data_file, header=None)

# Print the output of df_headers.head()
print(df_headers.head())


