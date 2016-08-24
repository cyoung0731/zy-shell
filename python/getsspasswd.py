#coding: utf-8
from bs4 import BeautifulSoup
import urllib2,re,os,shutil,time,datetime

os_encode = 'utf-8'
ss_config_file = 'E:\zcy\gui-config.json'
bak_dir = 'E:\\zcy\\temp'

def getSsPassword():
        url = 'http://www.ishadowsocks.org/'
        response = urllib2.urlopen(url)
        html = response.read()
        #print(html)

        soup = BeautifulSoup(html,"html.parser")
        #print soup.prettify("gbk")

        #找到密码
        servicelist = soup.find_all('div',class_='col-lg-4 text-center')
        for service in servicelist:
                h4 = service.find_all('h4')
                for haha in h4:
                        b_passwd = haha.get_text().encode(os_encode)
                        #b_passwd = haha.get_text()
                        if re.search('B密码',b_passwd):
                                return b_passwd.replace('B密码:','')

#主函数
if __name__ == '__main__':
        print getSsPassword()
#       shutil.copy(ss_config_file, bak_dir)