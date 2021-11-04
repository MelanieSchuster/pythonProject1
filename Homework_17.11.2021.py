N1=101
for num in range(1,N1):
    for i in range(2,num):
        if (num%i==0):
            break
        else:
            print(num)
            break

N = 10
for i in range(2,N+1):
    for j in range(2,i):
        if(i%j == 0):
            break
    else:
        print(i)

#the second version is better but we didn't had this either