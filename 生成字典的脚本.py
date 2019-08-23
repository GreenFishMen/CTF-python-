import itertools as its
words="0123456789"
dic=open('dictionary.txt','w')
for num in range(8,9):
    keys=its.product(words,repeat=num)
    for key in keys:
        dic.write("".join(key)+"\n")

dic.close()