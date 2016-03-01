import json;
import subprocess;
import math;
import os;
# Download the exampleyakker.py file and fill in the fields to use the program. Then rename it yakker.py
import yakker;

def getCurlRequest(typ,lat,lon,yid=None):
    if yid == None:
        yid = yid.getDefaultYid();
    cookie = yakker.getCookie(yid);
    return "curl -s 'https://www.yikyak.com/api/proxy/v1/"+typ+"?userLat="+lat+"&userLong="+lon+"&lat="+lat+"&long="+lon+"&myHerd=0' -H 'if-none-match: W/\"ee0f-AxVZDU3sErWZvluXofO/SQ\"' -H 'accept-encoding: gzip, deflate, sdch' -H 'accept-language: en-GB,en-US;q=0.8,en;q=0.6' -H 'user-agent: "+yakker.getUserAgent()+"' -H 'accept: application/json, text/plain, */*' -H 'referer: https://www.yikyak.com/nearby/hot' -H 'cookie: "+cookie+"' -H 'x-access-token: "+yid+"' --compressed";

def getYid(yid=None):
    if yid == None:
        yid = yakker.getDefaultYid();
    response = getServerResponse("curl -s 'https://www.yikyak.com/api/auth/token/refresh' -X POST -H 'origin: https://www.yikyak.com' -H 'accept-encoding: gzip, deflate' -H 'accept-language: en-GB,en-US;q=0.8,en;q=0.6' -H 'user-agent: "+yakker.getUserAgent()+"' -H 'accept: application/json, text/plain, */*' -H 'referer: https://www.yikyak.com/nearby/new' -H 'cookie: "+yakker.getCookie(yid)+"' -H 'x-access-token: "+yid+"' -H 'content-length: 0' --compressed");
    return response[3:len(response)-2];

def getServerResponse(theRequest):
    # call curl request
    p = subprocess.Popen(theRequest, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # put our output into a single string
    response = "";
    for line in p.stdout.readlines():
        response = response + str(line);
    retval = p.wait();
    return response;

def parseYakJson(response):
    # format that response
    response = str(response);
    #check for invalid cookie.
    if response == 'b\'{"error":{"message":"Invalid access token"}}\'':
        raise RuntimeError("Cookie is probably invalid");
    #get rid of start and end weird bits
    response = response[2:len(response)-1];
    # Fix escaped characters that otherwise break the json interpreter
    response = response.replace("\\\\\"",""); # \\"
    response = response.replace("\\",""); # \
    return(json.loads(response));

def getHotYaks(yid):
    theRequest = getCurlRequest('messages/all/hot','54.77525','-1.584852',yid); 
    response = getServerResponse(theRequest);
    return parseYakJson(response);

def getNewYaks(yid):
    theRequest = getCurlRequest('messages/all/new','54.77525','-1.584852',yid); 
    response = getServerResponse(theRequest);
    return parseYakJson(response);

def getYakarma(yid):
    theRequest = getCurlRequest('yakker/yakarma','54.77525','-1.584852',yid); 
    response = getServerResponse(theRequest);
    return parseYakJson(response)["yakarma"];