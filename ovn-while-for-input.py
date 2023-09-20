"""
Övningsmaterial om for-while-list och inmatning och felhantering
Specifikation:
Vi vill låta användaren mata in en lista med tal.
Användaren avslutar genom att mata in tomt.
Gränsnittet ska se ut något i stil med följande:
Mata in ett heltal: "3"
Mata in ett heltal: "5"
Mata in ett heltal: "8"
Mata in ett heltal: "a"
a är inte ett heltal, försök igen.
Mata in ett heltal: ""
Heltalen i listan är 3, 5, 8
"""

"""Vad behöver vi?
while och for
felhantering
input
funktioner
"""
def input_int():  

    """funnktion utan argument som tar in inmatning med input(),
      felhanterar och returnerar heltal eller "" """
    
    inmatning = input("Mata in ett heltal: ")
    try:
        if inmatning == "":
            return inmatning
        return int(inmatning)
    
    except ValueError as err:
        print(f"{inmatning} är inte ett heltal och ger fel {err}. Försök igen!" )


def utskrift(heltalslista):
    """funktion som tar en lista med heltal som argument 
    och skriver ut dessa med hjälp av for-loop"""

    print ("Talen i listan är", end=" ")
    for i in heltalslista[:-1]:
        print(i, end=", ")
    print(heltalslista[-1])


def inmatning(heltalslista):
    """function som tar en tom lista som argument 
    och fyller den med heltal"""
    while True:
        heltal = input_int()
        if heltal == "":
            break
        heltalslista.append(heltal)
    return heltalslista


def main():
    lista = []
    heltalslista = inmatning(lista)
    utskrift(heltalslista)

if __name__ == "__main__": 
    main()