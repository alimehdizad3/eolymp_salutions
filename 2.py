n=int(input())

if n == 0:
    print(1)
else:
    a=0
    while n!=0:
        n=n//10
        a=a+1
    print(a)
