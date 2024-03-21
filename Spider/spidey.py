import sys
import utils
import intro

def main(argv):
    intro.ft_welcome()
    if len(argv) <= 1 or len(argv) > 7:
        utils.ft_exit()
    spidey = utils.Arachnida()
    utils.parsing(argv, spidey)
    utils.ft_fetch(spidey)

if __name__ == "__main__":
    main(sys.argv)