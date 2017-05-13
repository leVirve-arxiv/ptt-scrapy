BOT_NAME = 'ptt'
BOARD_NAME = 'mobilecomm'

LOG_LEVEL = 'WARN'

SPIDER_MODULES = ['ptt.spiders']
NEWSPIDER_MODULE = 'ptt.spiders'

USER_AGENT = ('Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 '
              '(KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36')

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Database
MONGO_URI = 'localhost'
MONGO_DATABASE = 'ptt'

# Pipelines
ITEM_PIPELINES = {
   'ptt.pipelines.MongoPipeline': 300,
}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1.25
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 16
