#  This code will read run a speed test and report back the results.
#  Written by Ken Flerlage, February, 2021
#  This code is in the public domain

import sys
import os
import speedtest


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

print("Download: " + str(downSpeed) + " Mbps")
print("Upload: " + str(upSpeed) + " Mbps")
print("Ping: " + str(ping) + " ms")
