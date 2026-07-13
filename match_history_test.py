from match_history import *

if __name__ == "__main__":
    match_history_info = get_match_history(1)

    print("Match History:")
    for match in match_history_info:
        print(match)