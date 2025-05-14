print("--- JEDNOSTAVNA BILJEZNICA ---")

test=1
while test == 1:
    
    print("1. Dodaj novu biljesku")
    print("2. pregledaj sve biljeske")
    print("3. izlaz")

    a = int(input("Odaberite opciju (1-3): "))
    print()
    print()
    print()
    
    if a == 3:
        print("Izlaz iz bilježnice")
        test = 0
        
    elif a == 2:
        with open ("text.txt","r") as dat:
            b = dat.read()
            print("\n--- BILJESKE ---")
            if not b.strip():
                print("Biljeznica je prazna")
            else:
                print(b)
                
            print()
            print("---------------------------------")
            print()

    elif a == 1:
        unos = input("Unesi biljesku: ")
        with open ("text.txt","a") as dat:
            dat.write(unos.strip()+ "\n")
            
        print()
        print("---------------------------------")
        print()

    else:
        print("Nepoznata opcija. Molimo odaberite 1-3")
        
        
