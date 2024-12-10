from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import MahasiswaView

def main():
    database = DataMahasiswa()

    while True:
        print("\nMenu Utama")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Data Mahasiswa")
        print("4. Ubah Data Mahasiswa")
        print("5. Hapus Data Mahasiswa")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            nim, nama, jurusan = InputForm.input_data()
            database.tambah_data(Mahasiswa(nim, nama, jurusan))
        elif pilihan == '2':
            MahasiswaView.tampilkan_data(database.data)
        elif pilihan == '3':
            nim = input("Masukkan NIM yang dicari: ")
            mahasiswa = database.cari_data(nim)
            MahasiswaView.tampilkan_detail(mahasiswa)
        elif pilihan == '4':
            nim = input("Masukkan NIM yang akan diubah: ")
            nama = input("Masukkan Nama baru: ")
            jurusan = input("Masukkan Jurusan baru: ")
            database.ubah_data(nim, nama, jurusan)
        elif pilihan == '5':
            nim = input("Masukkan NIM yang akan dihapus: ")
            database.hapus_data(nim)
        elif pilihan == '6':
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
