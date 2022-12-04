import subprocess
from urllib.parse import urlparse

with open("url.txt", "rt") as f:
    domains = [url.strip() for url in f.readlines()]

for x in range(len(domains)):
    subprocess.run('scrapy crawl crawlerAnapedia -a deltafetch_reset=1 -a url={} -s JOBDIR=crawls/somespider-{} -o {}.json'
    .format(domains[x], urlparse(domains[x]).netloc, urlparse(domains[x]).netloc), shell=True)
