import json;
import subprocess;
import cookie;
theRequest = cookie.getCurlRequest(); 

p = subprocess.Popen(theRequest, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
response = "";
for line in p.stdout.readlines():
    response = response + str(line);
retval = p.wait();
response = str(response);
response = response[3:len(response)-2];
# Fix escaped characters that otherwise break the json interpreter
response = response.replace("\\\\\"",""); # \\"
response = response.replace("\\\'",""); # \'
response = response.replace("\\",""); # \
jsonData = response.split("},{"); # Response is not properly formatted for some reason, seperate and parse individually.
yaks = list();
for data in jsonData:
    if data[0] != "{":
        data = "{" + data;
    if data[-1] != "}":
        data = data + "}";
    data = json.loads(data);
    yaks.append(data["message"]);
    
print(yaks);