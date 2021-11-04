N=101
for num in range(1,N):
    for i in range(2,num):
        if (num%i==0):
            break
        else:
            print(num)
            break

#not bad but N has to be the number of the prime numbers displayed