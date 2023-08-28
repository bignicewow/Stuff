def coke():
    amount_due = 50
    while amount_due > 0:
        print(f"Amount due: {amount_due}")
        amount = int(input("Insert Coin: "))
        if amount == 25 or amount == 10 or amount == 5:
            amount_due -= amount
    amount_due *= -1
    print(f"Change owed: {amount_due}")

coke()