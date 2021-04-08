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


def interface():
    """
    interface functie waar de gebruiker input kan hebben
    :return
    """

    banner()
    login_dict = {}

    login_dict['host'] = input(colored("\n\t" + "Geef je host op: ", "yellow"))
    login_dict['gebruiker'] = input(colored("\n\t" + "Geef je mysql username op: ", "yellow"))
    login_dict['wachtwoord'] = input(colored("\n\t" + "Geef je mysql password op: ", "yellow"))
    login_dict["dbNaam"] = input(colored("\n\t" + "Geef je mysql database op: ", "yellow"))

    end_1, start_1 = recommendation_gender(login_dict)
    print(colored("\n\t recommendation_gender finished!", "green"))
    end_2, start_2 = recommendation_subcategory(login_dict)
    print(colored("\n\t recommendation_subcategory finished!", "green"))
    end_3, start_3 = recommendation_profile_orders_process(login_dict)
    print(colored("\n\t recommendation_profile_order finished!", "green"))
    end_4, start_4 = recommendation_main_category(login_dict)
    print(colored("\n\t recommendation_main_category finished!", "green"))

    totaaltime = (end_1 - start_1) + (end_2 - start_2) + (end_3 - start_3) (end_4 - start_4)

    print(colored("\n\tTotal time taken, " + str(round(end_3 - start_3, 6)) + " seconds", "green"))


interface()
