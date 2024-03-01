from utils.utils import last_five_operations, result_description, result_trasaction, result_summ

valid_transactions = last_five_operations()

for i in range(5):
    result_description(valid_transactions[i])
    result_trasaction(valid_transactions[i])
    result_summ(valid_transactions[i])
    print()
