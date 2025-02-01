# Initialize the list
items_list = []

def add():
    ask_user = input("What do you want to add to the list: ")
    items_list.append(ask_user)
    print(f"\n'{ask_user}' has been added to the list.\n")

def show():
    if not items_list:
        print("\nThe list is empty!\n")
    else:
        print("\nYour List:")
        for index, item in enumerate(items_list, start=1):
            print(f"{index}: {item}")
        print()

def remove():
    ask_to_remove = input("What do you want to remove: ")
    if ask_to_remove in items_list:
        items_list.remove(ask_to_remove)
        print(f"\n'{ask_to_remove}' has been removed from the list.\n")
    else:
        print("\nThis item is not in the list.\n")

print("Welcome to the List Manager!")

while True:
    print("\nLIST OF ACTIONS\n")
    print("1: Add items")
    print("2: Show items")
    print("3: Remove items")
    print("4: Quit")

    try:
        choice = int(input("Choose an option: "))
        if choice == 1:
            add()
        elif choice == 2:
            show()
        elif choice == 3:
            remove()
        elif choice == 4:
            print("\nThanks for using the List Manager. Goodbye!\n")
            break
        else:
            print("\nInvalid choice! Please choose a number between 1 and 4.\n")
    except ValueError:
        print("\nInvalid input! Please enter a number.\n")
