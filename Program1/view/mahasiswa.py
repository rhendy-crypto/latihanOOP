class MahasiswaView:
    @staticmethod
    def tampilkan_data(data):
        if data:
            for mhs in data:
                print(mhs)
        else:
            print("Belum ada data mahasiswa.")

    @staticmethod
    def tampilkan_detail(mahasiswa):
        if mahasiswa:
            print(mahasiswa)
        else:
            print("Mahasiswa tidak ditemukan.")
