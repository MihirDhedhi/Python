import pandas as pd
series1 = pd.Series([10, 20, 30, 40])
series2 = pd.Series([5, 10, 15, 20])
print("Addition:")
print(series1 + series2)
print("\nSubtraction:")
print(series1 - series2)
print("\nMultiplication:")
print(series1 * series2)
print("\nDivision:")
print(series1 / series2)





import pandas as pd
my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
series_from_dict = pd.Series(my_dict)
print(series_from_dict)




import pandas as pd
import numpy as np
my_list = [1, 2, 3, 4]
series_from_list = pd.Series(my_list)
print("Series from list:")
print(series_from_list)
my_array = np.array([10, 20, 30, 40])
series_from_array = pd.Series(my_array)
print("\nSeries from NumPy array:")
print(series_from_array)
my_dict = {'a': 100, 'b': 200, 'c': 300}
series_from_dict = pd.Series(my_dict)
print("\nSeries from dictionary:")
print(series_from_dict)




import pandas as pd
series1 = pd.Series([1, 2, 3], name='A')
series2 = pd.Series([4, 5, 6], name='B')
vertical_stack = pd.concat([series1, series2])
print("Vertically stacked series:")
print(vertical_stack)
horizontal_stack = pd.DataFrame({'Series A': series1, 'Series B': series2})
print("\nHorizontally stacked series:")
print(horizontal_stack)










