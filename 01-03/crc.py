# Class Responsibilities Colaborator (CRC) Card
# dibuat ketika akan melakukan sebuah tugas dengan membagi tugas (responsibilities) kepada
# class utama dan class collaborator untuk membantu menyelesaikan responsibilities

# contoh 
class CetakNama():
    '''
    @responsibility : mencetak nama
    '''
    def cetak(self):
        print("Cetak Nama", self.nama)


class Nama(CetakNama):
    '''
    @colaborator : CetakNama
    @responsibilities: mengambil nama yang akan dicetak 
    '''
    def __init__(self, nama):
        self.nama = nama

obj1 = Nama("Arya")
obj1.cetak()