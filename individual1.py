# Input list A of 10 items
A = []
for i in range(10):
    element = int(input(f"Enter element {i + 1}: "))
    A.append(element)

# Finding the smallest element
min_element = min(A)

# Finding the index of the smallest element
min_index = A.index(min_element)

# Swapping the smallest element with the last
A[min_index], A[-1] = A[-1], A[min_index]

# Output of the transformed array
print("Transformed Mas:")
print(A)