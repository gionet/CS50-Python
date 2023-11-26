def main():

    amount = 50
    while amount > 0:
        print(f"Amount Due: { amount }")
        change = int(input("Insert Coin: "))
        if change == 5 or change == 10 or change == 25:
            amount -= change

    print(f"Change Owed: {abs(amount)}")

if __name__ == "__main__":
    main()