from market import *

if __name__ == "__main__":
    info = get_market(order='desc', sortBy='date', max_results=2)

    print(info)