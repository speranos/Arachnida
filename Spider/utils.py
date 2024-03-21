from curses.ascii import NUL
from turtle import fillcolor
from intro import colors
import intro
import os
import validators
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


class Arachnida:
	def __init__(self):
		self.recursive = False
		self.max_rec  = 5
		self.Path = "./data/"
		self.Url = ""


def ft_exit():
	intro.ft_option()
	exit()

def parsing(argv, spidey: Arachnida):
	i = 1
	while i < len(argv):
		if argv[i] == "-r":
			spidey.recursive = True
		elif argv[i] == "-l" and spidey.recursive and i + 1 <  len(argv):
			spidey.max_rec = int(argv[i + 1])
			i+=1
		elif argv[i] == "-p" and i + 1 <  len(argv):
			if not os.path.isdir(argv[i + 1]):
				ft_exit()
			else:
				spidey.Path = argv[i + 1]
			i+=1
		else:
			if not validators.url(argv[i]):
				ft_exit()
			else:
				spidey.Url = argv[i]
		i+=1
	if not spidey.Url:
		ft_exit()


def	get_images(img_src, path):
	for img in img_src:
		if(validators.url(img)):
			res = requests.get(img)
			file_extension = os.path.splitext(urlparse(img).path)[1].lower()
			if file_extension in ('.jpg', '.jpeg', '.png', '.gif', '.bmp'):
				print(colors.BLUE + f"Adding: {img}" + colors.END)
				img_name = os.path.basename(urlparse(img).path)
				with open(os.path.join(path, img_name), 'wb') as f:
					f.write(res.content)



def get_links(url, path):
	img_src = set()
	links = set()
	res = requests.get(url)
	content_type = res.headers.get('Content-Type', '')
	if 'html' not in content_type:
		print(colors.RED + f"Skipping content: {url}" + colors.END)
		return links
	print(colors.GREEN + f"Currently Processing: {url}" + colors.END)
	pars = BeautifulSoup(res.content, 'html.parser')
	for img in pars.find_all('img'):
		img_src.add(img.get('src'))
		get_images(img_src, path)
	for a in pars.find_all('a'):
		href = a.get('href')
		if href:
			next = urljoin(url, href)
			if urlparse(next).netloc == urlparse(url).netloc:
				links.add(next)
	return links


def	ft_recursev(max_rec, links, current_rec, path):
	rec_links = set()
	if(links):
		if(current_rec < max_rec):
			for link in links:
				rec_links |= get_links(link, path)
			current_rec+=1
			ft_recursev(max_rec, rec_links, current_rec, path)



def ft_fetch(spidey: Arachnida):
	res = requests.get(spidey.Url)
	pars = BeautifulSoup(res.content, 'html.parser')
	links = get_links(spidey.Url, spidey.Path)
	current_rec = 0
	if(spidey.recursive):
		ft_recursev(spidey.max_rec, links, current_rec, spidey.Path)


