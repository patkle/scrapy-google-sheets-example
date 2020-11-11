import pkgutil
import pickle
from googleapiclient.discovery import build


class GoogleSheetsPipeline:
    def __init__(self, sheet_id, range):
        self.sheet_id = sheet_id
        self.range = range
        token_file = pkgutil.get_data("scrapy_google_sheets_example", "resources/token.pickle")
        token = pickle.loads(token_file)
        service = build('sheets', 'v4', credentials=token)
        self.sheet = service.spreadsheets()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            sheet_id=crawler.settings.get('GOOGLE_SHEET_ID'),
            range=crawler.settings.get('GOOGLE_SHEET_RANGE')
        )

    def process_item(self, item, spider):
        body = {
            'values': [[
                str(item['quote']),
                str(item['author'])
            ]]
        }
        self.sheet.values().append(
            spreadsheetId=self.sheet_id, 
            range=self.range, 
            body=body, 
            valueInputOption="USER_ENTERED" 
        ).execute()
        return item
