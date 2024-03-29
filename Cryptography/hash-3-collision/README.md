# Hash: Collision

### Description

**Author: k1nomi**

Aku baru saja membuat sebuah aplikasi yang akan memberikan flag pada user selama user itu telah terdaftar dalam sistem. Di sini aku berikan saja database username dan password mereka hehe. Selama sudah di-hash, password mereka akan aman... kan?

## Attachments
- `server.py`

### Flag

`TCP1P{1_r34lly_h0p3_th4t_y0u_c0ns1der_ab0u7_c0ll1sion5_wh3n_m4k1ng_h4sh_func7i0n5}`

### Proof of Concept
- misal ambil lah hashed password admin
- berdasarkan fungsi my_hash, balikin hash nya ke nilai sum
- cari string yang jumlah ord() nya sama dengan nilai sum (mod 2\*\*24 di sini ga ngaruh karena nilainya masih kecil)
- login admin dengan password string tersebut
- dapat flag
