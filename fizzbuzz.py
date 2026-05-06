

while True:
    try:
        n_input = input("Lūdzu, ievadiet veselu skaitli N: ")
        N = int(n_input)
        break
    except ValueError:
           print("Kļūda: Ievadītā vērtība nav vesels skaitlis! Mēģiniet vēlreiz.\n")

# Cikls no 1 līdz N (ieskaitot)
for i in range(1, N + 1):
        
    # Pārbaudām dalāmību un būvējam tekstu
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0 and i % 7 == 0:
        print("FizzJazz")
    elif i % 5 == 0 and i % 7 == 0:
        print("BuzzJazz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 7 == 0:
        print("Jazz")
    else: print(i)    
        

