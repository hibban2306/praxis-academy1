def bubble_short () :{

    def hib(ban) :
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
    hib(ban) }

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
