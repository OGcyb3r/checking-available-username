#!/usr/bin/env python
import requests
import threading
import thread
import os

def clearme():
    cce = 'clear'
    os.system(cce)
def maino():
    clearme()
    print(("""
\x1b[30;38;5;197m#\x1b[0mSCchecker
\x1b[1;38;5;238mhttps://github.com/OGcyb3r/p4p/blob/master/userloot.txt\x1b[0m
"""))
    usernamelist = raw_input("\x1b[1;37m#Enter usernames file\x1b[0m : ")
    checkedUsername = open(usernamelist, "r")
    headers = {
    "User-Agent": "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.67 Safari/536.11",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://accounts.snapchat.com/",
    "Cookie": "xsrf_token=a-mMpU6dwym43afgEibJnw; web_client_id=12966659-1ddb-4d0b-8c4c-e39610ddf0f8; _sca={%22cid%22:%2235552e94-28cd-46fc-bf26-b220994ae1d7%22%2C%22token%22:%22v1.key.2018-05-23_8lt9BOpW.iv.ykqLG02DA/OtGORO.j0/QFbsqE82bUtb8Qa0jO6//zEXiS4ZQT4tYissWzZ42fsdCsi8fl7Hy2bEHDm3hs1Li8jciZDbraK3xOUQoTk21tiPgsPcMQvecgafXovbGZOKh%22}; _scid=f2fd66fb-9e11-44d8-a36f-75d807b8d061; sc_at=v2|H4sIAAAAAAAAADNITjFJNjcz100zNjTVNTE2M9RNtDAz1k1NtjAzMU01TElKSqoxNDKwMjQ1NQZKA0VrkJgGAGh4Yl9AAAAA; _sctr=1|1553400000000; oauth_client_id=scan",
    "Connection": "close",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
    }
    url = "https://accounts.snapchat.com/accounts/get_username_suggestions"
    for rew in checkedUsername:
        data = "requested_username="+rew+"&xsrf_token=a-mMpU6dwym43afgEibJnw"
        url = "https://accounts.snapchat.com/accounts/get_username_suggestions"
        request = requests.post(url, headers=headers, data=data)
        po = request.content
        if "OK" in po:
            print(("""[ + ] \x1b[30;38;5;119mSnapchat account is available \x1b[0m: %s"""%(rew)))
            file = open("available.txt", "a+")
            file.write("[+] %s , %s" %(rew,po))
            file.close()
        elif "TAKEN" in po:
            print(("""[ - ] \x1b[30;38;5;197mSnapchat account is token \x1b[0m: %s"""%(rew)))
            file = open("token.txt", "a+")
            file.write("[-] %s , %s" %(rew,po))
            file.close()
        else:
            print(("""[ ! ] \x1b[30;38;5;160maccount being permanently locked or deleted \x1b[0m: %s"""%(rew)))
            file = open("deleted.txt", "a+")
            file.write("[!] %s , %s" %(rew,po))
            file.close()

t1 = threading.Thread(target=maino())
t1.start()
