l1 = [3425, 363236, 23623, 5654, 55135435, 4415646, 12512]

print(l1[3])
print(l1[-3:-1])
print(len(l1))

i=0
for elem in l1:
    print('Element {} at {}'.format(elem, i))
    i += 1

print(l1.index(12512))

print('-------------')
print(l1.count(12512))
print('-------------')


l1.insert(3, 50662)
print(l1)
print(len(l1))

s1 = set(l1)
print(s1)
l2 = list(s1)
print(l2)
l2.append(252556)
l2.sort(reverse=True)
print(sorted(l2))

#print(s1[5]) -> geht nicht, da die Reihenfolge nicht fest ist

l3 = [536, 265473, 'abcd', 2342.252]
print(l3)
bc = l3[2][1:3]
print(bc)

sum = 0
for el in l3:
    if type(el) == int:
        sum += el
print(sum)

print('-------------')
l4 = [25, 12, 654, 67]
l5 = [25, 66]
l6 = l4 + l5
print(l6)

l7 = [x*2 for x in l6]
print(l7)