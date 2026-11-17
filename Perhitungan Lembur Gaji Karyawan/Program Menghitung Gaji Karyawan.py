# Program Menghitung Gaji Karyawan

# Input golongan karyawan
golongan = input("Masukkan Golongan Karyawan (A/B/C): ")

# Menentukan gaji pokok
if golongan == "A":
    gaji_pokok = 5000000
elif golongan == "B":
    gaji_pokok = 6500000
elif golongan == "C":
    gaji_pokok = 9500000
else:
    print("Golongan tidak valid")
    exit()

# Input jam lembur
jam_lembur = int(input("Masukkan jumlah jam lembur: "))

# Menentukan persentase lembur
if jam_lembur == 1:
    persen_lembur = 0.30
elif jam_lembur == 2:
    persen_lembur = 0.32
elif jam_lembur == 3:
    persen_lembur = 0.34
elif jam_lembur == 4:
    persen_lembur = 0.36
elif jam_lembur >= 5:
    persen_lembur = 0.38
else:
    persen_lembur = 0

# Menghitung gaji lembur
gaji_lembur = gaji_pokok * persen_lembur

# Menghitung total penghasilan
total_gaji = gaji_pokok + gaji_lembur

# Output hasil
print("\n===== HASIL PERHITUNGAN =====")
print("Golongan Karyawan :", golongan)
print("Gaji Pokok        : Rp.", gaji_pokok)
print("Gaji Lembur       : Rp.", gaji_lembur)
print("Total Penghasilan : Rp.", total_gaji)