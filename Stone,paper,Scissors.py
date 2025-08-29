def siq() :
    import random
    r=['Stone','Paper','Scissors']
    s=random.choice(r)
    h=input("Select:\n 1,Stone \n2,Paper \n3,Scissors")
    print(f"Computers choice is : {s}")
    while True:
       if s.lower()=='stone'and h.lower()=='paper':
        print('You won')
        break
       elif s.lower()=='paper'and h.lower()=='stone':
        print('You lost')
        break
       elif s.lower()=='scissors'and h.lower()=='paper':
        print('You lost')
        break
       elif s.lower()=='paper'and h.lower()=='scissors':
        print('You won')
        break
       elif s.lower()=='stone' and h.lower()=='scissors':
        print('You lost')
        break
       elif s.lower()=='scissors'and h.lower()=='stone':
        print('You won')
        break
       elif s.lower()==h.lower():
        print(f"'Retry' ")
        siq()
        break
       else :
        print('Invalid choice \n try again')
        siq()
        break
siq()
    
        