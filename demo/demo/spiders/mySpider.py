import scrapy
import requests
from demo.items import WeightItem
from bs4 import UnicodeDammit
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from urllib.request import urlopen

'''class MySpider(scrapy.Spider):
    name="mySpider"
    n=1
    #source_url = 'https://www.womenshealthmag.com/weight-loss/'
    source_url='https://www.womenshealthmag.com/ajax/infiniteload/?id=c1a430f8-ff5d-433f-85a4-69ed34d4f0ec&class=CoreModels%5Csections%5CSectionModel&viewset=section&' \
               'page='+n+'&cachebuster='
    def start_requests(self):
        url = MySpider.source_url
        yield scrapy.Request(url=url, callback=self.parse)
        print("发送请求")

    def parse(self, response):
        try:

            dammit = UnicodeDammit(response.body, ["utf-8", "gbk"])
            data = dammit.unicode_markup
            selector = scrapy.Selector(text=data)
            print("收到源代码")
            links = selector.xpath("//div[position()>2][starts-with(@class,'simple-item grid-simple-item ')]/a[@class='simple-item-image item-image']")
            print("主页xpath")
            for link in links:
                newslink = link.xpath("./@href").extract_first()
                yield scrapy.Request(url=MySpider.source_url + newslink, callback=self.parse1)
        except Exception as err:
            print(err)

    def parse1(self,response):
                 dammit = UnicodeDammit(response.body, ["utf-8", "gbk"])
                 data = dammit.unicode_markup
                 selector = scrapy.Selector(text=data)
                 text = selector.xpath("//p[@class='body-text']/text()").extract()
                 text = "\n".join(text)
                 #text = selector.xpath("//p[@class='body-text']/text()")[0]
                 #text = text.xpath("string(.)")
                 pic = selector.xpath("/html/body/div[2]/div[4]/div[1]/div[1]/div/img/@data-src").extract_first()


                 header = selector.xpath("//header[@class='content-header standard-header']/div[@class='content-header-inner']")

                 title = header.xpath(".//h1/text()").extract_first()

                 subtitle = header.xpath(".//p/text()").extract_first()

                 profilephoto = header.xpath(".//img/@data-src").extract_first()

                 author = header.xpath(".//span[@class='byline-name']/text()").extract_first()
                 date = header.xpath(".//time[@class='content-info-date']/text()").extract_first()
                 video=""
                 tag="Weightloss"
                 item = WeightItem()


                 item["title"] = title.strip() if title else ""

                 item["tag"] = tag
                 item["subtitle"] = subtitle.strip() if subtitle else ""

                 item["author"] = author.strip() if author else ""

                 item["date"] = date.strip() if date else ""

                 item["profilephoto"] = profilephoto.strip() if profilephoto else ""

                 item["text"] = text.strip() if text else ""

                 item["pic"] = pic.strip() if pic else ""

                 item["video"]=video.strip()if video else ""

                 yield item
'''
class MySpider(scrapy.Spider):
    name = "mySpider"
    source_url = 'https://www.womenshealthmag.com'

    def start_requests(self):
         url_s='https://www.womenshealthmag.com/ajax/infiniteload/?params=%7B%22id%3Anot-in%22%3A%229a94c0a2-38b0-45bb-9728-613bffa1eacd%22%7D&id=e6d59648-6971-4a94-9937-c60807c5a2a3&class=CoreModels%5Csections%5CSectionModel&viewset=section&' \
               'page='
         url_e='&cachebuster='
         x=0
         while x<190:
          x+=1
          if x<90:

              USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
              url=url_s+str(x)+url_e
              r=requests.get(url,USER_AGENT)
          if x>=90&x<190:
              USER_AGENT='Mozilla / 5.0(Macintosh;Intel Mac OS X 10_14_3) AppleWebKit / 605.1 .15(KHTML, likeGecko) Version / 12.0 .3Safari / 605.1.15'
              url = url_s + str(x) + url_e
              r = requests.get(url, USER_AGENT)


          print(r.status_code)
          selector=scrapy.Selector(text=r.text)
          links=selector.xpath("//div[starts-with(@class,'simple-item grid-simple-item ')]")
          for link in links:
            newslink = link.xpath(".//a[@class='simple-item-image item-image']/@href").extract_first()
            yield scrapy.Request(url=MySpider.source_url+newslink,callback=self.parse1)




    def parse1(self,response):
                 dammit = UnicodeDammit(response.body, ["utf-8", "gbk"])
                 data = dammit.unicode_markup
                 selector = scrapy.Selector(text=data)
                 text = selector.xpath("//p[@class='body-text']/text()").extract()
                 text = "\n".join(text)

                 #text = selector.xpath("//p[@class='body-text']/text()")[0]
                 #text = text.xpath("string(.)")
                 pic = selector.xpath("/html/body/div[2]/div[4]/div[1]/div[1]/div/img/@data-src").extract_first()


                 header = selector.xpath("//header[@class='content-header standard-header']/div[@class='content-header-inner']")

                 title = header.xpath(".//h1/text()").extract_first()

                 subtitle = header.xpath(".//p/text()").extract_first()

                 profilephoto = header.xpath(".//img/@data-src").extract_first()

                 author = header.xpath(".//span[@class='byline-name']/text()").extract_first()
                 date = header.xpath(".//time[@class='content-info-date']/text()").extract_first()
                 video=""

                 tag = "Health"
                 item = WeightItem()

                 item["title"] = title.strip() if title else ""

                 item["tag"] = tag
                 item["subtitle"] = subtitle.strip() if subtitle else ""

                 item["author"] = author.strip() if author else ""

                 item["date"] = date.strip() if date else ""

                 item["profilephoto"] = profilephoto.strip() if profilephoto else ""

                 item["text"] = text.strip() if text else ""

                 item["pic"] = pic.strip() if pic else ""

                 item["video"] = video.strip() if video else ""

                 yield item


















