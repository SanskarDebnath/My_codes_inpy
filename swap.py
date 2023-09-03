a = int(input("Enter the first element: "))
b = int(input("Enter the second element: "))
print("Before swapping:")
print("a:", a)
print("b:", b)
a = a - b
b = a + b
a = b - a
print("After swapping:")
print("a:", a)
print("b:", b)