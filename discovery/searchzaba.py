import string
import requests
import sys
import myparser
import re
from bs4 import BeautifulSoup
import json
import json as simplejson



class search_zaba:

    def __init__(self, word, limit):
        self.word = word.replace(' ', '%20')
        self.results = ""
        self.totalresults = ""
        self.server = "www.google.com"
        self.userAgent = "(Mozilla/5.0 (Windows; U; Windows NT 6.0;en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6"
        self.quantity = "100"
        self.limit = int(limit)
        self.counter = 0;
        self.lst=[];
        self.a="hi";

    def do_search(self):
        dat1=[];
        dat2=[];
        dat3=[];
        http_proxy  = "http://*.*.*.*:*"
        https_proxy = "https://*.*.*.*:*"
        ftp_proxy   = "ftp://*.*.*.*:*"

        proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy,
              "ftp"   : ftp_proxy
            }
        self.word=self.word.replace(" ","+");
        try:
            urly="http://www.zabasearch.com/people/" + self.word+"/"
            print urly;
        except Exception, e:
            print e
        try:
            hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'gzip, deflate',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
            r=requests.get(urly,headers=hdr,proxies=proxyDict);
            print urly;
        except Exception,e:
            print e
        self.results = r.content
        print r.text;
        try:
            f = open("data.txt","w")
            f.write(r.text.encode('utf-8'));
            f.close();
        except Exception,e:
            print e;
        try:
            soup = BeautifulSoup(r.text,'html.parser')
            k=soup.find_all("div",{"class":"listing"});
            #p=soup.find_all("p",{"class":"givenName"});
            #s=soup.find_all("span",{"itemprop":"name"});
            #print p;

            for k_it in k:
                try:
                    print k_it;
                    #dat1.append(k_it.contents[0].encode('utf-8'));
                except Exception,e:
                    print e;

                print dat1.append(k_it);

            #for p_item in p:

             #   a=p_item.contents;
             #   print a;
             #   #m=re.search('(https)[^\&]+',a);
             #   #print m.group(0);
             #   dat2.append(a[0]);
            #for s_item in s:
            #    print s_item;
            #    dat3.append(s_item);
        except Exception,e:
            print e;
        try:
            print dat1;
            print dat3;
            lst=self.json_list(dat1);
        except Exception,e:
            print e;
        print k;
        return lst
        #k=soup.findall("div",{"class":"_Rm"});
        #print k;

        self.totalresults += self.results

    def get_people(self):
        rawres = myparser.parser(self.totalresults, self.word)
        return rawres.people_linkedin()

    def process(self):
            lst=self.do_search()
            self.lst=lst;
            return self.lst;




    def json_list(self,list1):
        lst = []
        print len(list1);
        for i in range(0,len(list1)):
            d = {}
            try:
                d['data']=(list1[i])
                lst.append(d)
                print d;
            except Exception,e:
                print e;
        print lst;
        return lst;



