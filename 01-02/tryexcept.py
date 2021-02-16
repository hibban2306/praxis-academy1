'''
while True:
  try:
      x = int(input("Please enter a number: "))
      break
  except ValueError:
      print("Oops!  That was no valid number.  Try again...")
'''

while True :
    try:
        angka = int(input("masukkan angka: "))
        break
    except:
        print("yang anda masukkan bukan angka")
print("berhasil anda memasukkan angka: ", angka)
