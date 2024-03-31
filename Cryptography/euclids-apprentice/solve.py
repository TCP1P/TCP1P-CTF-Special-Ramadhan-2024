from Crypto.Util.number import *

c1 = 78746519456787459867769556096386983694811384946995098039293792505870820084109642385113547421713999358774318815448856015269135444869248
c2 = 641606793310371792282348958798191776204340201299582820836362981880802983470403505850861414011727894326146227451752569563316980988515
c3 = -109446656897285649835873737145584471533031750955725947474427370335716970042821908651123104671422146210608911142611181104002645674675594082686127882379559257375421942958861654767279681238703674122770550747228463958701474897788409989299339399625811250434222728774602760597218984569772965378966746165388617777229993823306790649199310000

# Euclidean algorithm
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

# Extended euclidean algorithm
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = egcd(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcd, x, y

# First part 
m1 = gcd(c1-23,c2)

# Second part
x = egcd(c1,c2)[1]
y = egcd(c1,c2)[2]
m2 = c3 // (x*y)

print(long_to_bytes(m1) + long_to_bytes(m2))