# -*- coding:utf-8 -*-
import requests
import json
import random
import time

class LagouSpider(object):
    def __init__(self):
        self.base_url = "https://www.lagou.com/jobs/positionAjax.json?"
        self.proxy_list = []
        self.headers = {
                       # 反爬点1：检查Referer值，必须是一个合理值
                        "Referer":"https://www.lagou.com/jobs/list_python?px=default&xl=%E6%9C%AC%E7%A7%91&city=%E5%8C%97%E4%BA%AC&district=%E6%B5%B7%E6%B7%80%E5%8C%BA",
                        # 2. 反爬点2：User-Agent
                        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0;WOW64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/62.0.3202.89 Safari/537.36",
        }
        self.position = raw_input("请输入需要抓取的职位名")
        self.city = raw_input("请输入需要抓取的城市名")
        self.page = int(raw_input("请输入需要抓取的页数"))
        self.pn =  1

    def load_page(self):
        "载入页面"
        # post参数
        params = {
            "px": "default",
            "city": "北京",
            "needAddtonalResult": "false",
            "isSchoolJob": "0",
        }
        # 表单数据
        data = {
            "first": "true",
            "pn": self.pn,
            "kd": self.position,
        }
        # 发起请求
        try:
            print "[INFO] 正在抓取第%d页" %self.pn
            json_obj = requests.post(self.base_url, params=params,
                                     data=data, headers = self.headers).json()
            for temp in json_obj["content"]["positionResult"]["result"]:
                for (key, value) in temp.items():
                    print key, value
                print "**************************************"


        except Exception as e:
            print e
            print "发送请求失败"
        


    def write_page(self):
        pass

    def run(self):
        for temp in range(1, self.page+1):
            self.pn = temp
            self.load_page()
            time.sleep(random.randint(1, 5))

if __name__ == "__main__":
    lagou_spider = LagouSpider()
    lagou_spider.run()

    
