
def add_to_dict(inLabels,inData):
    
    eventData = {}
    
    if (len(inLabels) == len(inData)):

        for i in range(len(inLabels)):
            eventData[inLabels[i]] = inData[i]
                
       
    return eventData
    
    