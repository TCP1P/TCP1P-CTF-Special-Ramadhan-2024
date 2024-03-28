# euclid's apprentice

### Description

**Author: k1nomi**

Pengetahuan yang baik dalam modular arithmetic akan sangat membantumu dalam crypto, terutama dalam memahami beberapa algoritma seperti RSA dan Diffie-Hellman. Kalau begitu, mari mulai dari basic-nya. Zaman dahulu kala, Euclid menemukan sebuah cara untuk menghitung faktor persekutuan terbesar/greatest common divisor (GCD) dari dua bilangan bulat `a` dan `b` dengan cepat (Euclidean algortihm). 

Memperluas algoritmanya (Extended euclidean algorithm), kita juga bisa menemukan bilangan bulat `x` dan `y` yang memenuhi `ax + by = gcd(a,b)`.

Hints:
- angka `23` dan getPrime(216) itu konstanta random, tidak perlu dipikirkan
- ingat baik-baik apa output yang diberikan gcd() dan egcd() 

## Attachments
- `chall.py`
- `output.txt`

### Flag
`TCP1P{eucl1de4n_alg0r1thmmmm_4ndd_b3z0utsss_1d3ntityyyy}`

### Proof of Concept
- ambil `gcd(c1,c2)`, didapat `m1` --> flag part 1
- ambil `egcd(c1,c2)`, didapat `x` dan `y`
- hitung `c3 // (x*y)`, didapat `m2` --> flag part 2
