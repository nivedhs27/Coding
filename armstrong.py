r=int(input("Enter: "))
#t is  a temporary variable to store r
t=r
q=0
while r>0:
    m =r%10  #eg: if 153 given as input: 153%10->3
    r=r//10  #153//10->15
    q+=(m**3)
#153%10->3,,153//10->15
#15%10->5,,15//10->1
#1%10->1,,1//10->1,hence r becomes 1 at end of loop,thats why previously we stored it in t
if q==t:
    print('Armstrong')
else:
    print(False)
