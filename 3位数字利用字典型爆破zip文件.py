import zipfile
import os


def main():
    zip = zipfile.ZipFile("C:/Users/HP/Desktop/123.zip", "r", zipfile.zlib.DEFLATED)
    with open("C:/Users/HP/Desktop/password.txt") as f:
        for data in f.readlines():
            try:
                print("\n[+] Trying the password ", data.strip())
                zip.extractall(path="./", pwd=data.strip().encode())
                print("\n[+] The password is", data.strip())
                zip.close()
                return
            except Exception as e:
                print(e)
                pass


if __name__ == '__main__':
    main()