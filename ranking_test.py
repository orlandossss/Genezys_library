from ranking import *
from get_cup import *

if __name__ == "__main__":
    cups = get_available_cups_id()
    cup_id = cups[0]
    own, other = cup_leaderboard(cup_id, 10)
    print(f'{own=}, {other=}')

    own, other = division_leaderboard(10)
    print(f'{own=}, {other=}')