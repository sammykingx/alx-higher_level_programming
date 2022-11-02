def list_test(lst=[]):
    lst += [9, 8, 7]
    return lst


test_lst = [1, 2, 3, 4, 5, 6]
print('Before: ', test_lst)
list_test(test_lst)
print('After: ', test_lst)
