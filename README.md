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


## Starting the spider
The included spider is an example that gets quotes and their authors from [quotes.toscrape.com](http://quotes.toscrape.com/).
You can use the command `scrapy crawl quotes` to start the process. 
