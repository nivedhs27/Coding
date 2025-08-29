r=input("Enter string:")
m=['a','A','e','E','i','I','u','U','O','o']
n=0
for i in r:
    for j in m:
       if i==j:
           n=n+1
           
    
print(f"No of vowels are:{n}")