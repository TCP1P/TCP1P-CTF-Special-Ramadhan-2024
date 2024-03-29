# Hash 1: Intro

### Description

Hashing adalah sebuah metode untuk mengubah data menjadi sebuah string yang panjangnya tetap. Algoritma hash merupakan fungsi satu arah, artinya apabila diberikan hasil hash dari suatu data, akan sangat sulit untuk menerka data aslinya. Oleh karena itu, biasanya password disimpan di database dalam bentuk hash. 

Meskipun begitu, untuk beberapa value hash, kita bisa mengetahui data aslinya menggunakan tool yang tersedia online. Untuk soal ini, cobalah "crack" beberapa value hash MD5 pada `hashes.txt`.

## Attachments
- hashes.txt

### Flag

`TCP1P{d0nt_us3_sh0rt_p4ssw0rds}`

### Proof of Concept
- crack nilai hash tersebut menggunakan online tool seperti crackstation.net
