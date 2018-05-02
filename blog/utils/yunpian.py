# -*- coding: utf-8 -*-  
__author__ = 'style'
import requests
import json

class YunPianWang(object):
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def single_send(self, mobile, code):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【style博客】您的验证码是{code}".format(code=code),
        }
        response = requests.post(self.api_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict

if __name__ == '__main__':
    api_key = "453276edf2888acc6137bd8df066cf54"
    api_url = "https://sms.yunpian.com/v2/sms/single_send.json"
    YunPian = YunPianWang(api_url=api_url, api_key=api_key)
    YunPian.single_send(mobile="13209215136", code="654123")
