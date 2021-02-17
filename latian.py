'''
i = 0
while i < 10:
  if i == 5:

    continue
  print(i,' x ',i ,' = ',i*i)
  i += 1
for i in range(99):
    print(i)
    if i == 12 :
        continue
        

def hitung_luas_segitiga():
  alas = 5
  tinggi = 7
  luas = (alas * tinggi) / 2
  print("Luas segitiga adalah: ",luas)
   
hitung_luas_segitiga()

def nama_saya():
    print("Muhammad Hibban Arham")

nama_saya()

def sapa_orang(nama) :
    print("hai", nama)

sapa_orang("hibban")
sapa_orang("arham")
sapa_orang("muhammad")
'''
def harga_setelah_pajak(harga_dasar):
  return harga_dasar + (harga_dasar * 10/100)
 
harga_cilok = 5000
harga_final_cilok = harga_setelah_pajak(harga_cilok)
print("Harga cilok 1 porsi Rp.", harga_final_cilok)