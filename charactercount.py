# Get user input for the string
string = input("Enter a string: ")

# Initialize an empty dictionary to store the character counts
char_counts = {}

# Count the occurrences of each character in the string
for char in string:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

# Print the character counts
print("Character counts:")
for char, count in char_counts.items():
    print(f"{char}: {count}")
