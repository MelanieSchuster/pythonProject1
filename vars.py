a = 10
b = -5246196864864548465148468
c = a + b
print(type(c))
print('c:' + str(c))
print ('c{}'.format(c))


af = 242.033
bf = 65654654846465164654658979879879846545132123161484.352
cf = af + bf
print(type(cf))
print('cf:{}'.format(cf))

print(1.79e+308)
print(1.8e+308)

print('--------------')
bb = 0b11111111
# hexydecimal system
print(bb)

bx = 0xff
print(bx)

print(bb/bx)

f = 5

print(f**3)
#f hoch 3
g = 12
print('div g: {}'.format(g % 5))

h = 'ff'
print(int(h, 16))
#geb mir h als zahl im hexadezimalsystem aus
h1 = '525165'
h1i = int(h1)
print(h1.isdigit())
#only nummers
print(h1.isalpha())
#alphabet
print(h1.isalnum())
#alphabet OR numerical

print(type(h1))
print(type(h1i))

fa = 100
print(type(fa))
fa = 100.3563
print(type(fa))
print(round(fa, ))

g=[5,6.5,8.7]
print(type(g))