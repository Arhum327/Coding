def primefactor(n):

    c=2
    while n>1:
        if n%c ==0:
            print(c)
            n/=c
        else:
           c+=1
n=int(input("Enter no"))
primefactor(n)


