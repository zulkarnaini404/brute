# MODUL IN PYTHON 
# rikod mulu si plerr
import os,sys,requests, re, bs4, json, time,random, datetime
import hmac, hashlib, urllib, urllib.request, uuid
from bs4 import BeautifulSoup as parser
from time import sleep as jeda
from datetime import datetime
from random import randint

# MODUL IN RICH
from rich import print as tulis
from rich.panel import Panel 

#--- GET ID & TOKEN API
gett_token_API = 'AAEpIEq3gxzNui5z962GqWj-Zii1gmRkHas'
gett_token_API2 = 'AAFyLdcYxMKj2yVWBWEzCCeOrXbH-kGs2ME'

#--- WARNA RICH
Te = '[b]' # tebal 
P = '[#FFFFFF]' # putih
U = '[#AF00FF]' # ungu
O = '[#00FFFF]' # biru muda
M = '[#FF0022]' # merah
Pi = '[#FF0099]' # pink
H = '[#00FF33]' # hijau
K = '[#FFFF00]' # kuning
J = "[#FF8F00]" # Jingga

#--- WARNA ANSII (PYTHON)
m = '\x1b[1;91m' # merah
h = '\x1b[1;92m' # hijau
k = '\x1b[1;93m' # kuning
b = '\x1b[1;94m' # biru
u = '\x1b[1;95m' # ungu
o = '\x1b[1;96m' # biru muda
p = '\x1b[1;97m' # putih
j = '\033[38;2;255;127;0;1m' # orange
n = '\x1b[0m' # clear
til = '•'
ansixx = random.choice([m, h, k, b, u, o, p, j])

#--- TANGGAL BULAN 
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month 

waktu = ("{}-{}-{}").format(hari,bulan,tahun)
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}


"""

       fiks sekali di ubah error                                                                                                                                                                                                                                                                                                                                                                                                                                                                           CODING BY GUWEH ROMI AFRIZAL :v

"""
