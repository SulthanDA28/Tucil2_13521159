import random
import platform
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


class Point:
    def __init__(self):
        self.arr=[]
    def __lt__(self,other):
        return self.arr[0] < other.arr[0] 
    def __le__(self,other):
        return self.arr[0] <= other.arr[0]
    def __eq__(self,other):
        sama = True
        for i in range(len(self.arr)):
            if(self.arr[i]!=other.arr[i]):
                sama = False
                break
        return sama
    

def distance(P,Q):
    hasil = 0
    for i in range(len(P.arr)):
        hasil += (P.arr[i]-Q.arr[i])**2
    akhir = hasil**(0.5)
    return akhir

def mergeSort(x):
    if(len(x)>1):
        tengah = len(x)//2
        kiri = x[:tengah]
        kanan = x[tengah:]
        mergeSort(kanan)
        mergeSort(kiri)
        i = 0
        j = 0
        k = 0
        while(i<len(kiri) and j<len(kanan)):
            if(kiri[i]<=kanan[j]):
                x[k] = kiri[i]
                i+=1
            else:
                x[k] = kanan[j]
                j+=1
            k+=1
        while i<len(kiri):
            x[k] = kiri[i]
            i+=1
            k+=1
        while j<len(kanan):
            x[k] = kanan[j]
            j+=1
            k+=1


def bruteForceDistance(P):
    minim = float("inf")
    count = 0
    start = time.time()
    minimkoor1 = Point()
    minimkoor2 = Point()
    for i in range(len(P)):
        for j in range(len(P)):
            if(i==j):
                continue
            else:
                count+=1
                hitung = distance(P[i],P[j])
                if(minim>hitung):
                    minim = hitung
                    minimkoor1 = P[i]
                    minimkoor2 = P[j]
    end = time.time()
    waktu = end-start
    return minim,waktu,minimkoor1,minimkoor2,count



def threepoint(arr):
    min12 = distance(arr[0],arr[1])
    min23 = distance(arr[1],arr[2])
    min13 = distance(arr[0],arr[2])
    minakhir = min(min12,min23,min13)
    return minakhir

