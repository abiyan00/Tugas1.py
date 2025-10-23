# Program Hitung Gaji Karyawan - PT. Dingin Damai

# Data Tetap
GAJI_POKOK = 300000
HONOR_LEMBUR_PER_JAM = 3500

# Input
nama = input("Nama Karyawan: ")
golongan = int(input("Golongan Jabatan (1/2/3): "))
pendidikan = input("Pendidikan (SMA/D1/D3/S1): ").upper()
jam_kerja = int(input("Jumlah jam kerja: "))

# Hitung Tunjangan Jabatan
if golongan == 1:
    tunjangan_jabatan = 0.05 * GAJI_POKOK
elif golongan == 2:
    tunjangan_jabatan = 0.10 * GAJI_POKOK
elif golongan == 3:
    tunjangan_jabatan = 0.15 * GAJI_POKOK
else:
    tunjangan_jabatan = 0
    print("Golongan tidak valid, tidak ada tunjangan jabatan.")

# Hitung Tunjangan Pendidikan
if pendidikan == "SMA":
    tunjangan_pendidikan = 0.025 * GAJI_POKOK
elif pendidikan == "D1":
    tunjangan_pendidikan = 0.05 * GAJI_POKOK
elif pendidikan == "D3":
    tunjangan_pendidikan = 0.20 * GAJI_POKOK
elif pendidikan == "S1":
    tunjangan_pendidikan = 0.30 * GAJI_POKOK
else:
    tunjangan_pendidikan = 0
    print("Pendidikan tidak valid, tidak ada tunjangan pendidikan.")

# Hitung Honor Lembur
if jam_kerja > 8:
    honor_lembur = (jam_kerja - 8) * HONOR_LEMBUR_PER_JAM
else:
    honor_lembur = 0

# Total Gaji
total_gaji = GAJI_POKOK + tunjangan_jabatan + tunjangan_pendidikan + honor_lembur

# Output
print("\n=== LAYAR KELUARAN ===")
print(f"Karyawan yang bernama {nama}")
print(f"Tunjangan Jabatan     : Rp {int(tunjangan_jabatan):,}")
print(f"Tunjangan Pendidikan  : Rp {int(tunjangan_pendidikan):,}")
print(f"Honor Lembur          : Rp {int(honor_lembur):,}")
print(f"Total Gaji            : Rp {int(total_gaji):,}")
