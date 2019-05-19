'''
an additional stock infomation source: http://quote.eastmoney.com/center/gridlist.html#hs_a_board
'''

# %%
import requests
from bs4 import BeautifulSoup
import traceback
import re
import schedule
import time


# %%
def getHTMLText(url, code='utf-8'):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except:
        return ""


def getStockList(lst, stockURL):
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            stock_code = "sh" + re.findall(r"/gupiao/\d{6}", href)[0][-6:]
            lst.append(stock_code)
        except:
            continue


def getStockInfo(lst, stockURL, fpath):

    with open(fpath, 'a', encoding='utf-8') as f:
        f.write("crawler at {}: started\n".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))

    count = 0
    for stock in lst:
        url = stockURL + stock + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            infoDict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stockInfo = soup.find('div', attrs={'class': 'stock-bets'})

            name = stockInfo.find_all(attrs={'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})

            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')

            for i in range(len(keyList)):
                key = keyList[i].text
                val = valueList[i].text
                infoDict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count += 1
                # print("\r当前进度：{:.2f}%".format(count*100/len(lst)), end="")
        except:
            count += 1
            # print("\r当前进度：{:.2f}%".format(count*100/len(lst)), end="")
            continue
    print("crawler at {}: finished".format(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))


def spider():
    # %%
    stock_list_url = 'https://www.banban.cn/gupiao/list_sh.html'
    stock_info_url = 'https://gupiao.baidu.com/stock/'
    output_file = '/home/tiantian/Crawler/Cache/BaiduStockInfo.txt'

    slist = []

    # %%
    getStockList(slist, stock_list_url)
    getStockInfo(slist, stock_info_url, output_file)


if __name__ == "__main__":
    # schedule.every().days.at('10:00').do(spider)
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
    print('running CrawBaiduStock.py')
    spider()
    with open('/home/tiantian/Crawler/Cache/BaiduStockInfo.txt', 'r', encoding='utf-8') as fread:
        print('backup stock information from cache')
        timestick = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
        filename_output = '/home/tiantian/Crawler/Backup/BaiduStockInfo' + '-' + timestick + '.txt'
        with open(filename_output, 'x', encoding='utf-8') as fwrite:
            fwrite.write(fread.read())
            print('backup finished')
    

