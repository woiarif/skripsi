import scrapy

class BlogSpider(scrapy.Spider):
    name = 'artikel'
    start_urls = []
    allowed_domains = []

    def __init__(self, **kw):
        super(BlogSpider, self).__init__(**kw)
        url = kw.get('url') or kw.get('domain')
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'https://%s/' % url
        self.url = url
        self.start_urls = [url]
        self.allowed_domains = ["localhost"]

    def parse(self, response):
        linkpage = response.request.url
        p = response.css('div.post > p ::text').extract()
        img = response.xpath('//img/@src').get()

        judul = response.css('title::text').get()
        artikeljoin = ' '.join(p)
        artikeljoin = str(judul)+ " " +artikeljoin

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
                page_url = next_page
                yield response.follow(page_url, self.parse)

