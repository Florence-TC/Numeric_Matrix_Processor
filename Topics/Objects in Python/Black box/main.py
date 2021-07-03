# use the function blackbox(lst) that is already defined
lst1 = [3, 'dog', True]
lst2 = blackbox(lst1)
if id(lst1) == id(lst2):
    print("modifies")
else:
    print("new")
