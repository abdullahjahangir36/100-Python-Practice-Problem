# The current population of a town is 10000. 
# The population of the town is increasing at the rate of 10% per year.
# You have to write a program to find out the population at the end of each of the last 10 years. 
# For eg current population is 10000 so the output should be like this:
# 10th year - 10000
# 9th year - 9000
# 8th year - 8100 and so on

def calculate_population(initial_population, growth_rate, years):
    populations = []
    current_population = initial_population
    # Calculate population for each year, going back from the current year
    for year in range(years, 0, -1):
        populations.append(current_population)
        current_population /= (1 + growth_rate / 100)
    return populations

def print_population(populations):
    for i, population in enumerate(populations, start=1):
        print(f"{i}th year - {int(population)}")

# Initial parameters:
initial_population = 10000
growth_rate = 10
years = 10

# Calculate and print the population for each year
populations = calculate_population(initial_population, growth_rate, years)
print_population(populations)
