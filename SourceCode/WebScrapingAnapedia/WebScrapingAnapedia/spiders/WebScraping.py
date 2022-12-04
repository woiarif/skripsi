import scrapy
import re
from urllib.parse import urlparse
#from six.moves.urllib.parse import urlparse


class BlogSpider(scrapy.Spider):
    name = 'crawlerAnapedia'
    start_urls = []
    allowed_domains = []

    
    def __init__(self, **kw):
        super(BlogSpider, self).__init__(**kw)
        url = kw.get('url') or kw.get('domain')
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://%s/' % url
        self.url = url
        self.start_urls = [url]
        self.allowed_domains = [re.sub(r'^www\.', '', urlparse(url).hostname)]


    def parse(self, response):
        linkpage = response.request.url

        if linkpage.find('ceritaanak.org')!=-1:
            p = response.css('div.entry-content > p ::text').extract()
        
        elif linkpage.find('dongengceritarakyat.com')!=-1:
            p = response.css('div.entry-content > p ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()

        elif linkpage.find('inibudi.org')!=-1:
            p = response.css('div.entry-content > p ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()
        
        elif linkpage.find('squline.com')!=-1:
            p = response.css('div.post-content > p ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()

        elif linkpage.find('liburananak.com')!=-1:
            p = response.css('div.content-article > p ::text').extract()
            img = response.xpath('//img[@class="img-responsive"]/@src').get()
        
        elif linkpage.find('bimba-aiueo.com')!=-1:
            p = response.css('div.czr-wp-the-content > p ::text').extract()
            img = response.xpath('//div[@class="czr-wp-the-content"]//img/@data-src').get()

        elif linkpage.find('id.kumonglobal.com')!=-1:
            p = response.css('div.postcontent > p ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()
        
        elif linkpage.find('bobo.grid.id')!=-1:
            bobo = response.css('ul.breadcrumb__wrap > li.breadcrumb__item > a.pink ::text').getall()
            bobotxt = ' '.join(bobo)
            if bobotxt.find('SEKOLAH')!=-1:
                p = response.css('div.read__right.read__article > p ::text').extract()
                img = response.xpath('//meta[@property="og:image"]/@content').get()
            else:
                p = None

        elif linkpage.find('sahabatanak.org')!=-1:
            p = response.css('div.content_boxes > p ::text').extract()
            img = response.xpath('//div[@class="content_boxes"]//img/@src').get()

        elif linkpage.find('dongeng.org')!=-1:
            p = response.css('div.post-single-content.box.mark-links > p ::text').extract()
            img = response.xpath('//div[@class="post-single-content box mark-links"]//img/@src').get()
            if str(img).find("-150x150")!=-1:
                img = str(img).replace("-150x150", "")

        elif linkpage.find('biologiedukasi.com')!=-1:
            p = response.css('div.post-body.entry-content ::text').extract()
            img = response.xpath('//div[@class="post-body entry-content"]//img/@src').get()

        elif linkpage.find('waktuku.com')!=-1:
           #p = response.css('div.td-post-content.tagdiv-type > p ::text').extract()
            p = response.xpath('//div[@class="td-post-content tagdiv-type"]//p/text()').extract()
            img = response.xpath('//div[@class="td-post-content tagdiv-type"]//img/@data-src').get()
        
        elif linkpage.find('suaraedukasi.kemdikbud.go.id')!=-1:
            p = response.css('div.pb-12 > p ::text').extract()
            img = response.xpath('//div[@class="pb-12"]//img/@src').get()


        elif linkpage.find('amiroh.web.id')!=-1:
            p = response.css('div.entry-inner > p ::text').extract()
            img = response.xpath('//div[@class="entry-inner"]//img/@src').get()

        elif linkpage.find('rumahinspirasi.com')!=-1:
            rumahinspirasi = response.css('span.elementor-post-info__terms-list > a.elementor-post-info__terms-list-item ::text').getall()
            rumahinspirasitxt = ' '.join(rumahinspirasi)
            if rumahinspirasitxt.find('Artikel')!=-1:
                p = response.css('div.elementor-widget-container > p ::text').extract()
                img = response.xpath('//figure[@class="wp-caption"]//img/@src').get()
            else:
                p = None
            
        elif linkpage.find('radioedukasi.kemdikbud.go.id')!=-1:
            radioedukasi = response.css('ul.breadcrumb > li ::text').getall()
            radioedukasitxt = ' '.join(radioedukasi)
            if radioedukasitxt.find('Berita Pendidikan')!=-1:
                p = response.css('div.content > div.page-content > p ::text').extract()
                img = response.xpath('//div[@class="post-head"]//img/@src').get()
            else:
                p = None
        elif linkpage.find('museumnasional.or.id')!=-1:
            p = response.css('div.td-post-content > p ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()

        elif linkpage.find('makinpintar.com')!=-1:
            p = response.css('article.prose > p ::text').extract()
            
        elif linkpage.find('zenius.net')!=-1:
            p = response.css('div.entry-content > p ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()

        elif linkpage.find('ruangguru.com')!=-1:
            p = response.css('div.section.post-body > p ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()

        elif linkpage.find('fisikastudycenter.com')!=-1:
            p = response.css('div.leading-0.clearfix > p ::text').extract()
            img = response.xpath('//div[@class="leading-0 clearfix"]//img/@src').get()

        elif linkpage.find('kimiastudycenter.com')!=-1:
            p = response.css('div.entry-content.clearfix > p ::text').extract()
        elif linkpage.find('pelajaran.co.id')!=-1:
            p = response.css('div.entry-content.entry-content-single > p ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()
            
        elif linkpage.find('studybahasainggris.com')!=-1:
            p = response.css('div.entry-content.entry-content-single > p ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()

        elif linkpage.find('faunadanflora.com')!=-1:
            p = response.css('div.entry-content > p ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()

        elif linkpage.find('quipper.com')!=-1:
            p = response.css('div.inner-post-entry.entry-content > p ::text').extract()
            img = response.xpath('//div[@class="inner-post-entry entry-content"]//img/@data-src').get()

        elif linkpage.find('kelaskita.com')!=-1:
            p = response.css('section.body > p ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()

        elif linkpage.find('matematikastudycenter.com')!=-1:
            p = response.css('div.entry-content.mh-clearfix > p ::text').extract()
            img = response.xpath('//figure[@class="wp-block-image size-full"]//img/@src').get()

        elif linkpage.find('wikihow')!=-1:
            
            wiki = response.css('div.pre-content > a ::text').getall()
            wiki = ' '.join((wiki))
            if wiki.find('Pendidikan dan Komunikasi') or wiki.find('Hobi dan Kerajinan Tangan'):
                p = response.css('div.mw-parser-output ::text').extract()
            else:
                pass
            
        elif linkpage.find('wardayacollege.com')!=-1:
            p = response.css('div.entry-content > p ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()

        elif linkpage.find('sekolahdasar.net')!=-1:
            p = response.css('div.post-body.post-body-artikel > p ::text').extract()
            img = response.xpath('//div[@class="post-body post-body-artikel"]//img/@src').get()

        elif linkpage.find('sdtqcitamulia.com')!=-1:
            p = response.css('div.entry-content > p ::text').extract()
            img = response.xpath('//div[@class="post-thumbnail"]//img/@src').get()

        elif linkpage.find('modulkomputer.com')!=-1:
            p = response.css('div.entry-content > p ::text').extract()
            img = response.xpath('//div[@class="entry-content"]//img/@src').get()

        elif linkpage.find('biologimediacentre.com')!=-1:
            p = response.css('article > div.entry-content ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()
        
        
        elif linkpage.find('ilmusains.com')!=-1:
            p = response.css('div.post-body.entry-content > p ::text').extract()
            img = response.xpath('//div[@class="post-body entry-content"]//img/@src').get()

        elif linkpage.find('informazone.com')!=-1:
            p = response.css('div.entry-content > p ::text').extract()
            img = response.xpath('//div[@class="featured-image  page-header-image-single"]//img/@data-src').get()

        elif linkpage.find('kakakpintar.com')!=-1:
            p = response.css('div.entry-content.entry-content-single > p ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()

        elif linkpage.find('7pagi.com')!=-1:
            p = response.css('div.entry-content > p ::text').extract()
            img = response.xpath('//meta[@property="og:image"]/@content').get()

        tag = response.request.url.find('/tag/')
        category = response.request.url.find('/category/')
        page = response.request.url.find('/page')
        login = response.request.url.find('/login')
        tpage = "Page "
        
        if response.css('title ::text').get() !=-1:
            titlepage = response.css('title ::text').get().casefold().find(tpage.casefold())
        else:
            pass
        
        amp = response.request.url.find('amp=')
        uniq = response.request.url.find('~')

        tagheader = response.xpath('//h1[text()]').get()
        
        artikel = response.css('p::text').getall()
        artikeljoin = ' '.join((artikel))
        artikeljoin = response.css('title::text').get()+ " " +artikeljoin

        artikeljoin = (artikeljoin.encode('ascii', 'ignore')).decode("utf-8")
        artikeljoin = re.sub("&.*?;", "", artikeljoin)
        artikeljoin = re.sub(">", "", artikeljoin)
        artikeljoin = re.sub("!", "", artikeljoin)
        artikeljoin = re.sub(r'[0-9]+', '', artikeljoin)
        artikeljoin = re.sub("/", "", artikeljoin)      
        artikeljoin = re.sub("\n", "", artikeljoin)
        artikeljoin = re.sub("\t", "", artikeljoin)
        artikeljoin = re.sub("\r", "", artikeljoin)
        artikeljoin = re.sub("\2013", "", artikeljoin)
        artikeljoin = re.sub("[\]\|\[\@\,\$\%\*\&\\\(\)\":]", "", artikeljoin)
        artikeljoin = re.sub("-", " ", artikeljoin)
        artikeljoin = re.sub("\.+", "", artikeljoin)
        artikeljoin = re.sub("^\s+","" ,artikeljoin)
        artikeljoin = re.sub(' +', ' ', artikeljoin)
        artikeljoin = artikeljoin.lower()

        word_list = artikeljoin.split()
        number_of_words = len(word_list)

        if tag != -1 or category != -1 or page != -1 or titlepage != -1 or login != -1 or amp != -1 or uniq != -1:
            pass
        elif re.findall('='+r'[0-9]+', response.request.url):
            pass
        elif linkpage.find(urlparse(linkpage).netloc + '//')!=-1:
            pass
        elif number_of_words < 300:
            pass
        elif p:
            yield{
                'url' : linkpage,
                'image' : img,
                'title': response.css('title::text').get(),
                'text' : artikeljoin
            }

        for next_page in response.css('a::attr(href)').getall():
            if next_page.startswith('http'):
                yield response.follow(next_page, self.parse)
            else:
                page_url = (" ".join(self.start_urls) + next_page)
                yield response.follow(page_url, self.parse)

