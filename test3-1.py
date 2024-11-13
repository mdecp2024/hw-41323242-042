# Given values
v_i_kmh = 310          # initial velocity in km/h
d = 1000               # distance in meters
v_f = 0                # final velocity in m/s

# Convert initial velocity from km/h to m/s
v_i = v_i_kmh * 1000 / 3600

# Use the equation to calculate acceleration
a = (v_f**2 - v_i**2) / (2 * d)

# Output the result
print(f"The required constant acceleration is {a:.2f} m/s².")
