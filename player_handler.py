def get_user_input(board=[]):
    "Asks user for some input."
    user_input = input("Choose a position >")
    print('\n')

    x, y = user_input.split(',')
    x = int(x.strip())
    y = int(y.strip())
    return (x,y)
