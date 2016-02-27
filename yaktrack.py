import json;
import subprocess;
import math;
import os;
# You need a file curlreq that has a function getCurlRequest that returns the curl request to run.
# Get the curl request by inspecting the network request from:
#https://www.yikyak.com/api/proxy/v1/messages/all/hot?userLat=54.77525&userLong=-1.584852&lat=54.77525&long=-1.584852&myHerd=0 
# Chrome will give you the curl option when you right click on the request, copy paste that into your function and add the 
# -s flag so that curl runs silently (else you get a progress bar).
# You also need to escape some "'s in the request
import curlreq;

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
    response = response[3:len(response)-2];
    # Fix escaped characters that otherwise break the json interpreter
    response = response.replace("\\\\\"",""); # \\"
    response = response.replace("\\\'",""); # \'
    response = response.replace("\\",""); # \
    jsonData = response.split("},{"); # Response is not properly formatted for some reason, seperate and parse individually.
    newData = list();
    for data in jsonData:
        if data[0] != "{":
            data = "{" + data;
        if data[-1] != "}":
            data = data + "}";
        newData.append(json.loads(data));
    return(newData);

def getHotYaks():
    theRequest = curlreq.getCurlRequest('hot','54.77525','-1.584852'); 
    response = getServerResponse(theRequest);
    return parseYakJson(response);

def getNewYaks():
    theRequest = curlreq.getCurlRequest('new','54.77525','-1.584852'); 
    response = getServerResponse(theRequest);
    return parseYakJson(response);

yaks = getNewYaks()
for yak in yaks:
    print(yak["message"].ljust(200),str(math.floor(float(yak["score"]))).ljust(0));
