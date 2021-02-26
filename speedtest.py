#  This code will read run a speed test then write the result, with date and time to a Google Sheet
#  Written by Ken Flerlage, February, 2021
#  This code is in the public domain

import sys
import speedtest
from datetime import datetime
import gspread
import os
import time
from oauth2client.service_account import ServiceAccountCredentials

# Get the computer name.
computerName = os.environ['COMPUTERNAME']

# Open Google Sheet
scope = ['https://spreadsheets.google.com/feeds']

# Read API key from a local json file, authorize with Google, then open the spreadsheet
credentials = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/Ken/Documents/Ken/Blog/My Vizzes/Python/creds.json', scope)
gc = gspread.authorize(credentials) 
sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/1CinsOfGyAFWbEERqAWwL-47Ev6UMdvS3d9i__UwmajQ')
worksheet = sheet.get_worksheet(0)

timeStamp = datetime.now()

# Run speed tests
st = speedtest.Speedtest() 
downSpeed = st.download()
upSpeed = st.upload()

servernames =[]   
st.get_servers(servernames)   
ping = st.results.ping

# Convert to megabytes
downSpeed = downSpeed/1000000
upSpeed = upSpeed/1000000

record = [str(timeStamp), computerName, downSpeed, upSpeed, ping]

worksheet.append_row (record)