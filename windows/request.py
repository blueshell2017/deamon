#coding:utf-8
import requests
import logging
import time
def recon():
   
    logging.basicConfig(filename='logger.log', level=logging.INFO)
    user_Agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36"
    headers={'User-Agent':user_Agent}
    data = {"DDDDD":"lcl",
            "upass":"12345678",
            "0MKKey":"登陆 Login"}

    try:
        r = requests.get("https://www.baidu.com/",headers=headers,timeout=3)
        logging.info(str(time.localtime(time.time()))+"Every thing is ok")
    except:
        r = requests.post("http://192.168.100.3/", data=data, headers=headers)
        logging.info(str(time.localtime(time.time()))+ str(r.status_code))



recon()