#!/usr/bin/python
import logging
import time
import psutil
import uuid
import sys
import Adafruit_DHT
from iotSupport import getConfig, pi_h_status, dict_formatter, pushData



def main():

    config = {}
    dataPush = []
    singleResult = ()
    recordCount=0;
    
    therm_labels = ["eventType","timeStamp","deviceLabel","tempra","humidity","deviceNode"]
    
    
    
    globalConfig = getConfig.parseConfig("tempratureConfig.conf","GLOBAL")
    dhtConfig = getConfig.parseConfig("tempratureConfig.conf","DEVICEDHT")
    nrConfig = getConfig.parseConfig("tempratureConfig.conf","NEWRELIC")
    
    
    logging.basicConfig(filename=globalConfig['logfile'], level=logging.INFO)
    
    systemLog = logging.getLogger("Info");
    systemLog.info("Start")

    while True:

        if len(dhtConfig) > 1:
            #humidity, temperature, outTime = Adafruit_DHT.read_retry(dhtConfig['onedevicetype'], dhtConfig['onegpiopin'])
            humidity, temperature = Adafruit_DHT.read_retry(dhtConfig['onedevicetype'], dhtConfig['onegpiopin'])
            outTime =int(time.time())

            therm_values = ["SensorRead", outTime, dhtConfig['onelabel'], humidity, temperature,uuid.getnode()]
            formatResult = dict_formatter.add_to_dict(therm_labels,therm_values)
            dataPush.append(formatResult)
            
            time.sleep(float(dhtConfig['onechkspeed']));
            
            if recordCount == int(nrConfig['samplesize']):
                nrResponse = pushData.nrPost(nrConfig['nrurl'],nrConfig['nrinsertkey'],dataPush,systemLog)
                
                recordCount = 0;
                dataPush = []
                
            recordCount = recordCount+1   
    
    
    
    
        

        
        
        
    


   
main()

