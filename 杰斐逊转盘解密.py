
char = "ZWAXJGDLUBVIQHKYPNTCRMOSFE<<KPBELNACZDTRXMJQOYHGVSFUWI<<BDMAIZVRNSJUWFHTEQGYXPLOCK<<RPLNDVHGFCUKTEBSXQYIZMJWAO<<IHFRLABEUOTSGJVDKCPMNZQWXY<<AMKGHIWPNYCJBFZDRUSLOQXVET<<GWTHSPYBXIZULVKMRAFDCEONJQ<<NOZUTWDCVRJLXKISEFAPMYGHBQ<<QWATDSRFHENYVUBMCOIKZGJXPL<<WABMCXPLTDSRJQZGOIKFHENYVU<<XPLTDAOIKFZGHENYSRUBMCQWVJ<<TDSWAYXPLVUBOIKZGJRFHENMCQ<<BMCSRFHLTDENQWAOXPYVUIKZGJ<<XPHKZGJTDSENYVUBMLAOIRFCQW"

miyao = [2,5,1,3,6,4,9,7,8,14,10,13,11,12]
miwen = "HCBTSXWCRQGLES"

char_array = char.split('<<')
i = 0
result = ""
for n in miyao:
    str = char_array[n-1]
    s = miwen[i]

    postion = str.index(s) # 找到 密文字符在 字符串中的位置
    str1 = str[:postion]   # 截取前半部分字符串
    str2 = str[postion:] # 截取后后半部分字符串
    new_str = str2 + str1  #生成新的字符串
    i +=1
    result += new_str[-6]  #这里是根据输出的字符串 看到倒数第 6 列 是flag 才决定提取每一行的 倒数第6个字符
    print(new_str + "\n")

print("flag{" + result.lower() +  "}") #输出flag



