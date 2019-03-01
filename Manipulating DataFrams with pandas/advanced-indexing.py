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