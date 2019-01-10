#########################################
### List Comprehension and Generators ###
#########################################



# Create list comprehension: squares
squares = [i**2 for i in range(0,10)]



# Create a 5 x 5 matrix using a list of lists: matrix
matrix = [[col for col in range(0,5)] for row in range(0,5)]

# Print the matrix
for row in matrix:
    print(row)



################
# Conditionals #
################

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) > 6]

# Print the new list
print(new_fellowship)



# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) > 6 else '' for member in fellowship]

# Print the new list
print(new_fellowship)


###############################
# Dictionary Comprehensions ###
###############################

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member : len(member) for member in fellowship}

# Print the new list
print(new_fellowship)
