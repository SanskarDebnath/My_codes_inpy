def count_word_frequency(filename):
    word_frequency = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency
filename = input("Enter the file path: ")
frequency = count_word_frequency(filename)
for word, count in frequency.items():
    print(f'{word}: {count}')

#manual by sanskar : open it in any python folder say suppose i have a text file named sanskar.txt after run the python script in the python terminal simply write sanskar.txt
