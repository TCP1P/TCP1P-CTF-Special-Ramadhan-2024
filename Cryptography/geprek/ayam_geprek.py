import os

FLAG = b"redacted"

def generateKey():
    return os.urandom(16)
    
def encrypt(key, plaintext):
    result = b""
    for i in range(len(plaintext)):
        tmp = key[i % len(key)] ^ plaintext[i]
        result += bytes([tmp])
    return result.hex()

def decrypt():
    print("Saya lagi makan ayam geprek")
    print("Jangan diganggu!")

if __name__ == "__main__":
    key = generateKey()
    
    while True:
        try:
            print("pilih opsi:")
            print("1. flag")
            print("2. nyoba enkripsi")
            print("3. menu untuk dekrip")
            choice = int(input("Input: "))
            
            if choice == 1:
                ciphertext = encrypt(key, FLAG)
                print(ciphertext)
                
            elif choice == 2:
                plaintext = input("input pesan kamu dalam bentuk hex: ")
                ciphertext = encrypt(key, bytes.fromhex(plaintext))
                print(f"Hasil= {ciphertext}")
            
            elif choice == 3:
                decrypt()
            
            else:
                raise Exception("Illegal input user!")
            
            print()
        except Exception as e:
            print("terjadi error!\nProgram keluar!")
            break