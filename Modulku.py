import math

# melakukan konversi suhu ke Celcius
def fahrenheit_ke_celcius(f):
    return 5 * (f - 32) / 9

def reamur_ke_celcius(r):
    return (5 / 4) * r

def kelvin_ke_celcius(k):
    return k - 273

# melakukan konversi jam ke detik
def jam_ke_detik(hh, mm, ss):
    return (hh * 3600) + (mm * 60) + ss

# Nilai akhir
def nilaiakhir(uas, uts):
    return (0.65 * uas) + (0.35 * uts)

#Volume BOLA
def volumebola(r):
    return ((4/3) * math.pi * (r*r*r))

#Volume TABUNG
def volumetabung(r, t):
    return math.pi * (r*r) * t

#Volume KERUCUT
def volumekerucut(r, t):
    return (1/3)* math.pi * r * r * t
