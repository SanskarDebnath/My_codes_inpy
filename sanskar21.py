def read_first_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            lines = [next(file) for _ in range(n)]
        return lines
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except IOError:
        print(f"Error reading file '{filename}'.")
filename = input("Enter the file path: ")
n = int(input("Enter the number of lines to read: "))
lines = read_first_n_lines(filename, n)
if lines is not None:
    print(f"The first {n} lines of the file '{filename}' are:")
    for line in lines:
        print(line, end='')