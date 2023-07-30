while True:
    print('Type q for exit()')
    a = input('Enter your number: ')
    if a == 'q':
        break

    
    try:
      a = int(a)
      if a > 10 :
        print('{} is greater than 10'.format(a))
    except Exception as e:
       print('You enter you value')    

