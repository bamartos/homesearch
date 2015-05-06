# -*- coding: utf-8 -*-

import scrapy
import sys
from time import sleep

#http://www.hemnet.se/mitt_hemnet/sparade_sokningar/7638317
class taNeaSpider(scrapy.Spider):
    name = "homesearch"
    #url = "http://www.tanea.gr/news/articlelist/?pg="
    allowed_domains = ["Hemnet.se"]
    #start_urls = ["http://www.tanea.gr/news/articlelist/?pg=" + str(i) for i in range(1,51)]
    start_urls = ["http://www.hemnet.se/mitt_hemnet/sparade_sokningar/7643475"]
    #start_urls = ["http://www.hemnet.se/mitt_hemnet/sparade_sokningar/7638317"]
    #              "http://www.hemnet.se/mitt_hemnet/sparade_sokningar/7643475"]\
    #search_url = "http://www.hemnet.se/mitt_hemnet/sparade_sokningar/7638317"
    #rest_urls = ["http://www.hemnet.se/resultat?page="+str(i) for i in range(2, getrangeofpages(response)+1)]
    #rest_urls = ["http://www.hemnet.se/resultat?page="+str(i) for i in range(2,20)]
    #start_urls.extend(rest_urls)

#.//*[@id='pagination']/div[2]/a[2]

    def parse(self, response):

        #if response.status == 200:
        #    sys.exit("SHUT DOWN EVERYTHING!")\
        #print "PARSE URL", response.status

        resultpages = self.getrangeofpages(response)
        for i in range(1, resultpages+1):
            print "#"*80
            print 'Page:http://www.hemnet.se/resultat?page='+str(i)
            response = response.replace(response.url="http://www.hemnet.se/resultat?page="+str(i))
            print response.
            print self.parseadds(response)
            print "#"*80


        #add rest result urls
        #print self.start_urls

        # urls
        #print self.getrangeofpages(response), self.start_urls
        #print response
        #print response.xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/div[2]/div/a[3]/span[text()]').extract()
        #Pernw ola ta links katw apo to search
        #/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/div[2]/div/a[2]/span/text()
        #print response.xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/div[2]/div/a/span/text()')[2].extract()
        #Pernw tin timi tou telefteou link (arithmo selidwn)
        #responselist = response.xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/div[2]/div/a')

        #print response.status

        #print responselist, len(responselist)
        #print response.xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/div[2]/div/a').extract()[len(responselist)-1]
        #with open("TaNeaTitles.txt", 'a') as f:
        #    for count in range(1,len(response.xpath('//*[@id=\'roi\']/div[2]/div'))+1):
        #        f.write(response.xpath('//*[@id=\'roi\']//div[2]//div['+str(count)+']//h3//a//@title').extract()[0].encode('utf-8')+'\n')
        #f.close()

    def getrangeofpages(self, response):
        return int(response.xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/div[2]/div/a/span/text()')[2].extract())
        #def parse_page(self, response):
        #    if response.status == 200:
        #        raise scrapy.exceptions.CloseSpider('End of Crawling')

    def parseadds(self, response):
        #print response.xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/ul[2]/li')
        #print response.xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/ul[2]/li/div/@data-item-id/text()')
        #Show pages
        #return response.xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/ul[2]/li[1]/div/ul[1]/li[1]/text()').extract()
        #Get Add id item
        #return  response.xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/ul[2]/li/div/@data-item-id').extract()
        #Get Price
        #responeselist = response.xpath('/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/ul[2]/li/div/ul/li/text()').extract()
        ######################################
        #Take the list of the results
        xpath ='/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/ul/li/div/@data-item-id'
        #xpath = '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/p
        #xpath = '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/ul[2]/li[1]'
        #Price Xpath
        #xpath = '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/ul[2]//li/div/ul/li'
        #Everything Xpath?
        #xpath = '/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/ul[2]/li/div/ul/li'
        #return [x.encode('utf-8') for x in response.xpath(xpath).extract()]
        return response.xpath(xpath).extract()
        #return len(response.xpath(xpath).extract())#[0].encode('utf-8')
        #/html/body/div[1]/div/div[2]/div[2]/div[1]/div[5]/ul[2]/li

"""	title = "**************** OK  ****************"

# -*- coding: utf-8 -*-

import scrapy
import chardet

    def parse(self, response):
        with open("TaNeaTitles", 'w') as f:
            for count in range(1,len(response.xpath('//*[@id=\'roi\']/div[2]/div'))+1):
                title = response.xpath('//*[@id=\'roi\']//div[2]//div['+str(count)+']//h3//a//@title').extract()[0].encode('utf-8')
                f.write(title+'\n')
        f.close()


def parse(self, response):
    #with open("TaNeaTitles", 'wb') as f:
    for count in range(1,len(response.xpath('//*[@id=\'roi\']/div[2]/div'))+1):
        print response.xpath('//*[@id=\'roi\']//div[2]//div['+str(count)+']//h3//a//@title').extract()[0].encode('utf-8')
        #f.write(title)
    #f.close()

	print title
	
    def parse(self, response):
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        print "OK Scrapy"

def parse(self, response):
	for sel in response.xpath('.//*[@id=\'roi\']/div[2]'):
		title = sel.xpath('/div[1]/h3').extract()
        print title
        
def parse(self, response):
	#title = sel.xpath('.//*[@id=\'thesi1\']//div//h1//a').extract()
	#print title
	filename = response.url.split("/")[-2]
	with open(filename, 'wb') as f:
		f.write(response.body)"""
