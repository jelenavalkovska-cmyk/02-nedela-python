
import random; 
N= random.randint(1, 100)
print(N)
k = 1

while True or k < 10: 

    minejums = int(input("Tavs minējums: ")) 
   

    # ... apstrāde ... 

    if minejums < N: 
        print("Par mazu")
        k += 1;
    elif minejums > N:
        print("Par lielu")
        k += 1;
    else: 
        print(f"Apsveicu! Tu uzminēji, izmantojot {k} minējumus!")
        break 