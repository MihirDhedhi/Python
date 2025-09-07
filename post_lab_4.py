from functools import reduce

my_list = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, my_list)
print("Product of all items in the list:", product)




my_list = [10, 25, 4, 75, 23]
largest_number = max(my_list)
print("Largest number in the list:", largest_number)




my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(dict.fromkeys(my_list))
print("List after removing duplicates:", unique_list)





my_list = ['a', 'b', 'a', 'c', 'b', 'a']
frequency = {item: my_list.count(item) for item in set(my_list)}
print("Frequency of elements:", frequency)





list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_items = list(set(list1) & set(list2))
print("Common items:", common_items)




my_list = [1, 2, 3, 4]
single_integer = int(''.join(map(str, my_list)))
print("Single integer:", single_integer)
