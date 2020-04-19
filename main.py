# Most recent update: 04/18/2020

menu = {}
menu['1'] = '1 - Add user'
menu['2'] = '2 - Remove user'
menu['3'] = '3 - Find user'
menu['4'] = '4 - Exit'

all_users = []

while True:
    options = menu.keys()
    print('Menu/Options:')
    print('-------------')
    for entry in options:
        print(menu[entry])

    selection = input('Please select an option 1 - 4:\t')

    if selection == '1':

        print('Add user - Enter the information for the new user:\t')
        first_name = input('First name:\t')
        last_name = input('Last name:\t')
        hair_color = input('Hair color:\t')
        eye_color = input('Eye color:\t')
        age = input('Age:\t')

        user_info = {}
        user_info['First name'] = first_name
        user_info['Last name'] = last_name
        user_info['Hair color'] = hair_color
        user_info['Eye color'] = eye_color
        user_info['Age'] = age

        print('Please check if the information is correct: ')
        print(user_info)
        info_check = input('Is the information correct? Y \ N:\t')

        while True:

            correction = str()
            if info_check == 'Y' or info_check == 'y' or info_check == 'yes' or info_check == 'Yes':
                print('Great! New user information has been added.\n')
                break

            if info_check == 'N' or info_check == 'n' or info_check == 'no' or info_check == 'No':
                correction = str(input('What info is wrong? Please enter "First name", "Last name", "Hair color", "Eye color", "Age" or "None"\t'))

                if correction == 'First name' or correction == 'first name':
                    user_info['First name'] = input(
                        'Ok. You have selected "First name". Please enter the correct information:\t')
                    print('Got it! The information has been updated!')
                    break

                if correction == 'Last name' or correction == 'last name':
                    user_info['Last name'] = input(
                        'Ok. You have selected "Last name". Please enter the correct information:\t')
                    print('Got it! The information has been updated!')
                    break

                if correction == 'Hair color' or correction == 'hair color':
                    user_info['Hair color'] = input(
                        'Ok. You have selected "Hair color". Please enter the correct information:\t')
                    print('Got it! The information has been updated!')
                    break

                if correction == 'Eye color' or correction == 'eye color':
                    user_info['Eye color'] = input(
                        'Ok. You have selected "Eye color". Please enter the correct information:\t')
                    print('Got it! The information has been updated!')
                    break

                if correction == 'Age' or correction == 'age':
                    user_info['Age'] = input('Ok. You have selected "Age". Please enter the correct information:\t')
                    print('Got it! The information has been updated!')
                    break

                if correction == 'None' or correction == 'none':
                    print('Thanks. The user has been added!')
                    break

            else:
                print('Invalid option. Please try again.')
                break

        all_users.append(user_info)

    if selection == '2':
        def getInfo (remove_first_name, remove_last_name):
            print('Please enter the information of the user you are looking for:\n')
        remove_first_name = input("User's first name:\t")
        remove_last_name = input("User's last name:\t")

        for item_to_delete in all_users:
            if item_to_delete['First name'] == remove_first_name and item_to_delete['Last name'] == remove_last_name:
                delete_item = item_to_delete
                print(delete_item)
                print('Is this the user you are looking for?\n', delete_item)
                correct_choice = input('Y / N ? ')

                if correct_choice == 'Y' or correct_choice == 'y' or correct_choice == 'yes' or correct_choice == 'Yes':
                    all_users.remove(delete_item)
                    print('This user has been removed.')
                    break

                if correct_choice == 'N' or correct_choice == 'n' or correct_choice == 'no' or correct_choice == 'No':
                    print('Please try searching for the user with option #3 to see if there is a user with that information.')
                    break
            else:
                print('Sorry. There is no user found with that information. Please try again.')
                delete_item = None


    if selection == '3':
        print('\nChoose how to look up a user')
        print('1 - First name')
        print('2 - Last name')
        print('3 - Hair color')
        print('4 - Eye color')
        print('5 - Age\n')
        print('6 - Exit\n')
        search_option = input('Enter option 1 - 6:\t')

        if search_option == '1' or search_option == 'First name' or search_option == 'first name':
            find_first_name = input('Please enter the first name of the user:\t')
            for item in all_users:
                if item['First name'] == find_first_name:
                    my_item = item
                    print('User found\n', my_item)
                    break
            else:
                print('Sorry. There is no user found with that information. Please try again')
                my_item = None

        if search_option == '2' or search_option == 'Last name' or search_option == 'last name':
            find_last_name = input('Please enter the last name of the user:\t')
            for item in all_users:
                if item['Last name'] == find_last_name:
                    my_item = item
                    print('User found\n', my_item)
                    break
            else:
                print('Sorry. There is no user found with that information. Please try again')
                my_item = None

        if search_option == '3' or search_option == 'Hair color' or search_option == 'hair color':
            find_hair_color = input('Please enter the hair color of the user:\t')
            for item in all_users:
                if item['Hair color'] == find_hair_color:
                    my_item = item
                    print('User found\n', my_item)
                    break
            else:
                print('Sorry. There is no user found with that information. Please try again')
                my_item = None

        if search_option == '4' or search_option == 'Eye color' or search_option == 'eye color':
            find_eye_color = input('Please enter the eye color of the user:\t')
            for item in all_users:
                if item['Eye color'] == find_eye_color:
                    my_item = item
                    print('User found\n', my_item)
                    break
            else:
                print('Sorry. There is no user found with that information. Please try again')
                my_item = None

        if search_option == '5' or search_option == 'Age' or search_option == 'age':
            find_age = input('Please enter the age f the user:\t')
            for item in all_users:
                if item['Age'] == find_age:
                    my_item = item
                    print('User found\n', my_item)
                    break
            else:
                print('Sorry. There is no user found with that information. Please try again')
                my_item = None

        if search_option == '6' or search_option == 'Exit' or search_option == 'exit':
            print('Exiting to main menu..........')
            my_item = None

    if selection == '4':
        print('Exiting program..........')
        break
