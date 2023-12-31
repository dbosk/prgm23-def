"""Ett förslag"""

PI = 3.14

def area_kvadrat(sida):
    """Returnerar arean för en kvadrat med sidan sida"""
    return sida**2

def area_cirkel(radie):
    """Returnerar arean för en cirkel med radien radie"""
    return PI * radie**2

def gul_kakel_cirkel(sida):
    """Beräknar hur mycket gul färg som går åt på kaklet med gul cirkel"""
    return area_cirkel(sida/2)

def grön_kakel_cirkel(sida):
    """Beräknar hur mycket grön färg som går åt på kaklet med gul cirkel"""
    return area_kvadrat(sida) - gul_kakel_cirkel(sida)

print(f"En kakelplatta med sidan 10 cm behöver {gul_kakel_cirkel(10)} cm^2 gul färg och {grön_kakel_cirkel(10)} cm^2 grön färg.")