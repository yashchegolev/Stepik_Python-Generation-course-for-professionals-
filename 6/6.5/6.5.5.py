def flip_dict(dict_of_lists):
    from collections import defaultdict
    result = defaultdict(list)
    for key in dict_of_lists:
        for item in dict_of_lists[key]:
            result[item].append(key)
    return result
