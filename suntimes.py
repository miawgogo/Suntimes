#! /bin/python
# -*- coding: UTF-8 -*-
import urllib2, json, datetime, time
import dateutil.parser

global latitude
global longitude

api=json.loads(urllib2.urlopen("http://freegeoip.net/json/").read().decode("UTF-8"))
latitude=str(api['latitude'])
longitude=str(api["longitude"])

def getsunrise(lat="", lng="", formatted=1):
 if lat=="" or lng == "":
  lat=latitude
  lng=longitude
 url="http://api.sunrise-sunset.org/json?lat=" + lat + "&lng=" + lng + "&formatted=" + str(formatted)
 print url
 sunapi=urllib2.urlopen(url)
 return json.loads(sunapi.read().decode("UTF-8"))['results']['sunrise']

def getsunset(lat="", lng="", formatted="1"):
 if lat=="" or lng == "": 
  lat=latitude
  lng=longitude
 sunapi=urllib2.urlopen("http://api.sunrise-sunset.org/json?lat=" + lat + "&lng=" + lng + "&formatted=" + str(formatted))
 return json.loads(sunapi.read().decode("UTF-8"))['results']['sunset']

def nighttrue(lat="", lng=""):
 sunrise = dateutil.parser.parse(getsunrise(lat, lng, 0).replace("+00:00",""))
 sunset = dateutil.parser.parse(getsunset(lat, lng, 0).replace("+00:00",""))
 timenow = datetime.datetime.now()
 if sunrise >= timenow >= sunset ==False:
  return False
 else:
  return True

if __name__ == '__main__':
 bools=nighttrue()
 if bools == True:
    print "night time"
 elif bools == False:
  print "day"
 else:
  print bools
 
