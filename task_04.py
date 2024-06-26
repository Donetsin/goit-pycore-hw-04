'''simple assistant bot'''
from colorama import Style, Fore
def parse_input(user_input):
    '''input value parser'''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    '''input data parser'''
    if len(args) != 2:
        return Fore.RED + 'Invalid input. Please use the format: add [name] [phone]' + Style.RESET_ALL
    name, phone = args
    contacts[name] = phone
    return Fore.GREEN + "Contact added." + Style.RESET_ALL

def update_contact(args, contacts):
    '''contacts updater'''
    if len(args) != 2:
        return Fore.RED + 'Invalid input. Please use the format: add [name] [new phone]'
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return Fore.GREEN + 'Contact updated.' + Style.RESET_ALL
    return 'Contact not found.'

def get_phone(args, contacts):
    '''show phone by contact name'''
    if len(args) != 1:
        return Fore.RED + 'Invalid input. Please use the format: phone [name]' + Style.RESET_ALL
    name = args[0]
    if name in contacts:
        return contacts[name]
    return 'Contact not found.'

def get_all(contacts):
    '''return all list of contacts'''
    return '\n'.join(f'{name}: {phone}' for name, phone in contacts.items())

def main():
    '''entry point'''    
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'update':
            print(update_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(get_all(contacts))
        else:
            print(Fore.RED + 'Invalid command.' + Style.RESET_ALL)

if __name__ == '__main__':
    main()
