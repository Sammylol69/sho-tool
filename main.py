import os
import fade
os.system('clear')
logo_text = "  ██████  ██░ ██  ▒█████     ▄▄▄█████▓ ▒█████   ▒█████   ██▓    \n▒██    ▒ ▓██░ ██▒▒██▒  ██▒   ▓  ██▒ ▓▒▒██▒  ██▒▒██▒  ██▒▓██▒    \n░ ▓██▄   ▒██▀▀██░▒██░  ██▒   ▒ ▓██░ ▒░▒██░  ██▒▒██░  ██▒▒██░    \n  ▒   ██▒░▓█ ░██ ▒██   ██░   ░ ▓██▓ ░ ▒██   ██░▒██   ██░▒██░    \n▒██████▒▒░▓█▒░██▓░ ████▓▒░     ▒██▒ ░ ░ ████▓▒░░ ████▓▒░░██████▒\n▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░▒░▒░      ▒ ░░   ░ ▒░▒░▒░ ░ ▒░▒░▒░ ░ ▒░▓  ░\n░ ░▒  ░ ░ ▒ ░▒░ ░  ░ ▒ ▒░        ░      ░ ▒ ▒░   ░ ▒ ▒░ ░ ░ ▒  ░\n░  ░  ░   ░  ░░ ░░ ░ ░ ▒       ░      ░ ░ ░ ▒  ░ ░ ░ ▒    ░ ░   \n      ░   ░  ░  ░    ░ ░                  ░ ░      ░ ░      ░  ░\n                                                                "
faded_text = fade.greenblue(logo_text)
print(faded_text)
qf = input("Pick a number: ")