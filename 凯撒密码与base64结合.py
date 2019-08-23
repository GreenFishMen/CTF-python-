import base64

text = input("请输入题目密文")
text1 = ''
for i in text:
    t = chr(ord(i) - 4)
    text1 += t

print(text1)
print(base64.b64decode(text1))