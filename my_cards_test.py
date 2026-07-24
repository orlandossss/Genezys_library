from my_cards import *

if __name__ == "__main__":
    info = get_my_cards(order='desc', sortBy='baseScore', max_results=2)

    print(info)