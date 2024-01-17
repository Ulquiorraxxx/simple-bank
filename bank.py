# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# Datu tipi, mekle float - https://www.w3schools.com/python/python_datatypes.asp
# Pārbaudēm izmanto if...else - https://www.w3schools.com/python/python_conditions.asp
# Cipari https://www.w3schools.com/python/python_numbers.asp
# 

balance = float(0)

while True:
    print("\nBankas opcijas:")
    print("1. Ielikt naudu")
    print("2. Izņemt naudu")
    print("3. Pārbaudīt Balance")
    print("4. Iziet")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        bal_add = float(input("Summa: "))
        balance = balance + bal_add
        print("Balance = " , balance , "$")
    elif choice == '2':
        bal_remove = float(input("Summa: "))
        if balance < bal_remove:
            print("Nepietiek līdzekļu")
        else:
            balance = balance - bal_remove
            print("Jūs izņēmāt: " , bal_remove , "\nAtlikušais balance = " , balance , "$")    
    elif choice == '3':
        print("Balance = " , balance , "$")
    elif choice == '4':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
