# Coding Question

# Given a list of integers num_list containing numbers from 1 to N, where:

# One number is repeated twice.
# One number is missing.

# Write a Python function to:
# Identify the repeated number.
# Identify the missing number.
# Calculate and return the sum of the repeated and missing numbers.
# Example:
# num_list = [1, 1, 3, 4]

# Expected Output:
# Repeated number: 1
# Missing number: 2
# Sum: 3

def num(numlist):
    repeated = 0
    missing = 0

    for i in range(1, max(numlist) + 1):

        if numlist.count(i) > 1:
            repeated = i

        if numlist.count(i) == 0:
            missing = i

    sum = repeated + missing

    print("Repeated number:", repeated)
    print("Missing number:", missing)
    print("Sum:", sum)


num([1, 1, 3, 4])