n=int(input())
a=0
b=0
c=n
while a<=0.5:
    a=a+1/c
    c-=1
    b+=1
print(n-b+1)
