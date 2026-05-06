# Virkņu savienošana — Python neveic automātisku tipu konversiju 

print("90" + "3")          # rezultats: "903" 
#print("90" + 3)             # rezultats:  TypeError: can only concatenate str (not "int") to str
print(int("90") + 3)         # rezultats: 93  

# Robežgadījumi 
#print(int("abc"))         # rezultats: ValueError: invalid literal for int() with base 10: 'abc'
print(float("3.14"))       #rezultats: 3.14 

# Truthy / falsy 
print(bool(""))             # False (tukša virkne) 
print(bool(" "))            # True (atstarpe ir simbols!) 
print(bool("0"))            # True  (!) — jebkura netukša virkne ir True 
print(bool(0))              # False 
print(bool([]))             # False (tukšs saraksts) 
print(bool(None))           # False 
print(True + True + False)  # 2 (bool ir int apakšklase Python) 

# Jauktā aritmētika 
print(True * 10)            # 10 (True ir 1) 
print(False + 5)            # 5  (False ir 0) 
print(10 / True)            # 10.0 

#Skaitļu pārveidošana 
print(int(3.86))            # 3 ('norauj' beigas, nenotiek apaļošana) 
#print(int("3.14"))          # ValueError: invalid literal for int() with base 10: '3.14'
                            # Kļūda, tāpēc ka String vērtībai mēģina piekartot integer tipu
print(int(float("3.14")))   # 3 
print(float("1e3"))         # 1000.0 

 

#Citi interesanti gadījumi, izskaidrot kāpēc tā notiek. 
print(0.1 + 0.2 == 0.3)     # False, kāpēc? 
print(0.1 + 0.2)            # Tāpēc kā print(0.1 + 0.2) izdod vērtību lielāku par 0.3, t.i.
                               # 0.30000000000000004
                               #Tā ir Python "dīvainība" jo dzīvo binārājā sistēmā
print(0.1 + 0.1 == 0.2)     # Savukārt šī izteiksme ir True                           
print(round(2.5))           # 2 
print(round(3.5))           # 4 
                            #Tāpēc kā Python lieto algoritmu, kas 
                            # noapaļo līdz tuvākājām pāra skaitlim 
