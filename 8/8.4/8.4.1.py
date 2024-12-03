def recursive_sum(nested_lists):
    if type(nested_lists) != list:
        return nested_lists
    else:
        total = 0
        for item in nested_lists:
            total += recursive_sum(item)
        return total 
    
my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(recursive_sum(my_list))
    
my_list = []
print(recursive_sum(my_list))    
