pilih = input("1=Molaritas, 2=Normalitas: ")
jumlah = float(input("Masukkan mol atau ekivalen: "))
volume = float(input("Masukkan volume (L): "))
hasil = jumlah / volume
print("Hasil =", hasil, "mol/L" if pilih == "1" else "eq/L")
