from transaction_history import *

if __name__ == "__main__":
    transaction_history_info = get_transaction_history(2)

    print("Transaction History:")
    for transaction in transaction_history_info:
        print(transaction)