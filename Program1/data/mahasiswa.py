class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"NIM: {self.nim}, Nama: {self.nama}, Jurusan: {self.jurusan}"


class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah_data(self, mahasiswa):
        self.data.append(mahasiswa)

    def cari_data(self, nim):
        for mhs in self.data:
            if mhs.nim == nim:
                return mhs
        return None

    def hapus_data(self, nim):
        self.data = [mhs for mhs in self.data if mhs.nim != nim]

    def ubah_data(self, nim, nama, jurusan):
        mhs = self.cari_data(nim)
        if mhs:
            mhs.nama = nama
            mhs.jurusan = jurusan
