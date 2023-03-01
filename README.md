# Tucil2_13521159
## Tugas Kecil Strategi Algoritma IF-2211
### Pencarian Titik Terdekat pada Bidang 3 Dimensi Dengan Algoritma Divide and Conquer

<br>

 Disusun oleh:
 - Sulthan Dzaky Alfaro
 - 13521159
 - K1

<br>

## Penerapan Algoritma Divide and Conquer pada Pencarian Titik Terdekat

<br>

Algoritma Divide and Conquer adalah algoritma yang memecah-mecah suatu persoalan menjadi bagian yang kecil sehingga mudah untuk diselesaikan. Setelah memecah-mecah persoalan, hasil solusi dari persoalan yang telah dipecah tadi akan digabungkan dan di cari solusi yang terbaik. Penerapan algoritma divide and conquer pada pencarian pasangan titik terdekat pada bidang 3 dimensi dilakukan dengan cara membagi menjadi 2 daerah yang berisi titik titik yang banyaknya n/2 dari total n pada tiap daerah. daerah yang sudah dibagi tadi dibagi menjadi 2 lagi dan seterusnya secara rekursif sampai daerah berisi 2 titik saja atau 3 jika ganjil. Lalu cari jarak antara 2 titik tersebut atau cari jarak yang terkecil apabila ada 3 titik. Lalu bandingkan jarak tersebut dengan jarak daerah sebelahnya dan cari yang minimum(daerah yang terbagi lainnya). Begitu seterusnya sampai mendapat jarak minimum sementara, misal d. Setelah itu cek juga titik titik yang berada didaerah pembagi 2 misal pembagi pada garis L. Daerah yang dimaksud adalah pada L sepanjang d kekiri dan d kekanan. Cek tiap titik yang ada pada daerah tersebut. Apabila ada yang lebih kecil dari jarak d, maka ambil jarak yang paling kecil. Jadi kesimpulannya adalah ada 3 kemungkinan daerah pasangan titik berada:

<br>

- Pasangan titik berada didaerah kiri pembagi
- Pasangan titik berada didaerah kanan pembagi
- Pasangan titik berada didaerah sekitar pembagi

<br>

## Requirement Untuk Menjalankan Program

<br>

Adapun requirement untuk menjalankan program, yaitu:
- Pastikan sudah menginstall python, karena program menggunakan bahasa python. 
- Apabila sudah menginstall python, pastikan juga sudah menginstall matplotlib pada python. Jika belum, dapat menginstall matplotlib di terminal dengan menuliskan
```
pip install matplotlib
```

<br>

## Cara Menjalankan Program

<br>

Cara menjalankan program 3D Closest Point sebagai berikut:

<br>


- Pertama clone program dari repository ini
- Jika ingin menjalankan program melalui VS Code, buka file src lalu buka file 3Ddistance.py. Run pada file tersebut di VS Code
- Jika ingin langsung memakai di file exe, buka file bin dan jalankan file 3Ddistance.exe
- Jika sudah masuk ke dalam program, program akan meminta banyaknya titik yang akan diuji dan dimensi yang akan diuji
- Apabila sudah menginput, program akan membuat titik titik sebanyak input secara random
- Program akan mencari jarak 2 titik terdekat dengan menggunakan algoritma divide and conquer dan brute force sekaligus banyak operasi dan time execution pada tiap algoritma
- Lalu program akan menanyakan apakah ingin melihat titik titik tersebut ke dalam plot scatter diagram atau tidak.
- Jika iya, tekan y atau Y lalu program akan menampilkan plot semua titik
- Jika tidak, tekan selain y atau Y, program telah berakhir
- Untuk dimensi yang lebih dari 3 atau kirang dari 3, titik titik tidak dapat diplotkan
