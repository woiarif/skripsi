BOT_NAME = 'WebScrapingAnapedia'
SPIDER_MODULES = ['WebScrapingAnapedia.spiders']
NEWSPIDER_MODULE = 'WebScrapingAnapedia.spiders'
ROBOTSTXT_OBEY = False
DEPTH_LIMIT = 0
SCHEDULER_PRIORITY_QUEUE = 'scrapy.pqueues.DownloaderAwarePriorityQueue'
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = 'scrapy.squeues.PickleFifoDiskQueue'
SCHEDULER_MEMORY_QUEUE = 'scrapy.squeues.FifoMemoryQueue'
CONCURRENT_ITEMS = 50
CONCURRENT_REQUESTS = 50
CONCURRENT_REQUESTS_PER_DOMAIN= 50
DOWNLOAD_TIMEOUT = 30

DOWNLOAD_DELAY = 0
DELTAFETCH_ENABLED = True

SPIDER_MIDDLEWARES = {
    'scrapy_deltafetch.DeltaFetch': 100,
}


