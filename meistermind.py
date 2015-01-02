import random

def meistermind():
    solution = ""
    turns = 8
    
    print "Meistermind"
    print "You have 8 tries to guess the right sequence"
    print "of four symbols (being the letters A through G)"
    
    colors = {
        1: "A",
        2: "B",
        3: "C",
        4: "D",
        5: "E",
        6: "F",
        7: "G"
    }

    c = 1
    while c < 5:
        s = random.randint(1,7)
        solution += colors[s]
        c += 1

    while turns > 0:    #game loop
        turns -= 1
        correct = 0
        almost = 0
        guess = ""

        error = True
        while error:
            guess = str(raw_input("your guess: ",)).upper()
            if len(guess) == 4:
                error = False
            else:
                print "Error: the sequence must contain exactly 4 symbols."

        if guess == solution:
            print "You have won!"
            break
        else:
            for index, c in enumerate(guess):
                if c == solution[index]:
                    correct += 1
                elif c in solution:
                    almost += 1            
        
        print correct, "correct, ", almost, "almost"
        print "You have",
        if turns == 0:
            print "lost!"
            print "Solution:", solution
        else:
            print turns, "guesses left."

    print "the End"
