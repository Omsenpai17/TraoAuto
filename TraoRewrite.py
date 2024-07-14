import datetime
import json
import os
import requests
from time import sleep

from rich import print
from rich.align import Align
from rich.columns import Columns
from rich.console import Group
from rich.live import Live
from rich.panel import Panel
from rich.progress import (
	BarColumn,
	Progress,
	SpinnerColumn,
	TextColumn,
	TimeRemainingColumn,
	MofNCompleteColumn
)
from rich.spinner import Spinner

headers = {
	'authority': 'traodoisub.com',
	'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,''application/signed-exchange;v=b3;q=0.9',
	'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
	'user-agent': 'traodoisub tiktok tool',
}

waktu = datetime.datetime.now().strftime("%H : %M : %S")
bar = Progress(
	"{task.description}",
	SpinnerColumn("dots2"),
	BarColumn(),
	TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
	TimeRemainingColumn(),
	MofNCompleteColumn(),
)


def check_account(token):
	r = requests.get('https://traodoisub.com/api/?fields=profile&access_token=' + token, headers=headers,
					 timeout=5).json()
	user = r["data"]["user"]
	koin = r["data"]["xu"]
	return user, koin

# step 1
def animasi_check_account():
	send = check_account(Token)
	user = send[0]
	koin = send[1]
	loading_anim = Spinner("dots3", "Loading ...")
	panel_kolom = [
		Panel(Align.center(loading_anim)),
		Panel(Align.center('Mengirim token ke server Traodoisub')),
		Panel(Align.center(f'{waktu}'))
	]
	send_token = Panel(Columns(panel_kolom, expand=True))

	kolom_data_akun = [
		Panel(Align.center(f"Nama Akun : {user}")),
		Panel(Align.center(f'Total Koin : {koin}'))
	]
	data_grup = Group(
		Panel(Align.center('Berhasil mengirim token')),
		Columns(kolom_data_akun, expand=True)
	)

	with Live(send_token, refresh_per_second=4) as live:
		sleep(5)
	print(Panel(data_grup))
	return 'success'


def set_username(token, username):
	r = requests.get(f"https://traodoisub.com/api/?fields=tiktok_run&id={username}&access_token={token}", timeout=5,
					 headers=headers).json()
	ID = r['data']['id']
	id_unik = r['data']['uniqueID']
	pesan = 'Berhasil menyetel username'
	return ID, id_unik, pesan

# step 2
def animasi_set_username():
	loading_anim = Spinner("dots3", "Loading ...")
	panel_loading = [
		Panel(Align.center(loading_anim)),
		Panel(Align.center('Mengirim Username ke server Traodoisub')),
		Panel(Align.center(f'{waktu}'))
	]
	send_username = Panel(Columns(panel_loading, expand=True))
	header_grup = Group(
		Panel(Align.center('Masukan username yang akan digunakan')),
		Panel(Align.center('Pastikan sudah berada dalam akun'))
	)
	print(Panel(header_grup))
	nama = input('Masukan Username : @')
	sleep(1)
	os.system('cls')

	send = set_username(Token, nama)
	id = send[0]
	id_unik = send[1]
	pesan = send[2]

	data_tiktok = [
		Panel(Align.center(id), title='ID Tiktok', title_align='center'),
		Panel(Align.center(id_unik), title='ID Unik', title_align='center'),
		Panel(Align.center(pesan), title='Pesan Server', title_align='center')
	]
	tiktok_grup = Group(
		Panel(Align.center('Berhasil Menyetel Username')),
		Columns(data_tiktok, expand=True)
	)

	with Live(send_username, refresh_per_second=4):
		sleep(5)
	print(Panel(tiktok_grup))


def get_job(token):
	url = f"https://traodoisub.com/api/?fields=tiktok_follow&access_token={token}"

	job = requests.get(url=url, headers=headers).json()
	if job != 'error':
		return job
	else:
		cd = job["countdown"]
		return cd, 'error'


def redeem_job(token, id_job):
	cache = requests.get(f'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_CACHE&id={id_job}&access_token={token}',
						 headers=headers, timeout=5).json()
	total_cache = cache["cache"]
	return total_cache


def get_coin(token):
	url = f"https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token={token}"
	redeem_coin = requests.get(url, headers=headers, timeout=5).json()
	job = redeem_coin['data']['job_success']
	coin = redeem_coin['data']['msg']
	money = redeem_coin['data']['xu']
	return job, coin, money

# step 3
def animasi_running_job(ttl, cd):
	running = bar.add_task("", total=ttl)
	loading_anim = Spinner("dots3", "Loading ...")
	panel_loading = [
		Panel(Align.center(loading_anim)),
		Panel(Align.center('Menjalankan Tugas'))
	]
	loading_job = Panel(Group(
		Columns(panel_loading, expand=True),
		Panel(Align.center(bar))
	))

	max_job = 0
	while True:
		list_job = get_job(Token)
		with Live(loading_job, refresh_per_second=4):
			if 'error' in list_job:
				pesan = 'Terlalu cepat ... menunggu'
				cd = list_job[0]
				eror_kolom = [
					Panel(Align.center(pesan)),
					Panel(Align.center(f'Menunggu {cd} detik'))
				]
				print(Panel(Columns(eror_kolom, expand=True)))
				sleep(cd)
			else:
				if isinstance(list_job, dict):
					for job in list_job['data']:
						time = datetime.datetime.now().strftime("%H : %M : %S")
						job_id = job['id']
						username_tiktok = job['uniqueID']
						link = job['link']

						job_columns = [
							Panel(Align.center(job_id)),
							Panel(Align.center(username_tiktok)),
							Panel(Align.center(time))
						]
						print(Panel(Columns(job_columns, expand=True)))
						os.system(f'termux-open-url {link}')
						get_cache = redeem_job(Token, job_id)
						if get_cache != 'error':
							max_job += 1
							bar.advance(running, advance=1)
							if get_cache['cache'] >= 9:
								koin = get_coin(Token)
								print(koin)
								total_job_berhasil = koin[0]
								bertambah = koin[1]
								uang = koin[2]

								redeem_coin_kolom = [
									Panel(Align.center(total_job_berhasil), title='Total Job', title_align='center'),
									Panel(Align.center(bertambah), title='Koin Bertambah', title_align='center'),
									Panel(Align.center(uang), title='Total Koin', title_align='center')
								]
								reddem_koin_grup = Group(
									Panel(Align.center('Berhasil Redeem')),
									Panel(Columns(redeem_coin_kolom, expand=True))
								)
								print(Panel(reddem_koin_grup))
						if max_job == ttl:
							break
						else:
							sleep(cd)


try:
	with open("token.json", "r") as token:
		a = json.load(token)
		Token = a["token"]

except FileNotFoundError:
	with open("token.json", "w") as token:
		dat = input("Masukan token TDS : ")
		data = {"token": dat}
		json.dump(data, token, indent=2)

animasi_check_account()
animasi_set_username()

total = int(input("Jumlah : "))
cooldown = int(input("cooldown : "))
animasi_running_job(total,cooldown)
