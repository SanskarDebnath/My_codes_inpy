import re
def count_lines_and_words(filename):
    line_count = 0
    word_count = 0
    try:
        with open(filename, 'r') as file:
            for line in file:
                line_count += 1
                words = re.findall(r"\b[\w'-]+\b", line)
                word_count += len(words)
        return line_count, word_count
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except IOError:
        print(f"Error reading file '{filename}'.")
filename = input("Enter the file path: ")
line_count, word_count = count_lines_and_words(filename)
if line_count is not None and word_count is not None:
    print(f"The file '{filename}' contains:")
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")