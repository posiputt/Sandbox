def show_menu (games):
    print "Hello!"
    print "Choose your game or press Q and Enter to quit."
    for g in games:
        print "\t" + g + ") " + games[g]

quit = False

while not (quit):
    games = {
        "1": "Place Holder",
        "2": "No Game Here",
    }
    show_menu(games)
    choice = str(raw_input())
    if choice.lower() == "q":
        quit = True
