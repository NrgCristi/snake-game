# setup window
win = curses.newwin(20, 60, 0, 0) # y,x
win.keypad(1)
win.border(0)
win.nodelay(1) # -1

# snake and food
snake = [(4, 10), (4, 9), (4, 8)]
food = (10, 20)


#game logic
score = 0

ESC = 27
key = curses.KEY_RIGHT

while key != ESC:
    win.addstr(0, 2, 'Score ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake)//10 % 120) # increase speed
    
    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key
    
    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key
     
    #if snake runs over itself
    if snake [0] in snake[1:]: break
    
    if snake[0] == food:
        # eat the food
        score += 1
        food = ()
        while food == ():
            food = (radint(1,18), radint(1,58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '#')
    else:
        # move snake
        last = snake.pop()
        win.addch(last[0], last[1], ' ')
        
    win.addch(snake[0][0], snake[0][1], '*')

print(f"Final score = {score}")