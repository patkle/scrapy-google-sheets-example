import pkgutil
import pickle
from googleapiclient.discovery import build


class GoogleSheetsPipeline:
    """Example pipeline for saving data to Google Sheets"""

    def __init__(self, sheet_id, range) -> None:
        # save sheet_id and range for later use in process_item 
        self.sheet_id = sheet_id
        self.range = range
        # load token from pickle file which you hopefully saved to the resources folder
        token_file = pkgutil.get_data("scrapy_google_sheets_example", "resources/token.pickle")
        token = pickle.loads(token_file)
        # build connection to google sheets api
        service = build('sheets', 'v4', credentials=token)
        self.sheet = service.spreadsheets()

    @classmethod
    def from_crawler(cls, crawler) -> None:
        return cls(
            sheet_id=crawler.settings.get('GOOGLE_SHEET_ID'),
            range=crawler.settings.get('GOOGLE_SHEET_RANGE')
        )

    def _build_body(self, item) -> dict:
        """build body for data to submit to google sheets from item"""
        return {
            'values': [[
                str(item['quote']),
                str(item['author'])
            ]]
        }

    def _append_to_sheet(self, item) -> None:
        """Append item to spreadsheet"""
        # get body for sheets request from item
        body = self._build_body(item)
        # append body to spreadsheed
        self.sheet.values().append(
            spreadsheetId=self.sheet_id, 
            range=self.range, 
            body=body, 
            valueInputOption="USER_ENTERED" 
        ).execute()

    def process_item(self, item, spider):
        self._append_to_sheet(item)
        return item
