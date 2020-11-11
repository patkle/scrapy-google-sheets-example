# Scrapy settings for scrapy_google_sheets_example project
BOT_NAME = 'scrapy_google_sheets_example'
SPIDER_MODULES = ['scrapy_google_sheets_example.spiders']
NEWSPIDER_MODULE = 'scrapy_google_sheets_example.spiders'

GOOGLE_SHEET_ID = '1eX8ftT1jKY2MyUcaHFV-Oo93qGP1NgHdcC-4MFm6UUc'
GOOGLE_SHEET_RANGE = 'A:B'

from .pipelines import GoogleSheetsPipeline
ITEM_PIPELINES = {
    GoogleSheetsPipeline: 300
}
