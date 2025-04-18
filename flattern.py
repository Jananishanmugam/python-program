def flatten(lst):
    result = []
    for item in lst:
        print(item)
        if isinstance(item, list):
            print(item)
            result.extend(flatten(item))  # Recursive call for nested lists
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, [5,6],4]]]))
