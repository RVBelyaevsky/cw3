from utils.utils import last_five_operations, result_description

valid_transactions = last_five_operations()

for i in range(5):
    result_description(valid_transactions[i])

