import string
import requests
import sys
import myparser
import re
from bs4 import BeautifulSoup
import json



class search_linkedin:

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
        try:
            urly="http://"+ self.server + "/search?num=50&start=" + str(self.counter) + "&hl=en&meta=&q=site%3Alinkedin.com/in%20" + self.word
        except Exception, e:
            print e
        try:
            hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
            r=requests.get(urly,headers=hdr);
            print urly;
        except Exception,e:
            print e
        self.results = r.content
        #print r.text;
        try:
            f = open("data.txt","w")
            f.write(r.text.encode('utf-8'));
            f.close();
        except Exception,e:
            print e;
        try:
            soup = BeautifulSoup(r.text,'html.parser')
            k=soup.find_all("div",{"class":"f slp"});
            p=soup.find_all("cite",{"class":"_Rm"});
            print p;

            for k_it in k:
                print k_it.contents[0].encode('utf-8');
                dat1.append(k_it.contents[0].encode('utf-8'));
            for p_item in p:

                a=p_item.contents;
                print a;
                #m=re.search('(https)[^\&]+',a);
                #print m.group(0);
                dat2.append(a[0]);
        except Exception,e:
            print e;
        try:
            print dat1;
            print dat2;
            lst=self.json_list(dat2);
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




    def json_list(self,list2):
        lst = []
        print list2;
        print len(list2);
        for ur in list2:
            d = {}
            d['url']=ur
            lst.append(d)
            print d;
        print lst;
        return lst;



