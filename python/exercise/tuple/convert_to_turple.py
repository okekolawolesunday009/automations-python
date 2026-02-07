# Two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Use zip to combine the lists
combined = zip(names, ages)

# Convert the zip object to a list to print the result
print(list(combined))

# Outputs: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]