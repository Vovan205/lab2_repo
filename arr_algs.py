def min(arr1):
    minimal = arr1[0]
    for i, el in enumerate(arr1):
        if el < minimal:
            minimal = el
    return minimal
arr1 = [8, 5, 6, 9, 2, 1, 78]
print(min(arr1))

