options = ['start', 'stop', 'help', 'quit']
started = False

command = ''

while True:
    command = input('> ').lower()
    if command == options[0]:
        if started:
            print('Car is already started...')
        else:
            started = True
            print('Car is started...')
    elif command == options[1]:
        if started:
            print('Car is stopped...')
            started = False
        else:
            print('Car is already stopped...')
    elif command == options[2]:
        print('''
start -- to start the car
stop  -- to stop the car
quit  -- to finish the experience
        ''')
    elif command == options[3]:
        break
    else:
        print("Sorry, I don't understand you...")
