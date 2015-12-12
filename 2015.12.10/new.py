boxCount = 20
box = range(boxCount)
op = '0'
emptyList = range(boxCount)
boxes = {}
boxes = boxes.fromkeys(box, 'empty')

while True:
    op = raw_input('0 for set, 1 for get.\n')
    if op == '0':
        print('In set mode.')
        print('ID of empty box(es) are:')
        print(emptyList)
        boxToSet = -1
        if emptyList == []:
            print('Error. Box full.')
            continue
        while boxToSet not in emptyList:
            boxToSet = input('Input a valid box number to set.\n')
        packet = raw_input('Input packet.\n')
        password = raw_input('Input password.\n')
        telNum = raw_input('Input target tel number.\n')
        emptyList.pop(boxToSet)
        boxes[boxToSet] = {'packet': packet, 'password': password, 'telNum': telNum}
        print('Set finished.')
    elif op == '1':
        print('In get mode.')
        if emptyList == range(boxCount):
            print('All boxes are empty. Nothing to get.')
            continue
        telNum = raw_input('Input your tel number.\n')
        password = raw_input('Input password.\n')
        ifAnyBoxRight = False
        for (x, y) in boxes.items():
            if y != 'empty':
                if y['password'] == password and y['telNum'] == telNum:
                    ifAnyBoxRight = True
                    targetX = x
                    targetPacket = y['packet']
        if ifAnyBoxRight == False:
            print('Error. No corresponding packet found. Password or telNum incorrect.')
        else:
            print('Get packet success. Packet index is:')
            print(targetX)
            print('Packet is:')
            print(targetPacket)
            emptyList.append(targetX)
            emptyList = list(set(emptyList))
        print('Get finished.')

