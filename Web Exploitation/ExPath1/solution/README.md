# Summary 

Di challenge ini kita perlu melakukan exploitasi terhadap sebuah query XPath.

Flag berada pada salah satu username dalam `users.xml`

User diberikan sebuah web yang memungkinkannya untuk mencari username pada dokumen xml. User yang di-input harus sesuai dengan yang ada pada file tersebut, jika terdapat perbedaan maka query akan gagal.

query dilakukan dengan menggunakan unsafe method sebagai berikut

```python
name = request.args.get('name', '')
xpath_query = f"/users/user[username='{name}']"
```

input user langsung dimasukkan kedalam query tanpa sanitasi dan filter sehingga memungkinkan untuk dilakukan injeksi.

Karena kita tidak tahu value dari flag, maka kita bisa menggunakan bantuan `posisition()` untuk melakukan query terhadap node ke-n dari dokumen xml.

dengan menggunakan payload `' or position()=1 or '` maka query akan nampak sepert berikut dan mengeluarkan text node untuk node ke-1.

```xpath
/users/user[username='' or position()=1 or '']
```

dengan konsep ini, kita bisa melakukan leak value flag pada node ke-8 menggunakan payload `' or position()=8 or '`

