from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):
    if by_values == False:
        for key in sorted(ordered_dict):
            ordered_dict.move_to_end(key)
    else:
        for key in sorted(ordered_dict, key=lambda x: ordered_dict[x]):
            ordered_dict.move_to_end(key)
