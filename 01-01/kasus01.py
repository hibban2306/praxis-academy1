<<<<<<< HEAD
#bubble short
'''
def hib(ban):
    iterasi = 0
    for j in range (len(ban)-1):
        for i in range(len(ban)-1-j):
            if ban[i]>ban[i+1]:
                ban[i],ban[i+1]=ban[i+1],ban[i]
        iterasi+=1
        print(iterasi, ban)
ban = [9,17,2,42,1,7,3,4,67]
print('data yang akan di sort :' , ban)
print('bubble sort : ')
hib(ban)
'''
'''
#selection short
def ss(list):
    iterasi = 0
    for i in range(len(list)-1):
        minimal = i
        for j in range(i+1,len(list)):
            if list[j] < list[minimal]:
                minimal = j
        iterasi += 1
        list[minimal],list[i]=list[i], list[minimal]
        print(iterasi, list)
list=[98,6,33,11,57,33,44,55,29,76,60,81]
print('Data yang akan di sort :', list )
print('Selection Sort :')
ss(list)
'''
'''
#insertion short
def insertion(list):
    for j in range(len(list)-1,-1,-1):
        value = list[j]
        hole = j
        while hole <(len(list)-1) and list[hole+1]>list[hole]:
            list[hole] = list[hole+1]
            hole = hole+1
            list[hole] = value
        print(list)
list = [2,54,38,76,23,56,84,90]
print("Data yang akan di sort", list)
print("Insertion Sort :")
insertion(list)
'''
'''
#quick short
def quickshort(a,start,end):
    if start<end:
        pindex = partition(a,start,end)
        quickshort(a,start,pindex-1)
        quickshort(a,pindex+1,end)
 
def partition(a,start,end):
    middle = int(end/2)
    pivot = a[middle]
    pindex = start
    for i in range(start,middle):
        if a[i]>=pivot:
            a[i],a[pindex]=a[pindex],a[i]
            pindex = pindex + 1
    a[pindex],a[middle]=a[middle],a[pindex]
    print(a)
    return pindex
 
a = [68,90,78,44,34,20,100,56,34,2]
quickshort(a,0,len(a)-1)
'''
'''
#merge sort
def mergesort(a):
    print('memecah',a)
    n=len(a)
    if n<2:
        return a
    else:
        mid=n//2
        left=a[:mid]
        right=a[mid:]
 
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i< len(left) and j<len(right):
            if left[i]>right[j]:
                a[k]=left[i]
                i=i+1
            else:
                a[k]=right[j]
                j=j+1
            k=k+1
        while i<len(left):
            a[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            a[k]=right[j]
            j=j+1
            k=k+1
    print('menggabungkan',a)
    '''


def merge_sort(list_bilangan):
  jumlah_bilangan =  len(list_bilangan)
  if jumlah_bilangan > 1:
    posisi_tengah = len(list_bilangan)//2
    potongan_kiri = list_bilangan[:posisi_tengah]
    potongan_kanan = list_bilangan[posisi_tengah:]
    
    merge_sort(potongan_kiri)
    merge_sort(potongan_kanan)

    jumlah_bilangan_kiri = len(potongan_kiri)
    jumlah_bilangan_kanan = len(potongan_kanan)
    c_all,c_kiri,c_kanan = 0,0,0 # pencacah/counter
    print('Sebelum merge:',list_bilangan)  
    print('Potongan sebelum merge:',potongan_kiri,':',potongan_kanan)
    while c_kiri < jumlah_bilangan_kiri or c_kanan < jumlah_bilangan_kanan:
      if c_kiri == jumlah_bilangan_kiri: # elemen di potongan kiri habis
        list_bilangan[c_all] = potongan_kanan[c_kanan]
        c_kanan = c_kanan + 1
      elif c_kanan == jumlah_bilangan_kanan: # elemen di potongan kanan habis
        list_bilangan[c_all] = potongan_kiri[c_kiri]
        c_kiri = c_kiri + 1
      elif potongan_kiri[c_kiri] <= potongan_kanan[c_kanan]: # nilai elemen di potongan kiri lebih kecil
        list_bilangan[c_all] = potongan_kiri[c_kiri]
        c_kiri = c_kiri + 1
      else: # nilai elemen di potongan kanan lebih besar
        list_bilangan[c_all] = potongan_kanan[c_kanan]
        c_kanan = c_kanan + 1
      c_all = c_all + 1
    print('Setelah merge:', list_bilangan)
    print()
          
