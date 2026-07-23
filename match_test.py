from match import *
from cup import get_available_cups_id
import time


if __name__ == "__main__":
    cups_id = get_available_cups_id()
    run_division_match()
    for cup_id in cups_id:
        match_info = run_cup_match(cup_id)
        print(f"Match Info for Cup {cup_id}: {match_info}")
        time.sleep(1) 