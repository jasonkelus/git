import requests
import unittest
from data import logger

class TEST(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
    def test_name(self):
        '''测试获取活动类型'''
        self.url = 'http://test.cwty.bet/api/Content/ViewHelp'
        self.data = {"id": 23}
        r = requests.get(url=self.url, params=self.data)
        self.log.info("响应内容为%s"%r.json())
        self.log.info("响应状态码为%s"%r.status_code)

if __name__== '__main__':
    unittest.main()