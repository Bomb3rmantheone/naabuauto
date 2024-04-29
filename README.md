# naabuauto
 A simple bug bounty tool that runs an Nmap scan via Naabu on a list of subdomains in a txt file created with Subfinder, Assetfinder, etc.

Installation:

git clone https://github.com/Bomb3rmantheone/naabuauto.git

Before using:

Make sure you've installed Naabu.

Then open the naabuauto.py file inside of a text editor and where it says "path/to/file", replace with the path to your txt file with your subdomains or IP's. 

Then run:

Python3 naabuauto.py

It will automatically omit "https://" or "http://" when running against the list of subdomains in your txt file and runs through lists of just IP's also.

 
