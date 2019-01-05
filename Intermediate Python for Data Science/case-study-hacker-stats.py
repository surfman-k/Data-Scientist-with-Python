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

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))