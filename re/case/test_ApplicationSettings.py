import requests
import unittest
import data.getcofig as get
from data import logger

class TEST(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
    def test_name(self):
        '''网站配置信息'''
        self.url = 'http://test.cwty.bet/api/ApplicationSettings'
        r = requests.get('http://test.cwty.bet/api/ApplicationSettings')
        self.log.info("响应内容为%s"%r.json())
        self.log.info("响应状态码%s"%r.status_code)

if __name__== '__main__':
    unittest.main()