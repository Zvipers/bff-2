#-------------------------------------->
#     *recode mulu pleer 
#-------------------------------------->
#     *Coding by Zviper
#     *Name tool bff-2 <--- don't remove name bff-2
#     *version 1.3
	
#--- JALANKAN TOOL
if __name__=="__main__":
	try:
		import os, sys, shutil, subprocess 
	except requests.exceptions.ConnectionError:
		exit ('\n\t\x1b[0m $ koneksi bermasalah ...\n')
			
	if sys.version_info.major != 3: # cek versi python 
		exit("\n\t\x1b[0m type: python bff-2.py \n")
		
	try: # install module
		import requests 
	except (ImportError,ModuleNotFoundError):
		print ('\n\t\x1b[0m $ install module requests ...\n')
		os.system("pip install requests")
	try:
		import bs4 
	except (ImportError,ModuleNotFoundError):
		print ('\n\t\x1b[0m $ install module bs4 ...\n')
		os.system("pip install bs4")
	try:
		import mechanize 
	except (ImportError,ModuleNotFoundError):
		print ('\n\t\x1b[0m $ install module mechanize ...\n')
		os.system("pip install mechanize")
	try:
		import concurrent.futures 
	except (ImportError,ModuleNotFoundError):
		print ('\n\t\x1b[0m $ install module futures ...\n')
		os.system("pip install futures")
	try:
		import rich 
	except (ImportError,ModuleNotFoundError):
		print ('\n\t\x1b[0m $ install module rich ...\n')
		os.system("pip install rich")
		
	try: # music mp3
		bff_2 = open(os.devnull, "w")
		my_music = subprocess.call(["dpkg","-s","play-audio"],stdout=bff_2,stderr=subprocess.STDOUT)
		bff_2.close() 
		if my_music !=0:
			os.system('pkg install play-audio' )
	except FileNotFoundError:
		os.system('pkg install play-audio' )
			
	from zviper.menu import zviper_xyz_ganteng_banget as onichan 
	#from log.masuk import zviper_tzy as masuk 
	from shutil import rmtree as lolichan
	runtah = [
		"zviper/__pycache__",
		"log/__pycache__",
		"xyz/__pycache__"
	]
	try:
		[lolichan(xz) for xz in runtah]
	except: 
		pass 
	os.system('git pull')
	onichan() 
