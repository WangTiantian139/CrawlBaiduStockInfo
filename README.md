# CrawlBaiduStockInfo
一种从百度股票网站上爬取当日股票信息，并保存到本地以及通过email发送的方法。

## 如何使用
使用Linux的终端运行<code>**CrawBaiduStock.sh**</code>，结果保存在<code>./Cache/</code>和<code>./Backup/</code>目录下，
并生成<code>Crawler-python.log</code>日志文件。

## 关于爬虫
爬取股票信息主要用到python的requests-bs4-re几个库。参考了嵩天老师在中国大学MOOC上的课程[《Python网络爬虫与信息提取》](https://www.icourse163.org/course/BIT-1001870001)

股票名单来自<https://www.banban.cn/gupiao/list_sh.html>, 股票信息来自<https://gupiao.baidu.com/stock/>.

## 关于邮件
在服务器上自动发送邮件需要使用[SendGrid](https://sendgrid.com/)的服务，并在本地部署SendGrid的环境。
详细方法请参阅[sendgrid-python](https://github.com/sendgrid/sendgrid-python "SendGrid的python库")

## 关于定时启动
如果你希望在运行Linux系统的服务器上定时运行这个方法，你可以考虑使用<code>crontab</code>。在终端中运行
<code>
$ crontab -e
</code>
然后在文件的末尾加上
<code>min hour dom mon dow ~/Crawler/CrawBaiduStock.sh >> ~/Crawler/Crawler.log</code>. 
`min` `hour` `dom` `mon` `dow`根据你的需求制定。
具体方式参考<code>crontab</code>的教程。
