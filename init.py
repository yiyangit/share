import os
import sys
sys.stdout = open("D:/share/lists.html",mode='w');
file_name = os.listdir('D:/share/s')
for name in file_name:
	print("<a href='./s/"+name+"'>"+name+"</a></br>");