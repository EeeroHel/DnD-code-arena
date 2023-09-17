from Classes import Team
from Classes import Boon
from faker import Faker
from Selections import selectionFunc
import curses

fake = Faker()

teams = [Team("Silver League", 4), Team("Fluxos", 4), Team("Tryouts", 4), Team("Funnies", 4)]

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

def main(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()
    

    menu_options = ["Display Current Round", "Display all teams", "Begin next round", "Exit"]
    current_round = 1

    current_option = 0

    while True:
        
        
        for i, option in enumerate(menu_options):
            if i == current_option:
                stdscr.addstr(i, 0, option, curses.A_REVERSE)
            else:
                stdscr.addstr(i, 0, option)

        stdscr.refresh()

        key = stdscr.getch()

        if key == 456:
            if current_option < len(menu_options) - 1:
                current_option += 1
        elif key == 450:
            if current_option > 0:
                current_option -= 1
        elif key == 10:  # Enter key
            stdscr.clear()
            match current_option:
                case 0:
                    stdscr.addstr(len(menu_options) + 1, 0, f"Current Round: {current_round}")
                case 1:
                    for i, team in enumerate(teams, start=1):
                        stdscr.addstr(len(teams) + i, 0, f"Team {i}: {team.name} | Condition: {team.condition}")
                case 2:
                    for i, team in enumerate(teams):
                        team.conFunc()
                        stdscr.addstr(len(teams) + i, 0, f"Team {i}: {team.name} | Condition: {team.condition}")
                    current_round += 1
                    selectionFunc(teams)
                    for i, team in enumerate(teams):
                        if team.condition <= 0:
                            teams.remove(team)
            if current_option == len(menu_options) - 1:
                break  

            
        stdscr.refresh()

# Initialize curses and clean up properly
curses.wrapper(main)