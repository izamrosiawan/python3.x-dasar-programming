import os

tipe = {
    "nama": "string",
    "umur": "int",
    "tinggi": "float"
}

data_mahasiswa = {}

while True:
    os.system("cls")
    print("Masukkan data tipe mahasiswa:")
    mahasiswa = dict.fromkeys(tipe.keys())
    mahasiswa["nama"]= input("Nama: ")
    mahasiswa["umur"]= int(input("Umur: "))
    mahasiswa["tinggi"]=float(input("Tinggi: "))
    
    KEY = input("Masukkan Kode Mahasiswa: ")
    data_mahasiswa.update({KEY: mahasiswa})
    
    print("\nData Mahasiswa:\n")
    print(f"{"Kode Mahasiswa":<20} {"Nama":<15} {"umur":<15} {"Tinggi"} ")
    print("-" * 60)
    # for key, value in data_mahasiswa.items():
    #     print(f"{key:<10} {value['nama']:<15} {value['umur']:<15} {value['tinggi']:>4.2f}")
    
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA= data_mahasiswa[KEY]["nama"]
        UMUR  = data_mahasiswa[KEY]["umur"]
        TINGGI= data_mahasiswa[KEY]["tinggi"]    
        
        print(f"{KEY:<20} {NAMA:<15} {UMUR:<15} {TINGGI}")
        
    tambah= input("\nTambah data mahasiswa lagi? (y/n): ")
        
    if tambah.lower() == "n":
        break
    
print("\nTerima kasih telah menggunakan program ini!\n")
        