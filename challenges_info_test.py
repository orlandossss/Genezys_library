from challenges_info import *

if __name__ == "__main__":
    challenges_info = get_challenges_info()

    print("Challenges:")
    for challenge in challenges_info:
        print(challenge)