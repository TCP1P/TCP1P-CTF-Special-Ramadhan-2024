# ret2win 3

## Description
Salah satu mitigasi dari buffer overflow di stack adalah canary. Canary adalah 8 byte random yang diletakkan sebelum saved RBP. Jadi, kalau kita overwrite saved RIP menggunakan buffer overflow, canary pasti akan ikut berubah. Canary akan diperiksa oleh program setiap sebelum keluar fungsi dan kalau canary-nya berubah dari sebelumnya, berarti telah terjadi buffer overflow dan program akan dihentikan. Tetapi, kalau kita tau canary-nya, kita tinggal meletakkannya di payload kita pada offset yang sesuai.

## Flag
`TCP1P{gimana_rasanya_ngebypass_mitigasi_pertama_bang}`
