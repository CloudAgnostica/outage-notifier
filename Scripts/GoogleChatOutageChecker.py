#!/usr/bin/python3
import sys
import requests

def noResponseWebHook(webHookUrl,serviceUrl):
  requests.post(webHookUrl, json={"text": serviceUrl + " Did Not Respond"})

def httpWebHook(webHookUrl,serviceUrl,httpStatus):
  requests.post(webHookUrl, json={"text": serviceUrl + " Responded with HTTP Status: " + str(httpStatus)})

for index,arg in enumerate(sys.argv):
  if(index <= 1): continue
  try:
    urlStatus = requests.get(arg,verify=False).status_code
    if(urlStatus != 200):
      httpWebHook(sys.argv[1],arg,urlStatus)
  except:
    noResponseWebHook(sys.argv[1],arg)
