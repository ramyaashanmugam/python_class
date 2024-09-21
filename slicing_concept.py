#list_name[start:end:step]


# List of numbers
numbers = [10, 20, 30, 40, 50, 60]


# Slicing from index 1 to 4 (4 is exclusive)
print(numbers[1:4])


# Slicing from the beginning to index 3
print(numbers[:3])
# Output: [10, 20, 30]

# Slicing from index 2 to the end
print(numbers[2:])
# Output: [30, 40, 50, 60]


# Slicing with negative indices
print(numbers[-4:-1])
# Output: [30, 40, 50]


# Slicing from the beginning to the second last element
print(numbers[:-1])
# Output: [10, 20, 30, 40, 50]


# Slicing the last three elements
print(numbers[-3:])
# Output: [40, 50, 60]


# Slicing with a step of 2 (every second element)
print(numbers[::2])
# Output: [10, 30, 50]

# Slicing with a step of 3
print(numbers[::3])
# Output: [10, 40]

# Reversing the list using slicing with a negative step
print(numbers[::-1])
# Output: [60, 50, 40, 30, 20, 10]


# Slicing from the start with step of 2
print(numbers[::2])
# Output: [10, 30, 50]

# Slicing from index 1 to the end with step of 2
print(numbers[1::2])
# Output: [20, 40, 60]



# Slicing from start to end without specifying start, end, or step
print(numbers[:])
# Output: [10, 20, 30, 40, 50, 60]

# Modifying elements of a list using slicing
numbers[1:3] = [25, 35]
print(numbers)
# Output: [10, 25, 35, 40, 50, 60]

# Replacing a portion with fewer or more elements
numbers[1:4] = [100]
print(numbers)
# Output: [10, 100, 50, 60]



# Copying a list using slicing
numbers_copy = numbers[:]
print(numbers_copy)
# Output: [10, 100, 50, 60]
numbers_copy[1:4] = [100]
print(numbers_copy)
print(numbers)


# Nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Slicing the outer list
print(nested_list[1:])
# Output: [[4, 5, 6], [7, 8, 9]]

