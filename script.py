import hashlib
while True:
    chose = int(input('Choose the program:\n1 - generate hash\n2 - generate x zero hash:\n>> '))
    if chose == 1:
        str = input('Enter the string:\n>> ')
        print('HASH >> ' + hashlib.sha256(bytes(str, 'utf-8')).hexdigest() + ' <<')
    elif chose == 2:
        x = int(input('Enter the x:\n>> '))
        str = input('Enter the string:\n>> ')
        hash = hashlib.sha256(bytes(str, 'utf-8')).hexdigest()
        while hash[0:x] != '0'*x:
            hash = hashlib.sha256(bytes(hash, 'utf-8')).hexdigest()
            print(hash)
        print('HASH FOUND >> ' + hash + ' <<')
    print('\n')
