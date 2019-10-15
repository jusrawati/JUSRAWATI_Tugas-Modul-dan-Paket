import Modulku
def main():
    #Fahrenheit ke Celcius
    print("KONVERSI SUHU (Fahrenheit ke Celcius)")
    f = float(input("Masukkan suhu (Fahrenheit): "))
    c = Modulku.fahrenheit_ke_celcius(f)
    print("Fahrenheit \t:", f)
    print("Celcius \t:", c)
    print (" ")

    #Reamur ke Celcius
    print("KONVERSI SUHU (Reamur ke Celcius)")
    r = float(input("Masukkan suhu (Reamur): "))
    c = Modulku.reamur_ke_celcius(r)
    print("Reamur \t\t:", r)
    print("Celcius \t:", c)
    print (" ")

    #Kelvin ke Celcius
    print("KONVERSI SUHU (Kelvin ke Celcius)")
    k = float(input("Masukkan suhu (Kelvin): "))
    c = Modulku.kelvin_ke_celcius(k)
    print("Kelvin \t\t:", k)
    print("Celcius \t:", c)
    print (" ")
    
    #Konversi Jam ke Detik
    print("KONVERSI JAM KE DETIK")
    hh = int(input("Masukkan jumlah jam \t: "))
    mm = int(input("Masukkan jumlah menit \t: "))
    ss = int(input("Masukkan jumlah detik \t: "))
    totaldetik = Modulku.jam_ke_detik(hh, mm, ss)
    print(str(hh) + ':' + str(mm) + ':' + str(ss) + 
         " sama dengan " + str(totaldetik) + 
         " detik")
    print (" ")

    #Nilai Akhir
    print("NILAI AKHIR")
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    na = Modulku.nilaiakhir(uas, uts)
    print("Nilai Akhirnya \t:", na)
    print (" ")

    #Volume BOLA
    print("VOLUME BOLA")
    r = float(input("Masukkan Jari-jari: "))
    vol = Modulku.volumebola(r)
    print("Volume Bola \t: ", vol)
    print (" ")

    #Volume TABUNG
    print("VOLUME TABUNG")
    r = float(input("Masukkan Jari-jari: "))
    t = float(input("Masukkan Tinggi   : "))
    vol = Modulku.volumetabung(r, t)
    print("Volume Tabung \t: ", vol)
    print (" ")

    #Volume KERUCUT
    print("VOLUME KERUCUT")
    r = float(input("Masukkan Jari-jari: "))
    t = float(input("Masukkan Tinggi   : "))
    vol = Modulku.volumekerucut(r, t)
    print("Volume Kerucut \t: ", vol)
    print (" ")

if __name__ == "__main__":
   main()
