t1 = (5, 2, 8)
print(t1[2])
#second element of the list will be displayed

d1 = {0: 525, 1: 5747, 2: 3747}
print(d1[0])
#element named 0 will be displayed

d1 = {'a': 525,'a': 56464, 'bb': 6747, 'ccc': 3747}
d1['ddd'] = 436536
print(d1)
print(d1['a'])

for k, v, in d1.items():
    print('{}: {}'.format(k, v))
for k in d1.keys():
    print('{}: {}'.format(k, d1[k]))
