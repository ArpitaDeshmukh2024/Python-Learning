import numpy as np
def find_largest_number(arr):
    if arr.size == 0 :
        return None
    
    largest = np.max(arr)
    smallest = np.min(arr)
    return largest, smallest

my_array = np.array([12,45,9,74,23,208,88])
largest_number, smallest_number = find_largest_number(my_array)
print(f"Largest number is : {largest_number}")
print(f"Smallest number is : {smallest_number}")