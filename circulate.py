n = int(input("Enter the number of variables: "))
values = input("Enter the values separated by spaces: ").split()

circulated_values = values[1:] + [values[0]]
print("Circulated values:", " ".join(circulated_values))
