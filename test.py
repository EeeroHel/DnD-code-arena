import curses
stdscr = curses.initscr()

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(0, 0, "Press an arrow key (or any key) to see its keycode:")
    stdscr.refresh()
    
    key = stdscr.getch()
    
    stdscr.clear()
    stdscr.addstr(0, 0, f"Keycode: {key}")
    stdscr.refresh()
    
    stdscr.getch()  # Wait for a keypress to exit

curses.wrapper(main)