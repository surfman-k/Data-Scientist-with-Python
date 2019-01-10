###########
## Loops ##
###########

# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print('correcting...')
    offset = offset - 1
    print(offset)

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0:
        offset = offset - 1
    else:
        offset = offset + 1
    print(offset)


###############
## For Loops ##
###############

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for ar in areas:
    print(ar)

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, a in enumerate(areas) :
    print('room ' + str(index) + ': ' + str(a))

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for list in house:
    print('the ' + str(list[0]) + ' is ' + str(list[1]) + ' sqm')


#############################
## Looping Data Structures ##
#############################

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for k, v in europe.items():
    print('the capital of ' + k + ' is ' + v)

# For loop over np_height
for x in np_height:
    print(str(x) + ' inches')

# For loop over np_baseball
for x in np.nditer(np_baseball):
    print(x)


#########################
## Looping Over Pandas ##
#########################

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(row['country'] + ': ' + str(row['cars_per_cap']))

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, 'COUNTRY'] = str(row['country']).upper()

# Use .apply(str.upper)
cars["COUNTRY"] = cars["country"].apply(str.upper)

