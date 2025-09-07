import numpy as np
x = np.arange(2, 11).reshape(3, 3)
print(x)




import numpy as np
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print(reversed_arr)




import numpy as np
array1 = np.array([1, 2, 3, 4, 5, 6])
array2 = np.array([4, 5, 6, 7, 8, 9])
common_values = np.intersect1d(array1, array2)
print("The common values are:", common_values)



import numpy as np
arr = np.array([1, 2, 3])
repeated_arr = np.repeat(arr, 2)
print(repeated_arr)




import numpy as np
arr = np.array([10, 20, 30, 40, 50], dtype=np.int64)
total_memory = arr.size * arr.itemsize
print(f"Total memory size: {total_memory} bytes")




import numpy as np
ones_array = np.ones((2, 3))
print("Array of ones:")
print(ones_array)
zeros_array = np.zeros(5)
print("\nArray of zeros:")
print(zeros_array)




import numpy as np
arr = np.arange(1, 10)
print("Original array:", arr)
fourth_element = arr[3]
print("The 4th element is:", fourth_element)




