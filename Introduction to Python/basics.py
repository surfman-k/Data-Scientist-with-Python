############
## Basics ##
############

# Python created by Guido Van Rossum
# General Purpose language
# An extremely versatile language
# Learning V3.x as support for V2 will die over time
# Learning shell and script application of Python


# First Exercises are simple comments, printing, etc.

# Division
print(5 / 8)

# Addition
print(7 + 10)

# Suppose you have $100, which you can invest with a 10% return each year. After one year, it's 100×1.1=110 dollars, and after two years it's 100×1.1×1.1=121. Add code on the right to calculate how much money you end up with after 7 years.
# How much is your $100 worth after 7 years?
print(100 * 1.1 ** 7)

# Create a variable savings
savings = 100

# Print out savings
print(savings)

# Create a variable savings
savings = 100

# Create a variable growth_multiplier
growth_multiplier = 1.1

# Calculate result
result = savings * growth_multiplier ** 7

# Print out result
print(result)

# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)