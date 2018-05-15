<h1 align="center">
  <br>
  Tugas 1 Seleksi Warga Basdat 2018
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Data Scraping
  <br>
  <br>
</h2>

### Description
Program python yang akan melakukan data-scraping tentang recommended film dari BookMyShow. Setiap film akan diambil data ratingnya dan tiket-tiket yang tersedia untuk film tersebut.


### Specifications

1. Lakukan data scraping dari sebuah laman web untuk memeroleh data atau informasi tertentu __TANPA MENGGUNAKAN API__

2. Daftarkan judul topik yang akan dijadikan bahan data scraping pada spreadsheet berikut: [Topik Data Scraping](http://bit.ly/TopikDataScraping). Usahakan agar tidak ada peserta dengan topik yang sama. Akses edit ke spreadsheet akan ditutup tanggal 10 Mei 2018 pukul 20.00 WIB

3. Dalam mengerjakan tugas 1, calon warga basdat terlebih dahulu melakukan fork project github pada link berikut: https://github.com/wargabasdat/Seleksi-2018/tree/master/Tugas1. Sebelum batas waktu pengumpulan berakhir, calon warga basdat harus sudah melakukan pull request dengan nama ```TUGAS_SELEKSI_1_[NIM]```

4. Pada repository tersebut, calon warga basdat harus mengumpulkan file script dan json hasil data scraping. Repository terdiri dari folder src dan data dimana folder src berisi file script/kode yang __WELL DOCUMENTED dan CLEAN CODE__ sedangkan folder data berisi file json hasil scraper.

5. Peserta juga diminta untuk membuat Makefile sesuai template yang disediakan, sehingga program dengan gampang di-_build_, di-_run_, dan di-_clean_

``` Makefile
all: clean build run

clean: # remove data and binary folder

build: # compile to binary (if you use interpreter, then do not implement it)

run: # run your binary

```

6. Deadline pengumpulan tugas adalah __15 Mei 2018 Pukul 23.59__

7. Tugas 1 akan didemokan oleh masing-masing calon warga basdat

8. Demo tugas mencakup keseluruhan proses data scraping hingga memeroleh data sesuai dengan yang dikumpulkan pada Tugas 1

9. Hasil data scraping ini nantinya akan digunakan sebagai bahan tugas analisis dan visualisasi data

10. Sebagai referensi untuk mengenal data scraping, asisten menyediakan dokumen "Short Guidance To Data Scraping" yang dapat diakses pada link berikut: [Data Scraping Guidance](http://bit.ly/DataScrapingGuidance)

11. Tambahkan juga gitignore pada file atau folder yang tidak perlu di upload, __NB : BINARY TIDAK DIUPLOAD__

12. JSON harus dinormalisasi dan harus di-_preprocessing_
```
Preprocessing contohnya :
- Cleaning
- Parsing
- Transformation
- dan lainnya
```

13. Berikan README yang __WELL DOCUMENTED__ dengan cara __override__ file README.md ini. README harus memuat minimal konten :
```
- Description
- Specification
- How to use
- JSON Structure
- Screenshot program (di-upload pada folder screenshots, di-upload file image nya, dan ditampilkan di dalam README)
- Reference (Library used, etc)
- Author
```

### How To Use
Windows:
1. Open terminal in src directories
2. Run the program with command "python scrape.py"

Linux/Ubuntu:
1. Open terminal in task directories
2. make the Makefile with command "make"

### Json Structure
Each tuple of item data contains :
1. Judul film
2. Nilai suka pengguna
3. Rating pengguna dari bintang 1 ke 5
4. Info bioskop yang menayangkan film tersebut, terdiri dari :
	1. Nama bioskop
	2. Waktu, harga, dan tipe studio dari tiket film tersebut


### Screenshot
Screenshot 1
![alt_text](https://github.com/NPP0804/Seleksi-2018/blob/master/Tugas1/screenshots/sc1.jpg)
Screenshot 2
![alt_text](https://github.com/NPP0804/Seleksi-2018/blob/master/Tugas1/screenshots/sc2.jpg)
Screenshot 3
![alt_text](https://github.com/NPP0804/Seleksi-2018/blob/master/Tugas1/screenshots/sc3.jpg)
Screenshot 4
![alt_text](https://github.com/NPP0804/Seleksi-2018/blob/master/Tugas1/screenshots/sc4.jpg)


### Reference
Library that I used:
1. BeautifulSoup4 for html parser
2. time for sleep command
3. json for cleaning and writing json file
4. requests for getting the html script from url

### Author
Nama	: 	Naufal Putra Pamungkas <br>
Email	:	ajienaufal0804@gmail.com
			13516110@std.stei.itb.ac.id
