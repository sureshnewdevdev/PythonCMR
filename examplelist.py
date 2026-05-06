# Demonstrating various list operations in Python

import array;

# a=array.array()

# 1. An empty list
L1 = []
print("1. An empty list:", L1)

# 2. A list with four items (indexes 0 to 3)
L2 = [0, 1, 2, 3]
print("2. List with four items:", L2)

# 3. A nested list
L3 = ['abc', ['def', 'ghi']]
print("3. A nested list:", L3)

# 4. Creating a list from a string
L4 = list('spam')  # Converts each character of the string into a list item
print("4. List created from string 'spam':", L4)

# 5. Creating a list from a range of integers
L5 = list(range(-4, 4))  # List of integers from -4 to 3
print("5. List created from range(-4, 4):", L5)

# 6. Accessing an element by index
L6 = [10, 20, 30, 40]
print("6. Element at index 2 of L6:", L6[2])

# 7. Accessing an element from a nested list by index
L7 = ['x', [10, 20, 30], 'y']
print("7. Element at L7[1][2] (nested list):", L7[1][2])

# 8. Slicing a list
L8 = [0, 1, 2, 3, 4, 5]
print("8. Slicing L8 from index 2 to 4 (L8[2:5]):", L8[2:5])

# 9. Getting the length of a list
print("9. Length of L8:", len(L8))

# 10. Demonstrating nested indexing and slicing together
L9 = [10, [100, 200, 300, 400], 50]
print("10a. Element at L9[1]:", L9[1])  # Access the sublist
print("10b. Element at L9[1][3]:", L9[1][3])  # Access element 3 from the sublist
print("10c. Slicing sublist L9[1][1:3]:", L9[1][1:3])  # Slice the sublist

# Summary of outputs
print("\nSummary of Lists:")
print("L1:", L1)
print("L2:", L2)
print("L3:", L3)
print("L4:", L4)
print("L5:", L5)
print("L6:", L6)
print("L7:", L7)
print("L8:", L8)
print("L9:", L9)


# Basic useage of list

print(len([1, 2, 3]) )

combinedList = [1, 2, 3] + [4, 5, 6] 
print (combinedList)

sameValueList = ['abc'] * 4 
print (sameValueList)

print (str([1, 2]) + "34") # Same as "[1, 2]" + "34"
 
print([1, 2] + list("34")) # Same as [1, 2] + ["3", "4"]
[1, 2, '3', '4']

print(3 in [1, 2, 3]) # Membership

for x in [1, 2, 3]:
    print(x, end=' ') # Iteration

res = [c * 4 for c in 'SPAM'] # List comprehensions
res
# ['SSSS', 'PPPP', 'AAAA', 'MMMM']

