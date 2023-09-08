"""Ett exempel från en fråga"""

# Genererad kod från GitHub Copilot
def addera(a, b):
    """Returnerar summan av a och b"""
    return a + b

def subtrahera(a, b):
    """Returnerar differensen mellan a och b"""
    return a - b

def multiplicera(a, b):
    """Returnerar produkten av a och b"""
    return a * b

# Beräkna 1 + 2 + 3*4*5
def beräkna():
    """Beräknar 1+2+3*4*5 mha funktionerna addera, subtrahera och multiplicera"""
    #multiplikationen = multiplicera(3, 4)
    #multiplikationen = multiplicera(multiplikationen, 5)
    multiplikationen = multiplicera(multiplicera(3, 4), 5)
    summan = addera(addera(1, 2), multiplikationen)
    return summan

print("1+2+3*4*5 = {beräkna()}")
print(f"1+2+3*4*5 = {1+2+3*4*5}")