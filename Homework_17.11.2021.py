N = int(input('How many prime numbers do you want to print? N = '))
#insert the number of the first N prime numbers to print
a = 2
#because zero and one are no prime numbers by definition I start checking if the numbers are prime numbers beginning from 2
while N!=0:
#for N not zero
    for i in range(2, a):
        if a%i==0:
            break
#if the number can be devided by another number than one and itself without a leftover, then it is not a prime number and should not be printed.
#otherwise it should be printed.
    else:
        print(a)
        N -= 1
    a += 1
#after getting the prime number, 'N' has to be decreased.
#In any cases a has to be increased to check the next number.
