from pyfiglet import figlet_format
from termcolor import colored
valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")





def print_art(message, color):
    if color not in valid_colors:
        color = "magenta"

    ascii_art = figlet_format(message)
    colored_ascii = colored(ascii_art, color=color)
    print(colored_ascii)


message = input("What message do you want to print? ")
color = input("What color? ")

print_art(message, color)