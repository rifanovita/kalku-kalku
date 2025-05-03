print("Kalkulator Konsentrasi Kimia")
print("1. Hitung Molaritas")
print("2. Hitung Normalitas")

pilih = input("Pilih 1 atau 2: ")
jumlah = float(input("Masukkan jumlah mol atau ekivalen: "))
volume = float(input("Masukkan volume larutan (liter): "))
hasil = jumlah / volume

if pilih == "1":
    print("Molaritas =", hasil, "mol/L")
elif pilih == "2":
    print("Normalitas =", hasil, "eq/L")
else:
    print("Pilihan tidak valid.")
