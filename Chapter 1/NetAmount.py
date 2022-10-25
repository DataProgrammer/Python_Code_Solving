


def BankAccount(amount, transaction_mode):
    netAmount = 10000;
    amount = int(amount)
    if transaction_mode=="D":
        netAmount += amount
    elif transaction_mode=="W":
        netAmount -= amount
    else:
        pass
    return netAmount;

print (BankAccount(100, "D"))





