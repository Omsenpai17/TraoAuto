import datetime, json, requests, os
from time import sleep
from rich import print, box
from rich.columns import Columns
from rich.theme import Theme
from rich.panel import Panel
from rich.table import Table
from rich.align import Align
from rich.spinner import Spinner
from rich.live import Live
from rich.console import Group
from rich.progress import (
	BarColumn,
	Progress,
	SpinnerColumn,
	TextColumn,
	TimeElapsedColumn,
	TimeRemainingColumn,
	MofNCompleteColumn
)

job_progress = Progress(
	"{task.description}",
	SpinnerColumn("dots2"),
	BarColumn(),
	TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
	TimeRemainingColumn(),
	MofNCompleteColumn(),
)


def clear():
	os.system("cls")


def login(acc):
	headers = {
		'authority': 'traodoisub.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
				  'application/signed-exchange;v=b3;q=0.9',
		'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
		'user-agent': 'traodoisub tiktok tool',
	}
	r = requests.get('https://traodoisub.com/api/?fields=profile&access_token=' + acc, headers=headers,
					 timeout=5).json()
	user = r["data"]["user"]
	koin = r["data"]["xu"]
	return user, koin


def get_job(token):
	headers = {
		'authority': 'traodoisub.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
				  'application/signed-exchange;v=b3;q=0.9',
		'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
		'user-agent': 'traodoisub tiktok tool',
	}
	url = f"https://traodoisub.com/api/?fields=tiktok_follow&access_token={token}"

	job = requests.get(url=url, headers=headers).json()
	return job


def redeem_job(token, id_job):
	headers = {
		'authority': 'traodoisub.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
				  'application/signed-exchange;v=b3;q=0.9',
		'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
		'user-agent': 'traodoisub tiktok tool',
	}
	cache = requests.get(f'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_CACHE&id={id_job}&access_token={token}',
						 headers=headers, timeout=5).json()
	total_cache = cache["cache"]
	return total_cache


def redeem_coin(token):
	headers = {
		'authority': 'traodoisub.com',
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,'
				  'application/signed-exchange;v=b3;q=0.9',
		'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
		'user-agent': 'traodoisub tiktok tool',
	}
	redeem_coin = requests.get(
		f"https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token={token}",
		headers=headers).json()
	job = redeem_coin['data']['job_success']
	coin = redeem_coin['data']['msg']
	money = redeem_coin['data']['xu']
	return job, coin, money

def open_link(token,jumlah):
	loading = Panel(Spinner("dots2","Running ..."),expand=False)
	bar_progress = job_progress.add_task("",total=jumlah)
	running_job = [
		Panel()
	]
	running_job_group = Group(

	)

	job = get_job(token)
	selesai = job["cache"]
	max = 0
	for job in job["data"]:
			id_job = job["id"]
			link = job["link"]
			first_index = link.find('@')
			second_index = link.find('video')
			my_string = f'{link[first_index:second_index]}'
			username_tiktok = my_string.replace("\/", "")
			panel_following = [
				Panel(Align.center("Following username")),
				Panel(Align.center(f"{username_tiktok}"))
			]
			print(Columns(panel_following,expand=True))
			sleep(1)
			os.system(f'termux-open-url {link}')
			max += 1
			if max == jumlah:
				print(Panel("Selesai"))
				break
			else:
				pass

try:
	with open("token.json", "r") as token:
		a = json.load(token)
		account = a["Token"]

except FileNotFoundError:
	with open("token.json", "w") as token:
		dat = input("Masukan token TDS : ")
		data = {"token": dat}
		json.dump(data, token, indent=2)
