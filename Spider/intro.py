class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'

def ft_welcome():
    print(colors.RED + R"""
##########################################################
# __        __   _                            _____      #
# \ \      / /__| | ___ ___  _ __ ___   ___  |_   _|__   #
#  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \   | |/ _ \  #
#   \ V  V /  __/ | (_| (_) | | | | | |  __/   | | (_) | #
#    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|   |_|\___/  #
#  ____        _     _                                   #
# / ___| _ __ (_) __| | ___ _   _          / - \         #
# \___ \| '_ \| |/ _` |/ _ \ | | |       \_\(_)/_/       #
#  ___) | |_) | | (_| |  __/ |_| |       __//"\\__       #
# |____/| .__/|_|\__,_|\___|\__, |         /   \         #
#       |_|                 |___/       By Speranos      #
#                                                        #
# Spider is slow, but its web catches the fastest flies. #
##########################################################
""")

def ft_option():
    print(colors.GREEN + R"""
		./spidey [-rlp] URL

• Option -r : recursively downloads the images from the URL.

• Option -r -l [N] : indicates the maximum depth level of the recursive download.
If not indicated, it will be 5.

• Option -p [PATH] : indicates the path where the downloaded files will be saved.
If not specified, ./data/ will be used.
""")