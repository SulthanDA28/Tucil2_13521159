import random
import platform
import time
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


class Point:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __lt__(self,other):
        return self.x < other.x 
    def __le__(self,other):
        return self.x <= other.x
    

def distance(P,Q):
    hasil = ((P.x-Q.x)**2+(P.y-Q.y)**2+(P.z-Q.z)**2)**(1/2)
    return hasil

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
    minimkoor1 = Point(x=0,y=0,z=0)
    minimkoor2 = Point(x=0,y=0,z=0)
    for i in range(len(P)):
        for j in range(len(P)):
            if(i==j):
                continue
            else:
                count+=1
                hitung = distance(P[i],P[j])
                if(minim>hitung):
                    minim = hitung
                    minimkoor1 = Point(x=P[i].x,y=P[i].y,z=P[i].z)
                    minimkoor2 = Point(x=P[j].x,y=P[j].y,z=P[j].z)
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
        batas = arr[len(arr)//2].x
    else:
        batas = (arr[len(arr)//2-1].x + arr[(len(arr)//2)].x)/2
    batasbawah = batas - minsmntr
    batasatas = batas + minsmntr
    termasuk = []
    for i in range (len(arr)):
        if(arr[i].x>batasbawah and arr[i].x<batasatas):
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
listpoint = []
for i in range(banyakinput):
    a = random.randint(-100000,100000)
    b = random.randint(-100000,100000)
    c = random.randint(-100000,100000)
    koor = Point(x=a,y=b,z=c)
    listpoint.append(koor)
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
print("Titik 1 = ("+str(koor1.x)+","+str(koor1.y)+","+str(koor1.z)+")")
print("Titik 2 = ("+str(koor2.x)+","+str(koor2.y)+","+str(koor2.z)+")")


tanya = input("Apakah ingin melihat plot dari titik titik tersebut(y/n)=")
if(tanya=='y' or tanya=='Y'):
    listx = []
    listy = []
    listz = []

    for i in range(len(listpoint)):
        if((listpoint[i].x==koor1.x and listpoint[i].y==koor1.y and listpoint[i].z==koor1.z) or (listpoint[i].x==koor2.x and listpoint[i].y==koor2.y and listpoint[i].z==koor2.z)):
            continue
        else:
            listx.append(listpoint[i].x)
            listy.append(listpoint[i].y)
            listz.append(listpoint[i].z)

    numx = np.array(listx)
    numy = np.array(listy)
    numz = np.array(listz)

    hasilkoorx = np.array([koor1.x,koor2.x])
    hasilkoory = np.array([koor1.y,koor2.y])
    hasilkoorz = np.array([koor1.z,koor2.z])

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


