# Cryptographer.

![alt text](/doc/header.jpeg "Gasball header")
<center>
Repositori ini merupakan sebuah project aplikasi program yang menyediakan algoritma enkripsi dan dekripsi dari berbagai macam jenis cipher klasik yang dibuat untuk memenuhi tugas II4031 Kriptografi dan Koding

<br>

| NIM      | Nama                      |
| -------- | ------------------------- |
| 18221119 | Natasya Vercelly Harijadi |
| 18221121 | Rozan Ghosani             |

</center>

<p align="center">
  <a href="#about">About</a> |
  <a href="#system-requirement">System Requirements</a> |
  <a href="#installation">Installation</a> |
  <a href="#feature">Feature</a>
</p>

## About

Program ini merupakan program yang menyediakan algoritma enkripsi dan dekripsi dari berbagai macam jenis cipher klasik. Program ini dapat menerima pesan berupa plaintext yang diketikkan dari papan-ketik dan juga file sembarang dengan ekstensi apapun. Program ini dapat mengenkripsi plaintext dengan 26 huruf alfabet, kecuali untuk Extended Vigenere Cipher dan Auto-key Cipher yang dapat mengenkripsi 256 karakter ASCII. Program ini juga dapat mendekripsi kembali ciphertext menjadi plaintext. Hasil dari enkripsi dan dekripsi tersebut ditampilkan dalam bentuk kode Base64.

Enkripsi dan dekripsi yang dilakukan terhadap byte dilakukan dengan cara membaca setiap byte dari file termasuk dengan header dari file. Kemudian byte tersebut akan disimpan kembali dalam format ekstensi yang sama sehingga file tersebut tidak dapat dibuka oleh program apliaksinya. Pada setiap cipher, pengguna dapat memasukan sendiri kunci yang diinginkan.

Program ini ditulis dalam bahasa Python yang dibantu dengan library Flask untuk menampilkan GUI dari program dengan menggunakan HTML.

## System Requirement

- Python 3.8 atau lebih baru.

## Installation

### Cloning repository

1. Pada halaman utama repository [GitHub](https://github.com/zshnrg/tugas-1-kripto), buka menu **Clone** lalu salin URL dari repository
2. Buka Terminal
3. Pindah ke direktori yang diinginkan
4. Ketikan `git clone`, lalu tempelkan URL yang telah disalin tadi 
   ```
   git clone https://github.com/zshnrg/tugas-1-kripto.git
5. Tekan **Enter** untuk membuat *local clone*
   ```
   $ git clone https://github.com/zshnrg/tugas-1-kripto.git
    > Cloning into `tugas-1-kripto`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
   ``` 

### Running the app
1. Jalankan terminal pada repositori
2. Ketikan `python main.py`
3. Tekan **Enter** untuk menjalankan program
    ```
    $ \tugas-1-kripto> python main.py

    [ * ] Checking for required modules...
    [ X ] Flask is not installed. Installing...
    [ v ] All required modules are installed.
    [ * ] Starting the application...
    * Serving Flask app 'app'
    * Debug mode: off
    * Running on http://127.0.0.1:5000
    Press CTRL+C to quit
    ```
4. Halaman [http://127.0.0.1:5000/](http://127.0.0.1:5000/) akan otomatis terbuka.


## Feature
Program ini memiliki fitur:
- Enkripsi dan dekripsi dengan berbagai jenis cipher klasik
- Kustomisasi kunci
- Pengenkripsi dan dekripsian file dan text ketikkan

Berikut merupakan kompabilitas dari algoritma cipher yang tersedia.
<center>

| Algoritma                | Karakter   | Plaintext | File Input |
| ------------------------ | ---------- | --------- | ---------- |
| Vigenere Cipher          | 26 Alfabet | ✔️       | ❌         |
| Extended Vigenere Cipher | 256 ASCII  | ✔️       | ✔️         |
| Playfair Cipher          | 26 Alfabet | ✔️       | ❌         |
| Product Cipher           | 26 Alfabet | ✔️       | ❌         |
| Affine Cipher            | 26 Alfabet | ✔️       | ❌         |
| Auto-key Vigenere Cipher | 256 ASCII  | ✔️       | ✔️         |

</center>