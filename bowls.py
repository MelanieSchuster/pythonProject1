
rows = 5
#sum ? how many x's
#
#    x x x x x
#     x x x x
#      x x x
#       x x
#        x

n = int(input("enter number "))
sum = 0
for num in range (1, n +1, 1):
    sum = sum + num
print("sum of the first", n, "number is: ", sum)

sum_num = (n*(n+1)) / 2
print('sum as sequence: {}'.format(sum_num))
