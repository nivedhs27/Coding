l=input("Enter no:")
r=0
m=int(l)
while m>0:
    n=m%10
    r+=n
    m//=10
print(r)
