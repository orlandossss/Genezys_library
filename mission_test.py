from mission import *

if __name__ == "__main__":
    all_missions_rewards, missions_info = get_missions()
    print("All Missions Rewards:", all_missions_rewards)
    print("Missions Info:")
    for mission in missions_info:
        print(mission)