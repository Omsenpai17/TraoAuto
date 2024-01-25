#Coded by Traodoisub.com
import os
from time import sleep
from datetime import datetime

os.environ['TZ'] = 'Asia/Ho_Chi_Minh'

try:
	import requests
except:
	os.system("pip3 install requests")
	import requests

try:
	from pystyle import Colors, Colorate, Write, Center, Add, Box
except:
	os.system("pip3 install pystyle")
	from pystyle import Colors, Colorate, Write, Center, Add, Box

headers = {
	'authority': 'traodoisub.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
	'user-agent': 'traodoisub tiktok tool',
}

def login_tds(token):
	try:
		r = requests.get('https://traodoisub.com/api/?fields=profile&access_token='+token, headers=headers, timeout=5).json()
		if 'success' in r:
			os.system('clear')
			print(Colors.green + f"Sukses masuk kedalam akun\nUser: {Colors.yellow + r['data']['user'] + Colors.green} | Coin : {Colors.yellow + r['data']['xu']}")
			return 'success'
		else:
			print(Colors.red + f"Gagal masuk kedalam akun. Coba lagi :\n")
			return 'error_token'
	except:
		return 'error'

def load_job(type_job, token):
	try:
		r = requests.get('https://traodoisub.com/api/?fields='+type_job+'&access_token='+token, headers=headers, timeout=5).json()
		if 'data' in r:
			return r
		elif "countdown" in r:
			sleep(round(r['countdown']))
			print(Colors.red + f"{r['error']}\n")
			return 'error_countdown'
		else:
			print(Colors.red + f"{r['error']}\n")
			return 'error_error'
	except:
		return 'error'

def duyet_job(type_job, token, uid):
	try:
		r = requests.get(f'https://traodoisub.com/api/coin/?type={type_job}&id={uid}&access_token={token}', headers=headers, timeout=5).json()
		if "cache" in r:
			return r['cache']
		elif "success" in r:
			dai = f'''{Colors.yellow}______ ______ ______ ______ ______ ______ ______ ______ ______  
|______|______|______|______|______|______|______|______|______|'''
			print(dai)
			print(f"{Colors.cyan}Pekerjaan berhasil {r['data']['job_success']} Misi | {Colors.green}{r['data']['msg']} | {Colors.yellow}{r['data']['xu']}")
			print(dai)
			return 'error'
		else:
			print(f"{Colors.red}{r['error']}")
			return 'error'
	except:
		return 'error'


def check_tiktok(id_tiktok, token):
	try:
		r = requests.get('https://traodoisub.com/api/?fields=tiktok_run&id='+id_tiktok+'&access_token='+token, headers=headers, timeout=5).json()
		if 'success' in r:
			os.system('clear')
			print(Colors.green + f"{r['data']['msg']}|ID: {Colors.yellow + r['data']['id'] + Colors.green}")
			return 'success'
		else:
			print(Colors.red + f"{r['error']}\n")
			return 'error_token'
	except:
		return 'error'


os.system('clear')
banner = r'''        ,----,                                                                            
      ,/   .`|                                                                            
    ,`   .'  :                              ,---,                        ___              
  ;    ;     /                             '  .' \                     ,--.'|_            
.'___,/    ,' __  ,-.             ,---.   /  ;    '.             ,--,  |  | :,'   ,---.   
|    :     |,' ,'/ /|            '   ,'\ :  :       \          ,'_ /|  :  : ' :  '   ,'\  
;    |.';  ;'  | |' | ,--.--.   /   /   |:  |   /\   \    .--. |  | :.;__,'  /  /   /   | 
`----'  |  ||  |   ,'/       \ .   ; ,. :|  :  ' ;.   : ,'_ /| :  . ||  |   |  .   ; ,. : 
    '   :  ;'  :  / .--.  .-. |'   | |: :|  |  ;/  \   \|  ' | |  . .:__,'| :  '   | |: : 
    |   |  '|  | '   \__\/: . .'   | .; :'  :  | \  \ ,'|  | ' |  | |  '  : |__'   | .; : 
    '   :  |;  : |   ," .--.; ||   :    ||  |  '  '--'  :  | : ;  ; |  |  | '.'|   :    | 
    ;   |.' |  , ;  /  /  ,.  | \   \  / |  :  :        '  :  `--'   \ ;  :    ;\   \  /  
    '---'    ---'  ;  :   .'   \ `----'  |  | ,'        :  ,      .-./ |  ,   /  `----'   
                   |  ,     .-./         `--''           `--`----'      ---`-'            
                    `--`---'                                                              '''
gach  = '========================================='
option = f'''{gach}{Colors.green}
Pilih salah satu dari alat: {Colors.red}
1. auto Follow
2. auto Like (tidak disarankan)
{Colors.yellow}{gach}
'''
option_acc = f'''{gach}{Colors.green}
Pilihan Akun: {Colors.red}
1. Melanjutkan dengan akun Traodoisub yang sudah ada
2. Memakai akun Traodoisub yang baru
{Colors.yellow}{gach}
'''
print(Colorate.Horizontal(Colors.yellow_to_red, Center.XCenter(banner)))
print(Colors.red + Center.XCenter(Box.DoubleCube("TraoAuto tools terbaru")))


