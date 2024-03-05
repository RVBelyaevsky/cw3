from utils.utils import last_five_operations, result_description, result_transaction, result_summ

valid_transactions = last_five_operations()

for i in range(5):
    print(result_description(valid_transactions[i]))
    print(result_transaction(valid_transactions[i]))
    print(result_summ(valid_transactions[i]))
    print()
