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

        print('')
        _user_choice = input('Enter your choice from the list: ')

        if _user_choice == '1':
            print('')
            user_data = input('Please enter comma separated data: ')
            print(insert(user_data))

        elif _user_choice == '2':
            show()
        elif _user_choice == '3':
            search()
        elif _user_choice == '4':
            update()
        elif _user_choice == '5':
            delete()
        elif _user_choice == '6':
            break
        else:
            print("You entered a wrong choice. Please try again \n")


if __name__ == '__main__':
    user_choice()
    print('Good Bye!!')

