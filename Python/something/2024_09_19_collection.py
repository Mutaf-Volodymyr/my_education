
list1 = ([], 2, 3)
list2 = list1
list2[0].append(1)


print(list1)

print(list2)
print(id(list1))
print(id(list2))