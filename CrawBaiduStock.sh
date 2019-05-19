#!/bin/sh
echo ''
date
echo 'Crawl'
python3 ~/Crawler/CrawBaiduStock.py >> /home/tiantian/Crawler/Crawler-python.log
echo 'Send Email' 
python3 ~/Crawler/SendBriefing_SendGrid.py >> /home/tiantian/Crawler/Crawler-python.log
