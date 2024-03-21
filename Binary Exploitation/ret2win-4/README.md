# ret2win 4

## Description
Mitigasi lain untuk menyusahkan penyerang dalam mengubah alur program adalah PIE. PIE adalah singkatan dari Position Independent Executable yang mengakibatkan program kita untuk di-load ke dalam memori dengan offset random. Sehingga walaupun terdapat buffer overflow, penyerang tidak mengetahui alamat dari fungsi/instruksi yang ingin dijalankan.

## Flag
`TCP1P{leak_satu_alamat_semua_alamat_ketahuan}`
