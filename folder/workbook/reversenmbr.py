n=int(input("enter a nmbr  "))
print(str(n)[::-1])
k=0
rev=0
while(n>0):
    k=n%10
    rev=rev*10+k
    n//=10
print(str(rev))
