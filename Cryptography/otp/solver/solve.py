knownText = bytes.fromhex("36470088ba16f05854a998fc562fa8749e8c26e5dfe0ab08a73bc0e18c86b70b3743038eb519be1555a68df8576aaf7c9ac726ff9ee1ea0fbd3ec7f0848ce2")
text = "dengan menyelesaikan tantangan keamanan dalam tim atau individu"

# recover key dari text yang diketahui yaitu text kedua
key = b""
for i in range(32):
    tmp = knownText[i] ^ ord(text[i])
    key += bytes([tmp])
    
pesan = [
    "315608cfba1cb15950afc1ed5f27ab7483c732e58be1a146b13fc2e78789e5403f470088ae12b91555a68fb9572fb57c99802cea8bffab08f331cbf2889af60d224b028eb5",
    "36470088ba16f05854a998fc562fa8749e8c26e5dfe0ab08a73bc0e18c86b70b3743038eb519be1555a68df8576aaf7c9ac726ff9ee1ea0fbd3ec7f0848ce2",
    "06722dde8b03a00642a293cd5b15b37485b234d492a7a403be0fc5e783b7f3011c7d03dcb51fb55e42b78dd6533eba66c6b82cee8da7a412b234cfe8b29ba61326110392"
    ]

# recover semua pesan dengan key yang sudah ditemukan
for kalimat in pesan:
    result = ""
    j = 0
    for kata in bytes.fromhex(kalimat):
        tmp = key[j % len(key)] ^ kata
        result += chr(tmp)
        j += 1
    print(result)