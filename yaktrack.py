from lxml import html;
import requests;
a = None;
import cookie

if cookie == None:
    print("Error: Please place a valid cookie in cookie.py, cookie=\"yourcookie\"");
    

class YakTracker:
    def getTopYaks(self):
        return 0;

page = requests.get("https://www.yikyak.com/nearby/hot", verify=False, cookies = cookie);
tree = html.fromstring(page.content);
#yaks = tree.xpath('//p[@class="message-text"]/text()');
yaks = tree.xpath('//p[@class="sub-headline"]/text()');
print(yaks);
