# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 23:16:11 2021

@author: johnm
"""

#pip install pygeoip
import pygeoip

gip = pygeoip.GeoIP('GeoLiteCity.dat')
res = gip.record_by_addr('100.40.79.212')
for key, val in res.items():
    print('%s : %s' % (key,val))