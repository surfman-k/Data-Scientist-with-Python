# Case Study: Hacker Statistics

# Random Numbers

# Scenario :  
# We're walking up the Empire State Building and we're playing with a friend.
# We throw a die 100 times. If it falls on 1 or 2, we go one step down. If it's 3,4, or 5, we go one step up.
# If we get a 6, we throw it again and go up the corresponding amount of steps.
# We cannot go lower than step 0. We also have a 0.1% chance of falling down the stairs when we make a move.
# We bet that we will reach the 60th step. What are the odds that we will win this bet?

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice > 2 and dice < 6 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice, step)


# Initialize random_walk
random_walk = [0]

for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)


# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)

# Show the plot
plt.show()



# Visualizing multiple runs

# initialize and populate all_walks
all_walks = []
for i in range(10) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    all_walks.append(random_walk)

# Convert all_walks to Numpy array: np_aw
np_aw = np.array(all_walks)

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()