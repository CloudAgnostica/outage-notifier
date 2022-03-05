#!/usr/bin/python3
import sys
import requests

def webHook(webHookUrl,serviceUrl):
  requests.post(webHookUrl, json={"text": serviceUrl + " Did Not Respond");

for index,arg in enumerate(sys.argv):
  if(index <= 1): continue
  try:
    urlStatus = request.get(arg).status_code
    if(urlStatus != 200):
      webHook(sys.argv[1],arg)
