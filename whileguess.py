number = 23
running = True
while running:
    guess = int(raw_input('enter an integer'))
    if guess == number:
        print 'congratulations'
        running = False
    elif guess < number:
        print 'no,it is little higher than that'
    else:
        print 'no,it is little lower than that'
print 'the while loop is over'
    
