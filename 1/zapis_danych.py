def set_code():
    with open('code.txt', 'w') as file:
        file.write(input("Set code:\n"))


def unlock():
    set_new = 'n'
    with open('code.txt', 'r') as file:
        if input('Enter code:\n') == file.read():
            set_new = input('Code accepted.\nDo you want to set a new code? [y/n]\n')
        else:
            print('Incorrect.\n')
    if set_new in {'y', 'Y'}:
        set_code()


if __name__ == '__main__':
    while True:
        try:
            unlock()
        except FileNotFoundError:
            set_code()
