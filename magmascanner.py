import socket

import threading

import time

import os


r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
b = "\033[34m"
p = "\033[35m"
d = "\033[2;37m"
w = "\033[0m"

menu = f'''

{d} █▀▄▀█ ▄▀█ █▀▀ █▀▄▀█ ▄▀█ {g}█▀ █▀▀ ▄▀█ █▄░█ █▄░█ █▀▀ █▀█
{p} █░▀░█ █▀█ █▄█ █░▀░█ █▀█ {r}▄█ █▄▄ █▀█ █░▀█ █░▀█ ██▄ █▀▄


	{b}Created By {r}DeviLlMan {g}with {r}love :D
'''

print(menu)

ip = input(f'{b}>IP:')


def ScannerPort(port):

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.3)

	try:
		connect = s.connect_ex((ip, port))
		print(f'{g} This Port {port} IS Open!')
		connect.close()

	except:
		print(f'{r} This Port {port} IS Closed!')



def PortList():

	ports = [
		21, 22, 23,
		25, 38, 43, 80, 109, 110, 115, 118, 119, 143,	
		194, 220, 443, 540, 585, 591, 1112, 1433, 1443, 3128, 3197,
		3306, 4000, 4333, 5100, 5432, 6669, 8000, 8080, 9014, 9200
		]

	for allPortInServer in ports:  

		t = threading.Thread(target=ScannerPort, kwargs={'port': allPortInServer})

		t.start()


PortList()





def Nmap_Info():
	time.sleep(3)
	p = os.popen('nmap -A -p 80, 22 -v ' + ip)
	print(p.read())

Nmap_Info()