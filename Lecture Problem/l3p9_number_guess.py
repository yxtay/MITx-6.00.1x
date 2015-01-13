print "Please think of a number between 0 and 100!"
low = 0
high = 100

while True:
    guess = (low + high) / 2
    
    while True:
        print "Is your secret number %d?" % guess
        print "Enter 'h' to indicate the guess is too high.",
        print "Enter 'l' to indicate the guess is too low.",
        print "Enter 'c' to indicate I guessed correctly.",
        direction = raw_input()
        if direction in 'lch':
            break
        print "Sorry, I did not understand your input."
        
    if direction == 'c':
        break
    elif direction == 'l':
        low = guess
    elif direction == 'h':
        high = guess
        
print "Game over. Your secret number was: %d" % guess