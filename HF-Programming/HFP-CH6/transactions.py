def save_transaction(price, credit_card, description):
    file = open("transactions.txt", "a")
    file.write("%s%07d%s\n" % (price * 100, credit_card, description))
    file.close()