####################
## Exploring Data ##
####################

# Diagnosing Data that needs to be cleaned:

# Common Data Problems:
# -Inconsistent column names
# -Missing data
# -Outliers
# -Duplicate Rows
# -Untidy
# -Need to process columns
# -Column types can signal unexpected data values



######################
## Inspect the Data ##
######################

# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings_subset.csv')

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Print the head and tail of df_subset
print(df_subset.head())
print(df_subset.tail())

# Print the info of df
print(df.info())

# Print the info of df_subset
print(df_subset.info())



#######################
## Describe the Data ##
#######################

# For numerical data
print(df.describe())

# Print the value counts for 'Borough'
print(df['Borough'].value_counts(dropna=False))

# Print the value_counts for 'State'
print(df['State'].value_counts(dropna=False))

# Print the value counts for 'Site Fill'
print(df['Site Fill'].value_counts(dropna=False))
