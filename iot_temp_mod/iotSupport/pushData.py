import urllib2
import logging
import json
from urllib import urlopen


def nrPost(inURL,inKey,inDict,systemLog):
    

    reqResponse = ''
    req = urllib2.Request(inURL)
    req.add_header('Accept', 'application/json')
    req.add_header('X-Insert-Key', inKey)
    
    
    
    
    
    try:
        req = urllib2.Request(inURL, json.dumps(inDict), headers={'Content-type': 'application/json', 'Accept': 'application/json','X-Insert-Key': inKey})
        response = urllib2.urlopen(req)
        reqResponse = response.read()

        return reqResponse
        
    except Exception, e:
        pass
        systemLog.error('SendingDataFailed',str(e),'hi')
        return reqResponse
        