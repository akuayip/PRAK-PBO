#  Buatlah program python yang memiliki class Mahasiswa
# dengan properties nim, nama, angkatan, isMahasiswa. Buatkan minimal 3 method
# yang melakukan suatu operasi dan mengembalikkan suatu nilai (return). Object
# yang diinisiasikan minimal 2 dengan value properties yang berbeda. Gunakan default
# value parameter pada class untuk properties isMahasiswa kemudian coba hilangkan
# parameter untuk isMahasiswa saat ingin menginisiasi object kedua. 
# Diwajibkan menggunakan setter getter (fungsi ini tidak termasuk kedalam 
# 3 method yang diminta) untuk mengambil dan mengganti nilai properties 
# private yaitu nama dan nim.

class Mahasiswa :

    def __init__(self,nim,nama,angkatan,isMahasiswa):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
        self.__isMahasiswa = isMahasiswa

    @property
    def info(self):
        return "\n\t NIM : {}  \n\t Nama : {} \n\t Angkatan : {}".format(self.nim, self.nama, self.angkatan)
    
    @property
    def isMahasiswa(self):
        pass
    
    @isMahasiswa.getter
    def isMahasiswa(self):
        return self.__isMahasiswa

    @isMahasiswa.setter
    def isMahasiswa(self, input):
        self.__isMahasiswa = input
    
    def skripsi(self):
        print(f"Mahasiswa {self.nama} dengan {self.nim} angkatan {self.angkatan} sedang mmengerjakan skripsi")
              
    def lomba(self):
        print(f"Mahasiswa {self.nama} dengan {self.nim} angkatan {self.angkatan} sedang melaksanakan perlombaan")

    def olahraga(self):
        print(f"Mahasiswa {self.nama} dengan {self.nim} angkatan {self.angkatan} sedang melaksanakan olahraga")

    def belajar(self):
        print(f"Mahasiswa {self.nama} dengan {self.nim} angkatan {self.angkatan} sedang belajar diperpus")

Ana = Mahasiswa('122140083', 'Ana', '2022', 'Valid')
Ani = Mahasiswa('122140084', 'Ani', '2022', 'Valid')
Anu = Mahasiswa('122140085', 'Anu', '2022', 'Valid')
Ano = Mahasiswa('122140086', 'Ano', '2022', 'Valid')

Ana.skripsi()
Ani.lomba()
Anu.olahraga()
Ano.belajar()


# contoh untukk getter dan setter,, disini saya mengubah atau mengecek bahwa data mahasiswa atas nama ana itu valid, dan ucok non valid
 
print("Merubah Info ")
print(Ana.info)
print("Menjadi")
Ana.nama = 'Ucok'
Ana.nim = '122140100'
print(Ana.info)

print("getter dan sett  er untuk nama & nim")
print(Ana.info)
print(Ana.__dict__)
Ana.isMahasiswa = 'Non Valid'
print(Ana.info)
print(Ana.__dict__)