def cariTengah(arr,minsmntr):
    batas = 0
    if(len(arr)%2==1):
        batas = arr[len(arr)//2].arr[0]
    else:
        batas = (arr[len(arr)//2-1].arr[0] + arr[(len(arr)//2)].arr[0])/2
    batasbawah = batas - minsmntr
    batasatas = batas + minsmntr
    termasuk = []
    for i in range (len(arr)):
        if(arr[i].arr[0]>batasbawah and arr[i].arr[0]<batasatas):
            termasuk.append(arr[i])
    return termasuk

def minTengah(arrtengah):
    global count
    minim = float("inf")
    for i in range(len(arrtengah)):
        for j in range(i+1,len(arrtengah)):
            count+=1
            jarak2titik = distance(arrtengah[i],arrtengah[j])
            if(minim>jarak2titik):
                minim =  jarak2titik
    return minim
def dividenConquer(arr):
    global count
    if(len(arr)==3):
        return threepoint(arr)
    elif(len(arr)==2):
        count+=1
        return distance(arr[0],arr[1])
    else:
        bagi2 = len(arr)//2
        kiri = arr[:bagi2]
        kanan = arr[bagi2:]
        hasilkanan = dividenConquer(kanan)
        hasilkiri = dividenConquer(kiri)
        minim = min(hasilkanan,hasilkiri)
        tengaharr = cariTengah(arr,minim)
        hasilmintengah = minTengah(tengaharr)
        hasilakhir = min(minim,hasilmintengah)
        return hasilakhir



#-----------------------------
#--------Hitung Hitung--------
#-----------------------------


print("██████╗░██████╗░  ░█████╗░██╗░░░░░░█████╗░░██████╗███████╗░██████╗████████╗  ██████╗░░█████╗░██╗███╗░░██╗████████╗")
print("╚════██╗██╔══██╗  ██╔══██╗██║░░░░░██╔══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝  ██╔══██╗██╔══██╗██║████╗░██║╚══██╔══╝")
print("░█████╔╝██║░░██║  ██║░░╚═╝██║░░░░░██║░░██║╚█████╗░█████╗░░╚█████╗░░░░██║░░░  ██████╔╝██║░░██║██║██╔██╗██║░░░██║░░░")
print("░╚═══██╗██║░░██║  ██║░░██╗██║░░░░░██║░░██║░╚═══██╗██╔══╝░░░╚═══██╗░░░██║░░░  ██╔═══╝░██║░░██║██║██║╚████║░░░██║░░░")
print("██████╔╝██████╔╝  ╚█████╔╝███████╗╚█████╔╝██████╔╝███████╗██████╔╝░░░██║░░░  ██║░░░░░╚█████╔╝██║██║░╚███║░░░██║░░░")
print("╚═════╝░╚═════╝░  ░╚════╝░╚══════╝░╚════╝░╚═════╝░╚══════╝╚═════╝░░░░╚═╝░░░  ╚═╝░░░░░░╚════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░")


count = 0
print("Selamat datang di 3D Closest Point")
print("Berikut Spesifikasi Sistem Anda:")
my_system = platform.uname()
 
print(f"System: {my_system.system}")
print(f"Node Name: {my_system.node}")
print(f"Release: {my_system.release}")
print(f"Version: {my_system.version}")
print(f"Machine: {my_system.machine}")
print(f"Processor: {my_system.processor}")
print("\n")
banyakinput = int(input("Masukkan banyak titik yang akan diuji = "))
while(banyakinput<=1):
    print("Masukan salah, input harus lebih dari 1")
    banyakinput = int(input("Masukkan banyak titik yang akan diuji = "))
banyakdimns = int(input("Masukkan banyak dimensi yang ingin diuji = "))
while(banyakdimns<1):
    print("Masukan salah, input harus lebih dari 0")
    banyakdimns = int(input("Masukkan banyak dimensi yang ingin diuji = "))
listpoint = []
titik = Point()
for i in range(banyakinput):
    for j in range(banyakdimns):
        rand = random.randint(-100000,100000)
        titik.arr.append(rand)
    listpoint.append(titik)
    titik = Point()
mergeSort(listpoint)
start = time.time()
hasildnc = dividenConquer(listpoint)
end = time.time()
waktudnc = end-start
print("Jarak terdekat antar titik yang ditemukan : ")
print("----------------Divide and Conquer----------------")
print("Divide and Conquer =",hasildnc)
print("Time Execution =",waktudnc)
print("Banyak operasi =",count)
print("-------------------Brute Force--------------------")
print("Sebentar,lagi ngitung yang bruteforce :D")
hasilbruteForce,waktu,koor1,koor2,oprbrt = bruteForceDistance(listpoint)
print("Brute Force =",hasilbruteForce)
print("Time Execution =",waktu)
print("Banyak operasi =",oprbrt)
print("--------------------------------------------------")
print("Sepasang titik terdekat:")
print("Titik 1 =",koor1.arr)
print("Titik 2 =",koor2.arr)

if(banyakdimns == 3):
    tanya = input("Apakah ingin melihat plot dari titik titik tersebut(y/n)=")
    if(tanya=='y' or tanya=='Y'):
        listx = []
        listy = []
        listz = []

        for i in range(len(listpoint)):
            if(listpoint[i]==koor1 or listpoint[i]==koor2):
                continue
            else:
                listx.append(listpoint[i].arr[0])
                listy.append(listpoint[i].arr[1])
                listz.append(listpoint[i].arr[2])

        numx = np.array(listx)
        numy = np.array(listy)
        numz = np.array(listz)

        hasilkoorx = np.array([koor1.arr[0],koor2.arr[0]])
        hasilkoory = np.array([koor1.arr[1],koor2.arr[1]])
        hasilkoorz = np.array([koor1.arr[2],koor2.arr[2]])

        fig = plt.figure()

        project  =fig.add_subplot(121,projection = "3d")
        project.set_title("All Points")
        project.scatter(hasilkoorx,hasilkoory,hasilkoorz,c = "b")
        project.scatter(numx,numy,numz,c = "r")
        project.plot(hasilkoorx,hasilkoory,hasilkoorz,c = "b")

        project2  =fig.add_subplot(122,projection = "3d")
        project2.set_title("2 Point Nearest")
        project2.scatter(hasilkoorx,hasilkoory,hasilkoorz,c = "b")
        project2.plot(hasilkoorx,hasilkoory,hasilkoorz,c = "b")

        plt.show()
    else:
        print("Ok, titik titik tidak diplotkan. Program telah berakhir")
else:
    print("Karena banyak dimensi tidak sama dengan 3, maka titik titik tidak dapat diplot")

