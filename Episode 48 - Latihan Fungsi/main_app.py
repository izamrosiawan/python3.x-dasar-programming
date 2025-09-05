'''Latihan Fungsi'''

import os

# program menghitung luas dan keliling persegi panjang

# # Membuat header program
# os.system("clear")
# # os.system("cls")
# print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
# print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
# print(f"{'-'*40:^40}")

# # Mengambil input user
# LEBAR = int(input("Masukan nilai lebar: "))
# PANJANG = int(input("Masukan nilai panjang: "))

# # Program menghitung luas
# LUAS = PANJANG*LEBAR
# KELILING = 2*(PANJANG+LEBAR)

# # tampilkan hasilnya
# print(f"hasil perhitungan luas = {LUAS}")
# print(f"hasil perhitungan keliling = {KELILING}")

def header():
    '''fungsi Header'''
    # os.system("clear")
    os.system("cls")
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'-'*40:^40}")

def input_user():
    '''fungsi input user'''
    # Mengambil input user
    lebar = int(input("\nMasukan nilai lebar: "))
    panjang = int(input("Masukan nilai panjang: "))

    return lebar,panjang

def hitung_luas(lebar,panjang):
    '''fungsi luas'''
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    '''fungsi keliling'''
    return 2*(lebar+panjang)

def display(message,value):
    '''fungsi display'''
    print(f"\nhasil perhitungan {message} = {value}")
    
def minta_input_opsi():
    '''fungsi untuk meminta input opsi dari user'''
    while True:
        try:
            opsi = int(input("Masukkan opsi (1-3): "))
            if opsi in [1, 2, 3]:
                return opsi
            else:
                print("\tOpsi tidak valid, silakan coba lagi.")
        except ValueError:
            print("\tInput harus berupa angka, silakan coba lagi.")

def hitung_luas_keliling(lebar, panjang, opsi):
    '''fungsi untuk menghitung luas dan keliling'''
    if opsi == 1:
        hasil = hitung_luas(lebar, panjang)
        display("luas", hasil)
    elif opsi == 2:
        hasil = hitung_keliling(lebar, panjang)
        display("keliling", hasil)
    elif opsi == 3:
        luas = hitung_luas(lebar, panjang)
        keliling = hitung_keliling(lebar, panjang)
        display("luas", luas)
        display("keliling", keliling)
    

# Program utamanya
while True:
    header()
    
    print('''
    Operasi yang tersedia:  1. Hitung Luas
                            2. Hitung Keliling
                            3. Hitung Luas dan Keliling
    ''')
    
    OPSI = minta_input_opsi()
    LEBAR,PANJANG = input_user()
    
    hitung_luas_keliling(LEBAR, PANJANG, OPSI)

    isContinue = input("\napakah lanjut (y/n)? ")
    if isContinue == "n":
        break

print("\nProgram selesai, terima kasih")