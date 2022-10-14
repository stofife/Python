import curses
from curses.textpad import Textbox, rectangle

def main(stdscr):
    rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
    stdscr.refresh()


    c = stdscr.getch()
    if c == ord(' '):
        stdscr.addstr(0,0, "Henlo")
        while True:
            c = stdscr.getch()
            if c == ord('q'):
                break
            stdscr.refresh()

curses.wrapper(main)