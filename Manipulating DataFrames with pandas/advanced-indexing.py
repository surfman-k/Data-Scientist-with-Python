####################################
## Index objects and labeled data ##
####################################

# Indexes do not support mutable operations!

# Create the list of new indexes: new_idx
new_idx = [str.upper() for str in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)


# Assign the string 'MONTHS' to sales.index.name
sales.index.name = 'MONTHS'

# Print the sales DataFrame
print(sales)

# Assign the string 'PRODUCTS' to sales.columns.name 
sales.columns.name = 'PRODUCTS'

# Print the sales dataframe again
print(sales)


# Building an Index, then a DataFrame

# Generate the list of months: months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# Assign months to sales.index
sales.index = months

# Print the modified sales DataFrame
print(sales)


###########################
## Hierarchical Indexing ##
###########################

# Print sales.loc[['CA', 'TX']]
print(sales.loc[['CA', 'TX']])

# Print sales['CA':'TX']
print(sales['CA':'TX'])
## Output:
    #              eggs  salt  spam
    # state month                  
    # CA    1        47  12.0    17
    #       2       110  50.0    31
    # TX    1       132   NaN    52
    #       2       205  60.0    55
    #              eggs  salt  spam
    # state month                  
    # CA    1        47  12.0    17
    #       2       110  50.0    31
    # NY    1       221  89.0    72
    #       2        77  87.0    20
    # TX    1       132   NaN    52
    #       2       205  60.0    55


## Sorting the MultiIndex

# Set the index to be the columns ['state', 'month']: sales
sales = sales.set_index(['state', 'month'])

# Sort the MultiIndex: sales
sales = sales.sort_index()

# Print the sales DataFrame
print(sales)


## Accessing Data with Non-Unique Indexes

# Set the index to the column 'state': sales
sales = sales.set_index(['state'])

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc['NY'])


### Indexing multiple levels of a MultiIndex

# Look up data for NY in month 1: NY_month1
NY_month1 = sales.loc[('NY', 1)]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[(['CA', 'TX'], 2), :]

# Look up data for all states in month 2: all_month2
all_month2 = sales.loc[(slice(None), 2), :]
