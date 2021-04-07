from termcolor import colored
from random import randrange
from recommender_gender import *
from recommender_subcategory import *
from recommender_profile_product import *
from recommender_main_category import *

colors = ["green", "blue", "yellow", "red", "cyan"]

def banner():
    """
    functie voor de banner
    :return
    """
    print(colored('''
        @=====================================================================@

         ██▀███  ▓█████  ▄████▄   ▄████▄   ▒█████   ███▄ ▄███▓▓█████  ███▄    █
        ▓██ ▒ ██▒▓█   ▀ ▒██▀ ▀█  ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █
        ▓██ ░▄█ ▒▒███   ▒▓█    ▄ ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███   ▓██  ▀█ ██▒
        ▒██▀▀█▄  ▒▓█  ▄ ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒
        ░██▓ ▒██▒░▒████▒▒ ▓███▀ ░▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒▒██░   ▓██░
        ░ ▒▓ ░▒▓░░░ ▒░ ░░ ░▒ ▒  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒
          ░▒ ░ ▒░ ░ ░  ░  ░  ▒     ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░░ ░░   ░ ▒░
          ░░   ░    ░   ░        ░        ░ ░ ░ ▒  ░      ░      ░      ░   ░ ░
           ░        ░  ░░ ░      ░ ░          ░ ░         ░      ░  ░         ░
                        ░        ░

        @=====================================================================@

    ''', colors[randrange(5)]))


