
def sum_bowls_recursion(r):
    if r==1:
        return 1
    else:
        return r + sum_bowls_recursion(r-1)

n = int(input("enter number "))
print('Sum bowls u0sing resursion: {}'.format(sum_bowls_recursion(n)))