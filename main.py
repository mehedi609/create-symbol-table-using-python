from symbol_table import insert, show, update, delete, search


def user_choice():
    choice_msg = [
        "Enter 1 for Insert",
        "Enter 2 for Show",
        "Enter 3 for Search",
        "Enter 4 for Update",
        "Enter 5 for Delete",
        "Enter 6 for Exit",
    ]

    while True:
        for msg in choice_msg:
            print(msg)

        _user_choice = input('\n Enter your choice from the list: ')

        if _user_choice == '1':
            user_data = input('\n Please enter comma separated data you want to add: ')
            print(insert(user_data))

        elif _user_choice == '2':
            show()

        elif _user_choice == '3':
            user_data = input('\n Please enter variable name you want to search: ')
            print(search(var_name=user_data))

        elif _user_choice == '4':
            user_data = input('\n Please enter variable name you want to update: ')
            print(update(var_name=user_data))

        elif _user_choice == '5':
            delete()

        elif _user_choice == '6':
            break
        else:
            print("You entered a wrong choice. Please try again \n")


if __name__ == '__main__':
    user_choice()
    print('Good Bye!!')

