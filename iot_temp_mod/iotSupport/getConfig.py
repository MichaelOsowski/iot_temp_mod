'''
Created on Jan 26, 2016

@author: Michael Osowski
'''
import ConfigParser


def parseConfig(InFile,configGroup):
    confDict = {}
    config= ConfigParser.ConfigParser()
    config.read(InFile)
    options = config.options(configGroup)
    for option in options:
        try:
            confDict[option] = config.get(configGroup,option)
           
        except:
            print("Missing Config  values")
        
    return confDict