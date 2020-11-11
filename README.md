# scrapy-google-sheets-example
Example on how to use the Google Sheets API to write a Scrapy Item Pipeline

## Google API setup
### Configure the API
Firstly you will need to enable the API. You can do this here: [Step 1: Turn on the Google Sheets API](https://developers.google.com/sheets/api/quickstart/python#step_1_turn_on_the). 
After setting your project name, configure your OAuth client to **Desktop APP**. Then save the client configuration file (credentials.json) to this folder.

### Install the Client Library
Afterwards you will probably need to install some libraries as mentioned in [Step 2: Install the Google Client Library](https://developers.google.com/sheets/api/quickstart/python#step_2_install_the_google_client_library). 
The following command should do it in most cases:
`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

### Get your token
Now you can retrieve your token with the included file `get_token.py`. 
You should be able to start it with `python get_token.py`. After granting permissions, you should end up with a file named `token.pickle`. Move this file to the `scrapy_google_sheets_example/resources` folder. 

## Settings
In `scrapy_google_sheets_example/settings.py` you will have to set the ID of the Spreadsheet you want to save your data to. You can get the ID from the url. 
For example, for this url https://docs.google.com/spreadsheets/d/1eX8ftT1jKY2MyUcaHFV-Oo93qGP1NgHdcC-4MFm6UUc/edit#gid=0 the ID is **1eX8ftT1jKY2MyUcaHFV-Oo93qGP1NgHdcC-4MFm6UUc**. 
So the code would look like this:
`GOOGLE_SHEET_ID = '1eX8ftT1jKY2MyUcaHFV-Oo93qGP1NgHdcC-4MFm6UUc'`

You also need to set a range of cells for the Pipeline as `GOOGLE_SHEETS_RANGE`. In this example I used the range `A:B`, which means that the results will be written in the cells A and B. 

## Starting the spider
The included spider is an example that gets quotes and their authors from [quotes.toscrape.com](http://quotes.toscrape.com/).
You can use the command `scrapy crawl quotes` to start the process. 
