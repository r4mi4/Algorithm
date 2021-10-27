"""
    ontime pad cipher 
"""
import random

class OneTime:
    def encriypt(self,text):
        plain = [ord(i) for i in text] 
        key = []
        cipher = []
        for i in plain:
            k = random.randint(1,300)
            c = (i+k) * k
            key.append(k)
            cipher.append(c)
        return cipher, key

    def decriypt(self,cipher,key):
        plain = []
        for i in range(len(key)):
            p = int((cipher[i] - key[i]**2)/key[i])
            plain.append(p)
        result = ''.join(chr(i) for i in plain)
        return result

cipher, key = OneTime().encriypt('ramin')
print(cipher,key)
de = OneTime().decriypt(cipher,key)
print(de)