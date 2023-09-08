def fråga_ja_nej(string):
    """Tar string och skriver ut den, frågar om det den skriver ut (ja/nej).
    Kollar om svaret är no eller inte.
    Returnerar sant om man väljer no, annars falskt."""
    print(string)
    svar: bool = input()

    # om vi inte säger nej, då betyder det ja
    #if not no == "no":
    if svar != "no":
        return True
    else:
        return False

vattna = fråga_ja_nej("Vill du vattna blommorna? ")
if vattna:
    print("Vattnar blommorna")



sysslor = ["Tömma diskmaskinen", "Dammsuga mormors hus", "Gå ut med hunden"]

b = blommor()

if fråga_ja_nej("Vill du ta ut soporna?"):
    print("Tar ut soporna")

print("Förutom att vattna blommor och ta ut sopor ska vi:")

def skriv_ut_sysslor():
    """Skriver ut alla chores"""
    for x in sysslor:
        print(x)
        
skriv_ut_sysslor()
