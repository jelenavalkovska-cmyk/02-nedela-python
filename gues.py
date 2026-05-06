
import random; 
N= random.randint(1, 100)
print(N)
k = 0

def ievadit_skaitli():
    while True:
        try:
            minejums = int(input("Tavs minējums: "))
            if 0 <= minejums <= 100:
                return minejums
            else:
                print("Kļūda: Skaitlim jābūt robežās no 0 līdz 110!")
        except ValueError:
            print("Kļūda: Lūdzu, ievadiet veselu skaitli!")

while True and k < 10: 

    minejums = ievadit_skaitli() 
  
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

    if k == 10:
        print("Tu izmantoji visus 10 mēģinājumus! GAME over!")