#  -*- coding: utf-8 -*-
from urllib import request
import ssl
import time
import json
import re

ssl._create_default_https_context = ssl._create_unverified_context
# 关闭证书验证

def getlist():
	req = request.urlopen("https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-05-08&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=CDW&purpose_codes=ADULT")
	html = req.read() 
	dict = json.loads(html)
	return dict['data']['result']

i = 1
while True:
	print("=============================第%s次查询=========================" % i)
	for i in range(len(getlist())): 
		onesample = getlist()[i] 
		reobj = re.findall(r'\|\|\|\|(.+?)\|\|\|(.+?)\|\|(.+?)\|(.+?)\|\|\|\|\|', onesample)
		# print(reobj)
		if len(reobj) != 0:
			if u'有' in reobj[0]:
				start_time = re.findall(r'\|(\d{2}:\d{2})\|', onesample)[0]
				station_train_code = re.findall(r'\|([A-Z]\d{3,4})\|', onesample)[0]
				print("有票\t发车时间：%s\t 车次为%s" % (start_time, station_train_code))
	time.sleep(5)
	i += 1
	continue