while True:
	try:
		f = open(f'TDS.txt','r')
		token_tds = f.read()
		f.close()
		cache = 'old'
	except FileNotFoundError:
		token_tds = Write.Input("Masukan Traodoisub accestoken:", Colors.green_to_yellow, interval=0.0025)
		cache = 'new'
	
	for _ in range(3):
		check_log = login_tds(token_tds)
		if check_log == 'success' or check_log == 'error_token':
			break
		else:
			sleep(2)

	if check_log == 'success':
		if cache == 'old':
			while True:
				print(option_acc)
				try:
					choice = int(Write.Input("Pilihan akun mu:", Colors.green_to_yellow, interval=0.0025))
					if choice in [1,2]:
						break
					else:
						os.system('clear')
						print(Colors.red + f"salah pilihan, pilih antara 1 atau 2\n")
				except:
					os.system('clear')
					print(Colors.red + f"salah pilihan, pilih antara 1 atau 2\n")
			
			os.system('clear')
			if choice == 1:
				break
			else:
				os.remove('TDS.txt')

		else:
			f = open(f'TDS.txt', 'w')
			f.write(f'{token_tds}')
			f.close()
			break
	else:
		sleep(1)
		os.system('clear')

if check_log == 'success':
	#Nhập user tiktok
	while True:
		id_tiktok = Write.Input("Masukan username tiktok (pastikan sudah berada di web):", Colors.green_to_yellow, interval=0.0025)
		for _ in range(3):
			check_log = check_tiktok(id_tiktok,token_tds)
			if check_log == 'success' or check_log == 'error_token':
				break
			else:
				sleep(2)

		if check_log == 'success':
			break
		elif check_log == 'error_token':
			os.system('clear')
			print(Colors.red + f"Username tiktok belum ditambah di website tolong tambah dulu\n")
		else:
			os.system('clear')
			print(Colors.red + f"Server error tolong ulangi\n")

	#Lựa chọn nhiệm vụ		
	while True:
		print(option)
		try:
			choice = int(Write.Input("Pilihan (1/2):", Colors.green_to_yellow, interval=0.0025))
			if choice in [1,2]:
				break
			else:
				os.system('clear')
				print(Colors.red + f"salah pilihan, pilih antara 1 atau 2\n")
		except:
			os.system('clear')
			print(Colors.red + f"salah pilihan, pilih antara 1 atau 2\n")

	#Nhập delay nhiệm vụ
	while True:
		try:
			delay = int(Write.Input("Delay antara pekerjaan (detik):", Colors.green_to_yellow, interval=0.0025))
			if delay > 1:
				break
			else:
				os.system('clear')
				print(Colors.red + f"tidak boleh kurang dari 3\n")
		except:
			os.system('clear')
			print(Colors.red + f"Masukan angka lebih dari 2\n")

	#Nhập max nhiệm vụ
	while True:
		try:
			max_job = int(Write.Input("Maksimum pekerjaan yang dilakukan:", Colors.green_to_yellow, interval=0.0025))
			if max_job > 9:
				break
			else:
				os.system('clear')
				print(Colors.red + f"Minimal pekerjaan adalah 10\n")
		except:
			os.system('clear')
			print(Colors.red + f"Masukan angka diatas 9\n")

	os.system('clear')

	if choice == 1:
		type_load = 'tiktok_follow'
		type_duyet = 'TIKTOK_FOLLOW_CACHE'
		type_nhan = 'TIKTOK_FOLLOW'
		type_type = 'FOLLOW'
		api_type = 'TIKTOK_FOLLOW_API'
	elif choice == 2:
		type_load = 'tiktok_like'
		type_duyet = 'TIKTOK_LIKE_CACHE'
		type_nhan = 'TIKTOK_LIKE'
		api_type = 'TIKTOK_LIKE_API'
		type_type = 'TYM'

	dem_tong = 0

	while True:
		list_job = load_job(type_load, token_tds)
		sleep(2)
		if isinstance(list_job, dict) == True:
			for job in list_job['data']:
				uid = job['id']
				link = job['link']
				os.system(f'termux-open-url {link}')
				check_duyet = duyet_job(type_duyet, token_tds, uid)
				
				if check_duyet != 'error':
					dem_tong += 1
					t_now = datetime.now().strftime("%H:%M:%S")
					text = [pan(f'[ {dem_tong} ]'),pan(f'{t_now}'),pan(f'{type_type}'),pan(f'{uid}')]
					print(col(text))
					if check_duyet > 9:
						sleep(3)
						a = duyet_job(type_nhan, token_tds, api_type)


				if dem_tong == max_job:
					break
				else:
					for i in range(delay,-1,-1):
						print(Colors.green + 'Mohontunggu: '+str(i)+' Detik',end=('\r'))
						sleep(1)

		if dem_tong == max_job:
			print(f'{Colors.green}Complete {max_job} Pekerjaan!')
			break



