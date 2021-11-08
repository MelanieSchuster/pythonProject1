N = int(input('How many prime numbers do you want to print? N = '))
#insert the number of the first N prime numbers to print
a = 2
#because prime numbers begin with 2
while N!=0:
#for N not zero
    for i in range(2, a):
        if a%i==0:
            break
#if the number can be devided by 2 without a leftover, then it is not a prime number and should not be printed
    else:
        print(a)
        N -= 1
    a += 1
#after getting the prime number, 'N' has to be decreased, but 'a' has to be increased.
