from cup import *

if __name__ == "__main__":
    cups_id = get_available_cups_id()

    cups_info = get_available_cups_info()

    print(f'Available Cups ID: {cups_id}')
    print(f'Available Cups Info: {cups_info}')