import colorama

import time

from colorama import Fore, Back, Style

print(""""


█▀▀ █▀▀█ █── █▀▀█ █▀▀█ █───█ █▀▀█ █──█
█── █──█ █── █──█ █▄▄▀ █▄█▄█ █▄▄█ █▄▄█
▀▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀▀ ▀─▀▀ ─▀─▀─ ▀──▀ ▄▄▄█
"""

)

options = input("Enter the color you want text to print in:\n")
if options == "blue":
 colorblue = input("What text you want to print in blue:\n")
print(Fore.BLUE + f'{colorblue}')

# more colors coming soon
