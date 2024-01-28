try:
	import requests
except:
	os.system("pip3 install requests")
	import requests
try:
	import rich
except:
	os.system("pip3 install rich")
	import rich
import os
from time import sleep
from datetime import datetime
from rich.align import Align
from rich.columns import Columns as columns
from rich.panel import Panel as panel
from rich import print,box
from rich.live import Live
from rich.table import Table
from rich.rule import Rule as rule
from rich.console import Console
from rich.progress import (
    BarColumn,
    Progress,
    SpinnerColumn,
    TextColumn,
    TimeElapsedColumn,
    TimeRemainingColumn,
    MofNCompleteColumn
)
console = Console()

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
			nama = r['data']['user']
			koin = r['data']['xu']
			user = [panel(f'[royal_blue1]Nama User : [sea_green1]{nama}',border_style='blue'),
					panel(f'[rgb(95,95,255)]Koin : [rgb(95,255,175)]{koin}',border_style='blue')]

			print(columns(user,expand=True))
			sleep(1)
			return 'success'
		else:
			print(panel('[red]Gagal[/red] masuk kedalam akun | Coba Lagi',expand=False,border_style='red'))
			sleep(1)
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
			print(f"[bright_red]{r['error']}\n")
			return 'error_countdown'
		else:
			print(f"[bright_red]{r['error']}\n")
			return 'error_error'
	except:
		return 'error'

def duyet_job(type_job, token, uid):
	try:
		r = requests.get(f'https://traodoisub.com/api/coin/?type={type_job}&id={uid}&access_token={token}', headers=headers, timeout=5).json()
		if "cache" in r:
			return r['cache']
		elif "success" in r:
			job = r['data']['job_success']
			coin = r['data']['msg']
			money = r['data']['xu']
			tab =  [panel('[green]Berhasil',title='Status',border_style='green'),
					panel(f'{job}',title='Pekerjaan',border_style=("green")),
					panel(f'{coin}',title='Koin Bertambah',border_style=('green')),
					panel(f'{money}',title='Koin',border_style=('green'))]

			console.print(columns(tab,expand=True))
			return 'error'
		else:
			print(f"[bright_red]{r['error']}")
			return 'error'
	except:
		return 'error'

def check_tiktok(id_tiktok, token):
	try:
		r = requests.get('https://traodoisub.com/api/?fields=tiktok_run&id='+id_tiktok+'&access_token='+token, headers=headers, timeout=5).json()
		if 'success' in r:
			os.system('clear')
			print(f"Tiktok ID : {r['data']['id']}")
			return 'success'
		else:
			print(f"[bright_red]{r['error']}")
			return 'error_token'
	except:
		return 'error'

os.system('clear')
banner_start = ('''  .--.--.      ___                         ___     
 /  /    '.  ,--.'|_                     ,--.'|_   
|  :  /`. /  |  | :,'            __  ,-. |  | :,'  
;  |  |--`   :  : ' :          ,' ,'/ /| :  : ' :  
|  :  ;_   .;__,'  /   ,--.--. '  | |' .;__,'  /   
 \  \    `.|  |   |   /       \|  |   ,|  |   |    
  `----.   :__,'| :  .--.  .-. '  :  / :__,'| :    
  __ \  \  | '  : |__ \__\/: . |  | '    '  : |__  
 /  /`--'  / |  | '.'|," .--.; ;  : |    |  | '.'| 
'--'.     /  ;  :    /  /  ,.  |  , ;    ;  :    ; 
  `--'---'   |  ,   ;  :   .'   ---'     |  ,   /  
              ---`-'|  ,     .-./         ---`-'   
                     `--`---'                      ''')
banner_account = '''   ,---,                                                            ___     
  '  .' \                                                         ,--.'|_   
 /  ;    '.                       ,---.          ,--,      ,---,  |  | :,'  
:  :       \                     '   ,'\       ,'_ /|  ,-+-. /  | :  : ' :  
:  |   /\   \    ,---.    ,---. /   /   | .--. |  | : ,--.'|'   .;__,'  /   
|  :  ' ;.   :  /     \  /     .   ; ,. ,'_ /| :  . ||   |  ,"' |  |   |    
|  |  ;/  \   \/    / ' /    / '   | |: |  ' | |  . .|   | /  | :__,'| :    
'  :  | \  \ ,.    ' / .    ' /'   | .; |  | ' |  | ||   | |  | | '  : |__  
|  |  '  '--' '   ; :__'   ; :_|   :    :  | : ;  ; ||   | |  |/  |  | '.'| 
|  :  :       '   | '.''   | '.'\   \  /'  :  `--'   |   | |--'   ;  :    ; 
|  | ,'       |   :    |   :    :`----' :  ,      .-.|   |/       |  ,   /  
`--''          \   \  / \   \  /         `--`----'   '---'         ---`-'   
                `----'   `----'                                             '''
banner_tools = '''        ,----,                                   
      ,/   .`|                                   
    ,`   .'  :                 ,--,              
  ;    ;     /               ,--.'|              
.'___,/    ,' ,---.    ,---. |  | :              
|    :     | '   ,'\  '   ,'\:  : '   .--.--.    
;    |.';  ;/   /   |/   /   |  ' |  /  /    '   
`----'  |  .   ; ,. .   ; ,. '  | | |  :  /`./   
    '   :  '   | |: '   | |: |  | : |  :  ;_     
    |   |  '   | .; '   | .; '  : |__\  \    `.  
    '   :  |   :    |   :    |  | '.'|`----.   \ 
    ;   |.' \   \  / \   \  /;  :    /  /`--'  / 
    '---'    `----'   `----' |  ,   '--'.     /  
                              ---`-'  `--'---'   '''
