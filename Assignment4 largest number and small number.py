# Write a Python program to get the largest and smallest number from a list without builtin functions.

# Sample list
numbers = [95, 50, 30, 80, 4]

# Initialize 'largest' and 'smallest't
largest = numbers[0]
smallest = numbers[0]

# Iterate through the list to find the largest and smallest numbers
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Display the results
print("Largest number:", largest)
print("Smallest number:", smallest)