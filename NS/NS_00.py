# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 20:57:47 2016

@author: Sebastien, Oriol Forrest, and Hans
NS Tweeter
"""
# To instal a module run the following command from Command Prompt:
# python -m pip install PACKAGE

import util

#%% NS API Information
username = 'sebastienmoeller@gmail.com'
password = 'rleYtKMXeYbVarsbKGPKXTxXcST7PWFVNdQOP-_EyYZt6kfquPjFkA'


#%% Get Data from NS
import requests
import xml.etree.ElementTree as ET
url = 'http://webservices.ns.nl/ns-api-stations-v2'
data_name = requests.get(url, auth=(username, password)).content
root = ET.fromstring(data_name)

#%% Convert from name into url string
def urlConv(string):
    x = list(string)
    for n, i in enumerate(x):
        if (i == ' ' or i == '/' or i == '\\'):            
            x[n] = '+'
    return ''.join(x)
    
def exRem(string):
    x = list(string)
    for n in enumerate(x):
        if (n < len(x) - 10):
            if (x[n] + x[n+1] + x[n+2] + x[n+3] + x[n+4] + x[n+5] + x[n+6] + x[n+7] + x[n+8] == '<Bericht>'):
                for a in range(9):
                    x[n + 9 + a] = ''
            if (x[n] + x[n+1] + x[n+2] + x[n+3] + x[n+4] + x[n+5] + x[n+6] + x[n+7] + x[n+8] + x[n+9] == '</Bericht>'):
                x[n - 1] = ''
            if (x[n] == ']'):
                x[n] = ''
    return ''.join(x)

#%%
'''
Station_NL is a list of all dutch based stations in the NS system

Key: Station_NL[i][j][k]

i - station number, ordered alphabetically between 0 - 412

j = 0 station name
j = 1 unexpected delays
j = 2 expected delays

k - message index
'''
station_NL = []
for child in root:
    if (child[3].text == 'NL'):     
        info = []
        info.append(child[2][2].text)
        station_NL.append(info)

#%% Get URL for station traffic information API
urlstring = []
for child in station_NL:
    urlstring.append('http://webservices.ns.nl/ns-api-storingen?station=' + util.urlConv(child[0]))

#%% Extract what we want
for i in range(10):
    url = urlstring[i]
    data_traffic = requests.get(url, auth=(username, password)).content
    data_traffic = util.exRem(data_traffic)
    data_traffic = ET.fromstring(data_traffic)
    
    unplanned = []
    planned = []
    for j in range(len(data_traffic[0])):
        # append text 'bericht'
        unplanned.append(data_traffic[0][j][3].text.replace('\n', ''))
    for j in range(len(data_traffic[1])):
        planned.append(data_traffic[1][j][3].text.replace('\n', ''))
    
    station_NL[i].append(unplanned)
    station_NL[i].append(planned)
    
#%%
# Loop through all stations = len(station_NL)
for i in range(10):
    # Unexpected announcement loop
    for j in range(len(station_NL[i][1])):
        unplanned = []
        alert = station_NL[i][1][j]
        wanneer = alert[alert.find('<p><b>Wanneer: ') + len('<p><b>Wanneer: '):alert.find('</b><br/><b>Oorzaak:')]
        alert.replace('<p><b>Wanneer: ', 'Wanneer: ')
        oorzaak = alert[alert.find('</b><br/><b>Oorzaak: ') + len('</b><br/><b>Oorzaak: '):alert.find('</b><br/><b>Advies:')]
        alert.replace('</b><br/><b>Oorzaak: ', 'Oorzaak: ')

        done = False
        berecht = []
        start = alert.find('<br/>')
        while (done == False):            
            if (start != -1):
                alert.replace('<br/>', '')
                end = alert.find('<br/>')
                if (end != -1):
                    berecht.append(alert[start:end])
                    start = end
                else:
                    end = True
            else:
                end = True
                
                
        advies = alert[alert.find('</b><br/><b>Advies: ') + len('</b><br/><b>Advies: '):alert.find()]
        
        alert.find('</b><br/><b>Advies:')
        alert.find('<br/>')

    
    
    
    
    
    
    # Expected announcement loop
    for j in range(len(station_NL[i][2])):






#%% Tweet Information
# Sebastien
# CONSUMER_KEY = '3aYOT8FdbGb7StevaL7KrdQOi'
# CONSUMER_SECRET = 'shagB97BURkcpqMRBmwRu5ysbitqReLTmpQf3YPv2LfvtuEeXb'
# ACCESS_KEY = '862059036-EyDgXgdp7Hillak3Fi7JnRDxjtCTWQ1EXfLsomcA'
# ACCESS_SECRET = 'JhGMMTOJ9RV1BRpq43LANGa23Qs2flyCUFsai0xJuAd0q'
# NS Bot

CONSUMER_KEY = 'nr87FuIaOOfVXwIh0jCRVzk3k'
CONSUMER_SECRET = 'dN2XQkQplRNjfz0puK5XulYgvNnvVECqaAASGyPprcvn7uBr2S'
ACCESS_KEY = '777844901400682496-qi0pMuzTPxlqi9FbUf8ycqVnXb1zFQ9'
ACCESS_SECRET = 'WiLHb5chQSd1BUCUcSzBUVLB4cDCNnn4PouNrRwu8Jwdn'

#%% Initialize twitter environment
import tweepy

tweet_out = "Hello World!"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#%% TWEET
# api.update_status(tweet_out)


