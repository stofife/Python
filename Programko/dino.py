import curses, time, random, os, math

from numpy import true_divide

ground = list(3*"__.__.._,_,,,__._,")
print(len(ground)/3)
play = ["" for i in range(10)]

cacti = [" ** *", " ****", "***" " **"]

score = 0

# h: 10 lns, w: 18 lns

dino ="""     **** 
*    *****
*  ****\\ 
 ****** & 
  ****    
   L L
"""

dino =["     **** ", "*    *****", "*  ****\\ ", " ****** & ", "  ****", "  L L"]

stdscr = curses.initscr()

stdscr.nodelay(True)

while True:
    # set framerate
    time.sleep(1/30)
    
    #add score
    score += 1/10
    stdscr.addstr(2, 50, str(math.floor(score)))
    
    # getting input
    c = stdscr.getch()
    if c == ord("q"): 
        break
    if c == ord(" "):
        jump = 3
    
    #add obstacles
    if random.randint(1,1000) == 42:
        del ground[-5:-1]
        ground.append(random.choice(["**", "***"]))
    
    # draw ground
    ground.append(ground.pop(0))
    stdscr.addstr(9, 0, "".join(ground))
    
    #draw dino
    for i in range(6):
        stdscr.addstr(5+i, 0, dino[i])
    
    #refresh
    stdscr.refresh()

os.system("clear")