def find_largest_number(numbers):
    if len(numbers) == 0:
        print("The list is empty.")
        return None

    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number

    return largest
numbers = input("Enter a list of numbers (space-separated): ").split()
numbers = [int(num) for num in numbers]
largest_number = find_largest_number(numbers)
if largest_number is not None:
    print("The largest number in the list is:", largest_number)
