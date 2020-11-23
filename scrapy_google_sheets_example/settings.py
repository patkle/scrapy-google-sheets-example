# Scrapy settings for scrapy_google_sheets_example project
BOT_NAME = 'scrapy_google_sheets_example'
SPIDER_MODULES = ['scrapy_google_sheets_example.spiders']
NEWSPIDER_MODULE = 'scrapy_google_sheets_example.spiders'

# id of the spreadsheet you want to use to store your data
GOOGLE_SHEET_ID = '1eX8ftT1jKY2MyUcaHFV-Oo93qGP1NgHdcC-4MFm6UUc'
# range in which to insert the data
# the following specifies column A to column B
GOOGLE_SHEET_RANGE = 'A:B'

# activate the pipeline to transfer data to google sheets
from .pipelines import GoogleSheetsPipeline
ITEM_PIPELINES = {
    GoogleSheetsPipeline: 300
}
