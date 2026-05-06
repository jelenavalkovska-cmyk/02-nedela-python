def konvertetajs():
    print("Sveiki! Izvēlēties konversijas veidu:")
    print("1. No kilometriem (km) uz jūdziem (mi)")
    print("2. No kilogramiem (kg) uz mārciņām (lb)")
    print("3. No litriem (L) uz galoniem (gal)")
    print("4. No dolāriem ($) uz Eiro (€)")

izvele1 = input("Ievadi skaitli no 1 līdz 4: ")
 
if type(izvele1) != int:
   print("Kļūda! Tas nav vesels skaitlis!")
if izvele1 not in range(1, 5):
   print("Kļūda! Skaitlim jābūt no 1 līdz 4!")   


match izvele1:
     case "1":
        izvele2 = input("Ievadi virzienu: 1. km -> mi vai 2. mi -> km: ")
        if izvele2 == '1': 
            KM = float(input("Ievadi kilometrus: "))
            KM_TO_MI = KM * 0.621371
            print(f"Rezultāts: {KM:.2f} km ir {KM_TO_MI: .2f} mi")

        elif izvele2 == '2': 
            MI = float(input("Ievadi jūdzes: "))
            MI_TO_KM = MI / 0.621371
            print(f"Rezultāts: {MI:.2f} mi ir {MI_TO_KM: .2f} km")

        else: 
            print("Kļūda! Lūdzu, izvēlies 1 vai 2!")


     case "2":
         izvele2 = input("Ievadi virzienu: 1. kg -> lb vai 2. lb -> kg: ")
         if izvele2 == '1': 
            KG = float(input("Ievadi kilogramus: "))
            KG_TO_LB = KG * 2.20462
            print(f"Rezultāts: {KG:.2f} kg ir {KG_TO_LB: .2f} lb")

         elif izvele2 == '2': 
            LB = float(input("Ievadi mārciņas: "))
            LB_TO_KG = LB / 2.20462
            print(f"Rezultāts: {LB:.2f} lb ir {LB_TO_KG: .2f} kg")

         else: 
            print("Kļūda! Lūdzu, izvēlies 1 vai 2!")

        
     case "3":
         izvele2 = input("Ievadi virzienu: 1. L -> gal vai 2. gal -> L: ")
         if izvele2 == '1': 
            L = float(input("Ievadi litrus: "))
            L_TO_GAL = L * 0.264172
            print(f"Rezultāts: {L:.2f} L ir {L_TO_GAL: .2f} gal")

         elif izvele2 == '2': 
            GAL = float(input("Ievadi galonus: "))
            GAL_TO_L = GAL / 0.264172
            print(f"Rezultāts: {GAL:.2f} gal ir {GAL_TO_L: .2f} L")

         else: 
            print("Kļūda! Lūdzu, izvēlies 1 vai 2!")


     case "4":
         izvele2 = input("Ievadi virzienu: 1. $ -> \u20AC vai 2. \u20AC -> $: ")
         if izvele2 == '1': 
            D = float(input("Ievadi dolārus: "))
            D_TO_EIRO = D * 0.84235020
            print(f"Rezultāts: {D:.2f} $ ir {D_TO_EIRO: .2f} \u20AC")

         elif izvele2 == '2': 
            EIRO = float(input("Ievadi eiro: "))
            EIRO_TO_D = EIRO / 0.84235020
            print(f"Rezultāts: {EIRO:.2f} \u20AC ir {EIRO_TO_D: .2f} $")

         else: 
            print("Kļūda! Lūdzu, izvēlies 1 vai 2!")
    
     case _:
       print("Kļūda! Lūdzu, skaitli no 1 līdz 4")


konvertetajs()

