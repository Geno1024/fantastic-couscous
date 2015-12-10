op = '0'
d = {}

while op != '2':
    op = raw_input('0 for write, 1 for read.\n')
    if op == '0':
        print('In write mode.')
        msg = raw_input('Input message.\n')
        pwd = raw_input('Input password.\n')
        d[pwd] = msg
        print('Write finished.')
    elif op == '1':
        print('In read mode.')
        pwd = raw_input('Input query password.\n')    
        if pwd in d:
            print('The message is:')
            print(d[pwd])
            d.pop(pwd)
        else:
            print('Not found.')
        print('Read finished.')