banner = '''[purple]        ,----,                                                                            
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
option = '''
[blue3]Pilih salah satu dari alat[/blue3] :
1. [dodger_blue3]auto Follow[/dodger_blue3]
2. [dodger_blue2]auto Like (tidak disarankan)
'''
option = Table.grid(expand=True)
option.add_row(Align.center('Pilihan Tools'))
option.add_row('1.','[#e8851c]Auto Follow','([#ed810e]Disarankan[/])')
option.add_row('2.','[#e8851c]Auto Like','([#ed810e]Tidak Disarankan[/])')


option_acc = Table.grid(expand=True)
option_acc.add_row('1.','[#e8851c]Menggunakan Akun Lama','([#ed810e]Tidak menghapus akun yang sudah tersimpan[/])')
option_acc.add_row('2.','[#e8851c]Menggunakan Akun Baru','([#ed810e]Menghapus akun lama dan menggunakan yang baru[/])')

print(panel(Align.center(banner),border_style='cyan'))
console.rule('User')
while True:
	try:
		f = open(f'TDS.txt','r')
		token_tds = f.read()
		f.close()
		cache = 'old'
	except FileNotFoundError:
		print(panel(Align.center('[green]Masukan Traodoisub Acces Token[/]'),
						   subtitle='╭─────',subtitle_align='left'))
		token_tds = input("   ╰──>> ")
		cache = 'new'
	
	for _ in range(3):
		check_log = login_tds(token_tds)
		if check_log == 'success' or check_log == 'error_token':
			break
		else:
			sleep(2)
	os.system('clear')
	if check_log == 'success':
		if cache == 'old':
			while True:
				print(panel(Align.center(banner_account),border_style='bright_blue'))
				console.rule('>> Pilihan Akun <<')
				print(option_acc)
				try:
					print(panel(Align.center('[cyan]Pilihan Akun mu'),subtitle='╭─────',subtitle_align='left'))
					choice = int(input("   ╰──>> "))
					if choice in [1,2]:
						break
					else:
						os.system('clear')
						print(panel(Align.center("salah pilihan, pilih antara 1 atau 2"),border_style='bright_red'))
						print('\n')
				except:
					os.system('clear')
					print(panel(Align.center("salah pilihan, pilih antara 1 atau 2"),border_style='bright_red'))
					print('\n')
			
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
	#Username tiktok
	while True:
		print(panel(Align.center('Masukan username tiktok (pastikan sudah berada di web)'),
			  subtitle='╭─────',subtitle_align='left',border_style='#3b8ce3'))
		id_tiktok = input("   ╰──>> ")
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
			print(panel(Align.center(f"Username tiktok belum ditambah di website tolong tambah dulu"),
							border_style='bright_red'))
		else:
			os.system('clear')
			print(Align.center("[red]Server error tolong ulangi[/red]"))

	while True:
		print(panel(Align.center(banner_tools),border_style='cyan'))
		console.rule('')
		print(option)
		try:
			print(panel('Pilih Tools',subtitle='╭─────',subtitle_align='left'))
			choice = int(input("   ╰──>> "))
			if choice in [1,2]:
				break
			else:
				os.system('clear')
				print(panel("salah pilihan, pilih antara 1 atau 2",border_style='bright_red'))
				sleep(2)
		except:
			os.system('clear')
			print(panel("salah pilihan, pilih antara 1 atau 2",border_style='bright_red'))
			sleep(2)

	while True:
		try:
			print(panel('Delay antara pekerjaan (detik)',subtitle='╭─────┤ Minimal 3 ',subtitle_align='left'))
			delay = int(input("   ╰──>> "))
			if delay > 3:
				break
			else:
				os.system('clear')
				print(panel("tidak boleh kurang dari 3",border_style='bright_red'))
				sleep(2)
		except:
			os.system('clear')
			print(panel("Masukan angka saja",border_style='bright_red'))
			sleep(2)

	while True:
		try:
			print(panel('Berapa pekerjaan yang akan dilakukan',subtitle='╭─────┤Minimal 10 ',subtitle_align='left'))
			max_job = int(input("   ╰──>> "))
			if max_job > 10:
				break
			else:
				os.system('clear')
				print(panel("Minimal pekerjaan adalah 10",border_style='bright_red'))
				sleep(2)
		except:
			os.system('clear')
			print(panel("Masukan angka di atas 10",border_style='bright_red'))
			sleep(2)

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
	print(panel(Align.center(banner_start),border_style='bright_blue'))
	console.rule('')
	
	while True:
		progress = Progress(
    	"{task.description}",
    	SpinnerColumn("dots10"),
		BarColumn(bar_width=200),
		TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
		TimeRemainingColumn(),
		MofNCompleteColumn(),
		)

		list_job = load_job(type_load, token_tds)
		sleep(1)
		with progress:
			tugas = progress.add_task("[green]Running",total=max_job)
			if isinstance(list_job, dict) == True:
				for job in list_job['data']:
					uid = job['id']
					link = job['link']
					os.system(f'termux-open-url {link}')
					check_duyet = duyet_job(type_duyet, token_tds, uid)
					if check_duyet != 'error':
						dem_tong += 1
						t_now = datetime.now().strftime("%H:%M:%S")
						progress.update(tugas, advance=1)
						if check_duyet >= 9:
							a = duyet_job(type_nhan, token_tds, api_type)
							os.system('clear')
							print(panel(Align.center(banner_start),border_style='bright_blue'))
							console.rule('')
							sleep(3)
					if dem_tong == max_job:
						break
					else:
						for i in range(delay,-1,-1):
							sleep(1)

		if dem_tong == max_job:
			print(f'[green]Complete {max_job} Pekerjaan!')
			break

