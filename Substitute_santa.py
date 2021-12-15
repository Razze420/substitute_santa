# Rasmus Ekstedt
# NTI
# Tetek20
# v.50

def val1():
    global filnamn
    filnamn = input("Vad ska filen heta? ")
    barnnamn = input("Vad heter barnet? ")
    with open(filnamn+".txt", "a", encoding="utf8") as personal:
        personal.write(f"barnet heter {barnnamn}\n\n")
        print("Skriv in vad barnet vill ha i sin önskelista, Skriv # om du vill avsluta?\n")

        tr = True
        while tr:
            skriv = input("vad önskar barnet sig? ")
            if "#" in skriv:
                break
            else:
                personal.write(f"barnet önskar sig: {skriv}\n")

def val2():
    filnamn = input("vilken fil vill du öppna?(du behöver inte skriva txt)\n")
    with open(filnamn+".txt", "r", encoding="utf8") as personal:
        s = personal.readlines()
        for line in s:
            print(line,end="")

def main():
    tr = True
    while tr:
        print("----VÄLKOMMEN TILL MENYN----\n1. skapa en ny önskelista\n2. Lägg till saker i din ösnkelista\n3. Avsluta(#)")
        s = input("")
        if s == str("1"):
            val1()
        elif s == str("2"):
            val2()
        elif s == str("#"):
            break
    

if __name__ == "__main__":
        main()

