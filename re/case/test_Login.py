import requests
import unittest
import data.getcofig as get
from data import logger

class TEST(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
    def test_name(self):
        '''测试登录'''
        self.url = 'http://test.cwty.bet/api/Account/Login'
        self.headers = get.get_header()
        self.data = {"membername": "11",
                    "password": "123456",
                    "clienttype": 1}
        r = requests.post(url=self.url,json=self.data,headers=self.headers)
        self.log.info("响应内容为%s"%r.json())
        self.log.info("响应状态码为%s"%r.status_code)

if __name__== '__main__':
    unittest.main()