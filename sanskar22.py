def read_file(filename):
    try:
        # Open the file
        with open(filename, 'r') as file:
            # Read the file line by line
            lines = file.readlines()

        # Combine the lines into a single string variable
        file_content = ''.join(lines)

        return file_content
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except IOError:
        print(f"Error reading file '{filename}'.")

# Prompt the user to enter the file path
filename = input("Enter the file path: ")

# Read the file and store its content in a variable
file_content = read_file(filename)

# Display the content of the file
if file_content is not None:
    print(f"The content of the file '{filename}' is:")
    print(file_content)
