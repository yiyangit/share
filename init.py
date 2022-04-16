# -*- coding: UTF-8 -*-
import time
import os
import sys
sys.stdout = open("D:/share/lists.html",encoding='utf-8',mode='w')
file_name = os.listdir('D:/share/s')
print("<p>更新于"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"</p>")
for name in file_name:
	print("<a href='./s/"+name+"'>"+name+"</a></br>")