angka = [6,5,3,1,8,7,2,4]
print('Sebelum sort:',angka)
merge_sort(angka)
print('Setelah sort:',angka)
=======
#bubble short
'''
def hib(ban):
    iterasi = 0
    for j in range (len(ban)-1):
        for i in range(len(ban)-1-j):
            if ban[i]>ban[i+1]:
                ban[i],ban[i+1]=ban[i+1],ban[i]
        iterasi+=1
        print(iterasi, ban)
ban = [9,17,2,42,1,7,3,4,67]
print('data yang akan di sort :' , ban)
print('bubble sort : ')
hib(ban)
'''
'''
#selection short
def ss(list):
    iterasi = 0
    for i in range(len(list)-1):
        minimal = i
        for j in range(i+1,len(list)):
            if list[j] < list[minimal]:
                minimal = j
        iterasi += 1
        list[minimal],list[i]=list[i], list[minimal]
        print(iterasi, list)
list=[98,6,33,11,57,33,44,55,29,76,60,81]
print('Data yang akan di sort :', list )
print('Selection Sort :')
ss(list)
'''
'''
#insertion short
def insertion(list):
    for j in range(len(list)-1,-1,-1):
        value = list[j]
        hole = j
        while hole <(len(list)-1) and list[hole+1]>list[hole]:
            list[hole] = list[hole+1]
            hole = hole+1
            list[hole] = value
        print(list)
list = [2,54,38,76,23,56,84,90]
print("Data yang akan di sort", list)
print("Insertion Sort :")
insertion(list)
'''
'''
def quickshort(a,start,end):
    if start<end:
        pindex = partition(a,start,end)
        quickshort(a,start,pindex-1)
        quickshort(a,pindex+1,end)
 
def partition(a,start,end):
    middle = int(end/2)
    pivot = a[middle]
    pindex = start
    for i in range(start,middle):
        if a[i]>=pivot:
            a[i],a[pindex]=a[pindex],a[i]
            pindex = pindex + 1
    a[pindex],a[middle]=a[middle],a[pindex]
    print(a)
    return pindex
 
a = [68,90,78,44,34,20,100,56,34,2]
quickshort(a,0,len(a)-1)
'''
'''
def mergesort(a):
    print('memecah',a)
    n=len(a)
    if n<2:
        return a
    else:
        mid=n//2
        left=a[:mid]
        right=a[mid:]
 
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while i< len(left) and j<len(right):
            if left[i]>right[j]:
                a[k]=left[i]
                i=i+1
            else:
                a[k]=right[j]
                j=j+1
            k=k+1
        while i<len(left):
            a[k]=left[i]
            i=i+1
            k=k+1
        while j<len(right):
            a[k]=right[j]
            j=j+1
            k=k+1
    print('menggabungkan',a)
    '''


def merge_sort(list_bilangan):
  jumlah_bilangan =  len(list_bilangan)
  if jumlah_bilangan > 1:
    posisi_tengah = len(list_bilangan)//2
    potongan_kiri = list_bilangan[:posisi_tengah]
    potongan_kanan = list_bilangan[posisi_tengah:]
    
    merge_sort(potongan_kiri)
    merge_sort(potongan_kanan)

    jumlah_bilangan_kiri = len(potongan_kiri)
    jumlah_bilangan_kanan = len(potongan_kanan)
    c_all,c_kiri,c_kanan = 0,0,0 # pencacah/counter
    print('Sebelum merge:',list_bilangan)  
    print('Potongan sebelum merge:',potongan_kiri,':',potongan_kanan)
    while c_kiri < jumlah_bilangan_kiri or c_kanan < jumlah_bilangan_kanan:
      if c_kiri == jumlah_bilangan_kiri: # elemen di potongan kiri habis
        list_bilangan[c_all] = potongan_kanan[c_kanan]
        c_kanan = c_kanan + 1
      elif c_kanan == jumlah_bilangan_kanan: # elemen di potongan kanan habis
        list_bilangan[c_all] = potongan_kiri[c_kiri]
        c_kiri = c_kiri + 1
      elif potongan_kiri[c_kiri] <= potongan_kanan[c_kanan]: # nilai elemen di potongan kiri lebih kecil
        list_bilangan[c_all] = potongan_kiri[c_kiri]
        c_kiri = c_kiri + 1
      else: # nilai elemen di potongan kanan lebih besar
        list_bilangan[c_all] = potongan_kanan[c_kanan]
        c_kanan = c_kanan + 1
      c_all = c_all + 1
    print('Setelah merge:', list_bilangan)
    print()
          
angka = [6,5,3,1,8,7,2,4]
print('Sebelum sort:',angka)
merge_sort(angka)
print('Setelah sort:',angka)
>>>>>>> 77538eeb8a1ceb3f44bff14194f997772003ca65
