from user_info import *

def test_get_gnz():
    gnz = get_gnz()
    print(f"GNZ: {gnz}")

def test_get_gems():
    gems = get_gems()
    print(f"Gems: {gems}")

def test_get_activity_points():
    activity_points = get_activity_points()
    print(f"Activity Points: {activity_points}")

def test_get_airdrop():
    airdrop = get_airdrop()
    print(f"Airdrop: {airdrop}")

def test_get_username():
    username = get_username()
    print(f"Username: {username}")

if __name__ == "__main__":
    test_get_gnz()
    test_get_gems()
    test_get_activity_points()
    test_get_airdrop()
    test_get_username()