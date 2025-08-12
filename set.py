set_1 = {1,2,3,4,5,2,1}
print(set_1)

set_2 = {3,4,5,6,7,8}

print(set_1.union(set_2))

print(set_1.intersection(set_2))

set_1.add(6)
print(set_1)

# value = set_1.pop()
# print(value)
# print(set_1)
# value2 = set_1.pop()
# print(value2)
# print(set_1)
# value3 = set_1.pop()
# print(value3)
# print(set_1)

set_1.remove(2)
set_1.discard(3)
print(set_1)
# set_1.remove(9)
set_1.discard(8)
print(set_1)