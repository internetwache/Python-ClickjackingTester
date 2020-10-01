Python ClickjackingTester
=======================
- 1.) Installation
- 2.) Usage
- 3.) Functionality
- 4.) ToDo
- 5.) License

##1. Installation

[Pyhton 2.7](http://www.python.org/download/releases/2.7/) is required to run this software.

You only need to clone this GitHub repository:

```
git clone https://github.com/internetwache/Python-ClickjackingTester.git ClickjackingTester
```

Yay you're done :)

##2. Usage

```
% ./clickjacking.py 
[*] Started ClickjackingTester
[*] Usage:  ./clickjacking.py  [URL]
[-] URL: the url to test
```

You only need to run the script with the url to test as the first parameter. e.g. :

```
./clickjacking.py www.internetwache.org
[*] Started ClickjackingTester
[*] Testing...
[*] You can't clickjack this!
[+] Done
```

##3. Functionality

This tool only checks whether the X-Frame-Options header is set in the servers HTTP-Response.

##4. ToDo

- Implement advanced tests. (e.g. Framebuster)

##5. License

This script is licensed under [MIT](http://choosealicense.com/licenses/mit/). 
Please feel free to extend or improve the code/functionality of this script :)

Happy Hacking!
