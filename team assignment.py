def display_menu():
    print("Please choose an option:")
    print("[1] View today's schedule")
    print("[2] Check weather forecast")
    print("[3] Read latest news")
    print("[4] Play a game")
    print("[5] Open calculator")
    print("[6] Play volleyball")
    print("[7] Display system info")
    print("[8] Help")
    print("[9] About this program")
    print("[0] Exit")


while True:
    display_menu()
    choice = input("Enter your choice [0–9]: ")

    if choice == "1":
        print("You selected 1: Viewing today's schedule.")
    elif choice == "2":
        print("You selected 2: Checking the weather forecast.")
    elif choice == "3":
        print("You selected 3: Reading the latest news.")
    elif choice == "4":
        print("You selected 4: Launching a game.")
    elif choice == "5":
        print("You selected 5: Opening calculator.")
    elif choice == "6":
        print("You selected 6: playing volleyball")
    elif choice == "7":
        print("You selected 7: Displaying system information.")
    elif choice == "8":
        print("You selected 8: Help section - choose a number to perform an action.")
    elif choice == "9":
        print("You selected 9: This program was created by Team XYZ for Module 4.")
    elif choice == "0":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between [0] and [9].")
