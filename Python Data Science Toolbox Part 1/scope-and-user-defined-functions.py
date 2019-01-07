# Scope and User-Defined Functions

# Scopes: 
#   Global - defined in the main body of the script
#   Local - defined within a function
#   Built-in - in pre-defined built-in modules of Python

# Create a string: team
team = "teen titans"

# Define change_team()
def change_team():
    """Change the value of the global variable team."""

    # Use team in global scope
    global team

    # Change the value of team in global: team
    team = "justice league"
# Print team
print(team)

# Call change_team()
change_team()

# Print team
print(team)