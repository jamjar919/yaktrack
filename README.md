**YakTrack**
A simple library to scrape the YikYak API. Comes with a simple viewer (yakview.py) and the library functions for viewing data (yaktrack.py).

Supports the following features:
* Get all hot yaks - getHotYaks()
* Get all new yaks - getNewYaks()
* Post a new yak - yak(message)
* Comment on a yak - comment(yakID,comment)
* Get current yakarma - getYakarma()
* Vote on yaks - voteYak(yakID,vote)
* Vote on comments - voteComment(yakID,commentID,vote)

**Setup Instructions**
Dependencies: json, subprocess, curses (for UI)
The library works with curl, so you must also have curl installed and available to use when you run the files, or they won't work. 
This has only been tested on openSUSE, and I make no claim that it will run on any other system, but you are welcome to try.

After you have resolved all dependencies, fill in the exampleyakker.py details, namely the cfuid and yid parameters. You can find these by inspecting a network request to the api in Chromium (Or any browser of your choice). To do this, authenticate your account for web on the YikYak website, press F12, scroll to the network tab and refresh the page. Clicking on one of the calls to /notifications? will give you access to the request. The yid and cfuid can be found by navigating to the Cookies panel within the network request. 

Alternatively, the yid and cfuid can be found by installing a browser extension like EditThisCookie, which make the process a bit simpler. 

Once you have pasted in the parameters, rename the file yakker.py. The program should then begin to work properly.
