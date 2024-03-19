import intro
import os
import validators
#python3 -m pip install validators

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

