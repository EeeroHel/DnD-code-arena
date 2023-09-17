from Classes import Team
from Classes import Boon
import curses
import random

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

boons = [Boon("Positive", 1), Boon("Negative", -1)]
teams = [Team("Silver League", 4), Team("Fluxos", 4), Team("Tryouts", 4), Team("Funnies", 4)]

for i, team in enumerate(teams):
    team.conFunc()

def selectionFunc(teams):
    for i, team in enumerate(teams):
        match team.condition:
            case 4:
                boons[1].boonFunc()
                print(team.name + "4")
            case 3:
                number = random.randint(1, 5)
                if number >= 3:
                    target_team = random.choice(teams)  # Randomly select a target team
                    while target_team == team:  # Ensure the target is not the same as the current team
                        target_team = random.choice(teams)
                    target_team.condition -= 1  # Decrease the target team's condition
                else:
                    team.condition += 1
                print(team.name + "3")
            case 2:
                number = random.randint(1, 5)
                if number >= 2:
                    target_team = random.choice(teams)  # Randomly select a target team
                    while target_team == team:  # Ensure the target is not the same as the current team
                        target_team = random.choice(teams)
                    target_team.condition -= 1  # Decrease the target team's condition
                else:
                    team.condition += 1 
                print(team.name + "2")
            case 1:
                number = random.randint(1, 5)
                if number >= 1:
                    target_team = random.choice(teams)  # Randomly select a target team
                    while target_team == team:  # Ensure the target is not the same as the current team
                        target_team = random.choice(teams)
                    target_team.condition -= 1  # Decrease the target team's condition
                else:
                    team.condition += 1
                print(team.name + "1")

    for i, team in enumerate(teams):
        print(f"Team {i}: {team.name} | Condition: {team.condition}")
    return teams

selectionFunc(teams)
                