'''Module providing a function.'''
from pathlib import Path
from colorama import Style, Fore

def print_directory_structure(startpath, prefix: str = ''):
    '''function returns folders structure as a tree'''
    root = Path(startpath)
    if not root.is_dir():
        print(f'{root} is not a directory')
        return

    files = sorted([file for file in root.iterdir()])
    for i, element in enumerate(files):
        connector = '├──' if i < len(files) - 1 else '└──'
        directory_font = f"{prefix}{connector}" + Fore.BLUE + f"{element.name}" + Style.RESET_ALL
        file_font = f"{prefix}{connector}" + Fore.GREEN + f"{element.name}" + Style.RESET_ALL
        printline = directory_font if element.is_dir() else file_font
        print(printline)
        if element.is_dir():
            extension = '│   ' if i < len(files) - 1 else '    '
            prefix += extension
            print_directory_structure(element, prefix)
