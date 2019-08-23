text = "gndk€rlqhmtkwwp}z"
n =1
t = ''
for i in text:
    t += chr(ord(i)-n)
    n += 1
print(t)