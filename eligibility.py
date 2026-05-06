def ievadit_vecumu():
    while True:
        try:
            vecums = int(input("Ievadiet vecumu (0-110): "))
            if 0 <= vecums <= 110:
                return vecums
            else:
                print("Kļūda: Vecumam jābūt robežās no 0 līdz 110!")
        except ValueError:
            print("Kļūda: Lūdzu, ievadiet veselu skaitli!")

def ievadit_ja_ne(jautajums):
    while True:
        atbilde = input(f"{jautajums} (j/n): ").strip().lower()
        if atbilde == 'j':
            return True
        elif atbilde == 'n':
            return False
        else:
            print("Kļūda: Lūdzu, ievadiet 'j' (jā) vai 'n' (nē)!")

print("=== Informācijas ievade ===")
vecums = ievadit_vecumu()
ir_tiesibas = ievadit_ja_ne("Vai ir autovadītāja apliecība?")
ir_students = ievadit_ja_ne("Vai ir students?")
ir_pensionars = ievadit_ja_ne("Vai ir veterāns?")

# Nosacījumu pārbaude
var_balsot = vecums >= 18
var_iret = ir_tiesibas and var_balsot
studentu_atlaide = ir_students
senioru_atlaide = ir_pensionars

# Ķeksīšu un krustiņu definēšana
KEKSITIS = "✓"
KRUSTINS = "✗"

print("\n=== Rezultāti ===")

# 1. Balsošana
print(f"Balsošana: [{KEKSITIS if var_balsot else KRUSTINS}]")

# 2. Mašīnas īre
print(f"Auto īre: [{KEKSITIS if var_iret else KRUSTINS}]")

# 3. Studenta atlaide
print(f"Studentu atlaide: [{KEKSITIS if studentu_atlaide else KRUSTINS}]")

# 4. Seniora atlaide
print(f"Seniora atlaide: [{KEKSITIS if senioru_atlaide else KRUSTINS}]")