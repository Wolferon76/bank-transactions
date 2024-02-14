# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# 

transactions = []

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. List last 10 transactions")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        # deposit, jāpievieno jaunu transakciju
        # https://www.w3schools.com/python/python_lists_add.asp
        deposit = int(input("Please, how much money do you want to deposit into your account: "))
        
        transactions.append(deposit)
        print(transactions)

        pass
    elif choice == '2':
        # withdraw, jāpievieno jaunu transakciju ar mīnus zīmi
        # https://www.w3schools.com/python/python_lists_add.asp
        Withdraw = int(input("Please, how much money do you want to Withdraw from your account: "))
        Withdraw = Withdraw *-1
        transactions.append(Withdraw)
        print(transactions)
        pass
    elif choice == '3':
        # pārbaudīt atlikumu
        # jasummē visus saraksta elementus kopā ar ciklu palidzību
        # https://www.w3schools.com/python/python_for_loops.asp
        Withdraw = Withdraw *-1
        if Withdraw > deposit:
            print("E.R.O.R.")
        elif Withdraw < deposit:
            balance = deposit - Withdraw
            transactions.append(balance)
           
        print(transactions)

        balance = 0
        for t in transactions:
            balance += t

        print("Balance:", balance)

        pass
    elif choice == '4':
        # rāda 10 pēdējas transakcijas
        # https://www.w3schools.com/python/python_lists_access.asp (Range of Negative Indexes)
        print(transactions[-10:-1])
        pass
    elif choice == '5':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
