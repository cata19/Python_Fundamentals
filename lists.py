# collection of values assigned to one variable
a = [10, 10, 1, 2, 3, 4, 3.56, 'Hello', [11, 13]]

# print(a)
# print(a.index('Hello'))
# print(a.reverse())
# print(a.pop())
# print(a.pop(0))
# print(a.append(99))
print(a.count(10))
print(a)

a += [45, 67, 77]
print(a)

a.append(19)
print(a)

print(a[3])
print(a[8][1])

if 10 in a:
    print('10 is in the list')
