"""
Avgöra om en e-postadress är giltig

Skriv ett program som tar en e-postadress som input och sedan returnerar om den givna e-postadressen är giltig eller inte. Går det att återanvända kod från föregående uppgift?
"""

def kolla_mailadress(mailadress):
    """
    Kollar om mailadress har alla delear som krävs:
    Ska finnas en del, sedan @, sedan någonting . någonting.

    Returnera True om giltig adress, False om ogiltig.

    Begränsningar: bara ett @
    """
    if mailadress.count("@") == 1:
        namn, domän = mailadress.split("@")
    else:
        return False
    return len(namn) > 0 and "." in domän

print(f"dbosk@kth.se {kolla_mailadress('dbosk@kth.se')}")
print(f"dbosk@@kth {kolla_mailadress('dbosk@@kth')}")
print(f"dbosk {kolla_mailadress('dbosk')}")