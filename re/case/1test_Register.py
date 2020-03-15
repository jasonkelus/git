import requests
import unittest
import data.getcofig as get
from data import logger

class login(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
    def test_Login(self):
        '''注册测试'''
        self.url = 'http://test.cwty.bet/api/Account/Register'
        self.headers = get.get_header()
        self.data = {
                      "clienttype": 0,
                      "password": "123qwe",
                      "cmfpassword": "string",
                      "membername": "clearlove",
                      "captcha": "string",
                      "agent": "string"
                    }
        r = requests.post(url=self.url,json=self.data,headers=self.headers)
        self.log.info("响应内容为%s"%r.json())

if __name__== '__main__':
    unittest.main()