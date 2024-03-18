# Kriteria Pembuatan Challenge

Berikut adalah kriteria yang harus dipenuhi dalam merancang dan mengevaluasi challenge Capture the Flag (CTF):

## Kriteria Umum TCP1P CTF

- Deskripsi dan hint di tulis dalam bahasa Indonesia.
- Untuk soal yang membutuhkan hosting, wajib menggunakan docker compose. Contoh dari docker compose bisa di cek di [samehadaku-kw-after-ctf](./Web%20Exploitation/samehadaku-kw-after-ctf/)
- Challenge ini akan menggunakan format challenge.yaml [rcds](https://rcds.redpwn.net/en/latest/challenge/) sebagai format pendeployan. Kalian bisa menyelipkan README.md atau membuat challenge.yml kalian sendiri untuk configurasi challenge.
- Hindari penggunaan soal yang mengharuskan menebak (guessing).
- Juga hindari penggunaan soal steganografi yang berhubungan dengan ciphertext. Namun, masih diperbolehkan jika soal steganografi berhubungan dengan pemulihan gambar, disk, zip, atau terkait dengan algoritma.
- Format flag untuk CTF ini `TCP1P{.*}`.
