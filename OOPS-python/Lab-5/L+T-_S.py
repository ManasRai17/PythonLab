integer_list = [1, 2, 3, 4, 5]
integer_tuple = (6, 7, 8, 9, 10)

string_list = list(map(str, integer_list))

string_tuple = list(map(str, integer_tuple))

combined_strings = string_list + string_tuple

print("List of integers:", integer_list)
print("Tuple of integers:", integer_tuple)
print("Combined list of strings:", combined_strings)
