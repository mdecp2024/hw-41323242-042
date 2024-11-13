import math

# Given values
P0 = 100           # initial population
P_target = 50000    # target population
T = 3              # doubling time in hours

# Calculate time using the formula
t = T * math.log(P_target / P0, 2)

# Output the result
print(f"The population will first reach {P_target} after {t:.2f} hours.")