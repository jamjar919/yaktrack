def getDefaultYid(): #yid changes every time the page updates, paste the first yid here
    return "";

def getEndUserID(): # optimizelyEndUserId in cookie
    return "";

def get_ga(): # in cookie
    return "";

def getAmplitudeID(): #in cookie, does not change (?)
    return "";

def get__cfduid(): # in cookie
    return "";

def getOptimiserSegments(): # in cookie
    return "";

def getOptimiserBuckets(): # in cookie
    return "";

def getUserAgent(): # User agent you want to emulate
    return "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36";

def getCookie(yid): # leave this as it is
    return "__cfduid="+get__cfduid()+"; optimizelyEndUserId="+getEndUserID()+"; optimizelySegments="+getOptimiserSegments()+"; optimizelyBuckets="+getOptimiserBuckets()+"; _ga="+get_ga()+"; amplitude_idyikyak.com="+getAmplitudeID()+"; yid="+yid+"; rm=true";