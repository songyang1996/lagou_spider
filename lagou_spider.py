# -*- coding:utf-8 -*-
import requests
import json
import random
import time

class LagouSpider(object):
    def __init__(self):
        self.base_url = "https://www.lagou.com/jobs/positionAjax.json?"
        # 代理池 如果有的话以此字典{"http" :
        # "username:passwd@ip:port"}格式填入下面列表
        # 并使用random.choice随机选择一个
        # 作为requests.post的proxies参数传入 使用代理
        self.proxy_pool = []
        self.headers = {
            "Accept" : "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding" : "gzip, deflate, br",
            "Accept-Language" : "zh-CN,zh;q=0.9,en;q=0.8",
            "Connection" : "keep-alive",
            "Content-Length" : "26",
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie" : "user_trace_token=20170923184359-1ba5fe6f-a04c-11e7-a60e-525400f775ce; LGUID=20170923184359-1ba6010d-a04c-11e7-a60e-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; JSESSIONID=ABAAABAACEBACDGF071FAE6BE1F68696EF4356C16381303; X_HTTP_COOK_CODE=85782; TG-TRACK-CODE=index_search; SEARCH_ID=3f9e61601dc745c39f89855c4ba48fff; _gid=GA1.2.1239271841.1510196816; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1509193471,1509936663,1510196816,1510216967; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1510219012; _ga=GA1.2.136733168.1506163440; LGSID=20171109164247-f6241c4c-c529-11e7-986b-5254005c3644; LGRID=20171109171652-b8fc422e-c52e-11e7-986b-5254005c3644",
            "Host" : "www.lagou.com",
            "Origin" : "https://www.lagou.com",

            # 1 . 反爬点1：检查Referer值，必须是一个合理值
            "Referer" : "https://www.lagou.com/jobs/list_python?px=default&xl=%E6%9C%AC%E7%A7%91&city=%E5%8C%97%E4%BA%AC&district=%E6%B5%B7%E6%B7%80%E5%8C%BA",

            # 2. 反爬点2：User-Agent
            "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36",
            "X-Anit-Forge-Code" : "0",
            "X-Anit-Forge-Token" : "None",
            "X-Requested-With" : "XMLHttpRequest"
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
            "city": self.city,
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
            json_obj = requests.post(self.base_url, params=params,data=data, headers=self.headers).json()
        except Exception as e:
            print e
            print "发送请求失败"
        else:
            return json_obj


    '''
    数据格式
    companySize 150-500人
    firstType 开发/测试/运维类
    appShow 0
    pcShow 0
    positionName C++ 开发工程师
    education 本科
    financeStage 不需要融资
    city 西安
    companyLogo i/image/M00/7D/D6/Cgp3O1hIywmADvhNAAAtD40SLng344.png
    district 户县
    companyId 161330
    explain None
    industryField 企业服务,其他
    createTime 2017-11-10 11:44:55
    positionLables [u'\u9ad8\u7ea7', u'\u8f6f\u4ef6\u5f00\u53d1']
    score 0
    adWord 0
    formatCreateTime 11:44发布
    industryLables []
    salary 8k-12k
    workYear 3-5年
    secondType 软件开发
    jobNature 全职
    deliver 0
    gradeDescription None
    imState disabled
    companyFullName 西安增材制造国家研究院有限公司
    companyLabelList []
    positionId 3373824
    companyShortName 增材制造国家研究院
    isSchoolJob 0
    approve 1
    businessZones None
    plus None
    lastLogin 1510297363000
    positionAdvantage MFC
    publisherId 6596000
    promotionScoreExplain None'''

    def write_page(self, json_obj):
        "读取json对象并写入磁盘文件中"
        item_list = list()
        try:
            for temp in json_obj["content"]["positionResult"]["result"]:
               # for (key, value) in temp.items():
                   # print key, value
                #print "**************************************"
                item = dict()
                item["companyFullName"] = temp["companyFullName"]
                item["salary"] = temp["salary"]
                item["positionName"] = temp["positionName"]
                item["createTime"] = temp["createTime"]
                item_list.append(item)
        except Exception as e:
            print e
            print "[ERROR]数据提取失败"
        else:
            # 写入磁盘
            json.dump(item_list, open("lagou.json", "w"))
            print "[INFO] 写入文件成功"

    def run(self):
        for temp in range(1, self.page+1):
            self.pn = temp
            json_obj = self.load_page()
            time.sleep(random.randint(1, 6))
            self.write_page(json_obj)


if __name__ == "__main__":
    lagou_spider = LagouSpider()
    lagou_spider.run()
 
