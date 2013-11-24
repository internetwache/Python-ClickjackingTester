#!/usr/bin/python2.7

# Python - ClickjackingTester
# Author: Sebastian Neef - Internetwache.org
# Twitter: @internetwache
# Comment: Happy Hacking!

import sys, urllib2
clickjacking = False

class ClickjackingTest(object):

    def __init__(self):
        self.__init()

    def __init(self):
        self.__url = ""
        self.__csrfPoc = ""

    def __create_poc(self):
        html = '''
    <html>
    <body>
        <iframe src="'''+self.__url+'''"></iframe>
    </body>
    </html>
        '''
        self.__csrfPoc =  html

    def __is_clickjackable(self):
        url = self.__url
        try:
            if url[:4] != "http":
                url = "http://" + url
                sys.argv[1] = url

            req = urllib2.urlopen(url)
            headers = req.info()

            if not "X-Frame-Options" in headers:
                return True
        except:
            pass
        return False

    def getURL(self):
        return self.__url

    def getPoC(self):
        return self.__csrfPoc

    def test(self,url):
        self.__init()
        self.__url = url

        if(not self.__is_clickjackable()):
            return False
        
        self.__create_poc()
        return True

def usage():
    print "[*] Usage: ", sys.argv[0]," [URL]"
    print "[-] URL: the url to test"

def main():
    print "[*] Started ClickjackingTester"

    if len(sys.argv) <= 2:
        if(len(sys.argv)==1 or sys.argv[1]=="-h" or sys.argv[1]=="--help"):
            usage()
            sys.exit(0)
        else:
            url = sys.argv[1]
    else:
        usage()
        sys.exit(0)

    clkTester = ClickjackingTest()

    print "[*] Testing..."
    if clkTester.test(url):
        print "[*] X-Frame-Options-Header is missing"
        print "[*] Clickjacking is possibe"
        print clkTester.getPoC()
    else:
        print "[*] You can't clickjack this!"
    print "[+] Done"

main()