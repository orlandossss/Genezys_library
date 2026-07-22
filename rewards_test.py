from rewards import *

if __name__ == "__main__":
    id, reward_type, reward_quantity, item_id = get_daily_rewards_info()
    missions_info = get_missions_info()

    print("Daily Rewards Info:")
    print(f"ID: {id}")
    print(f"Reward Type: {reward_type}")
    print(f"Reward Quantity: {reward_quantity}")
    print(f"Item ID: {item_id}")
    print("\nMissions Info:")
    for mission in missions_info:
        print(mission)
