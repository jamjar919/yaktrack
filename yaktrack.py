import json;
import subprocess;
import cookie;
theRequest = cookie.getCurlRequest(); 

p = subprocess.Popen(theRequest, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
response = "";
for line in p.stdout.readlines():
    response = response + str(line);
retval = p.wait();

print(response);