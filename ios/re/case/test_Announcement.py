import requests
import unittest
import data.getcofig as get
from data import logger

class TEST(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
    def test_name(self):
        '''获取公告信息列表'''
        self.url = 'http://test.cwty.bet/api/Announcement'
        self.headers = get.get_header()
        self.data = {'clienttype': '1'}
        r = requests.get(url=self.url, params=self.data,headers=self.headers)
        self.log.info("响应内容为%s"%r.json())
        self.log.info("响应状态码%s"%r.status_code)
        r.raise_for_status()
if __name__== '__main__':
    unittest.main()