# lagou_spider
## 拉钩网爬虫 python2.7 requests 暂未添加数据保存方式 在下个版本更新
##### 拉钩网采用前后端分离框架 数据获取的接口为https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0
##### 拉钩网的反爬机制
##### 1.检测请求报头的ua,验证是否为浏览器用户
##### 2.检测请求报头的Referer项，判断请求json的来源
##### 3.记录同一IP的请求次数 （解决方案为使用代理池 设定请求延时时间）
##### 爬虫程序具有时效性 可能会因为网站更换了反扒机制导致爬虫运行不成功 我以后会即时更新程序

