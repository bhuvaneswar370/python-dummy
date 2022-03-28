calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    #conditional_check = num_of_days > 0
    #print(type(conditional_check))
    #if num_of_days > 0:
        return f"{num_of_days} day are {num_of_days * calculation_to_units} {name_of_unit}"
    #elif num_of_days == 0:
    #    return "you entered 0, please enter a valid positive number"
    #else:
    #    return "you entered a negative value, no converstion for you!"
   
def validate_and_execute():
    if user_data.isdigit():
        user_input_number = int(user_data)
        if user_input_number > 0:
            elif user_input_number == 0:
                print("you entered 0, please enter a valid positive number")
        else:
            print("you entered a negative value, no converstion for you!")
        calculated_value = days_to_units(user_input_number)
        print(calculated_value)
    else:
        print("your input is not a number, Don't ruin my program!")
user_data = input("Hey User, enter a number of days and I will convert it to hour!\n")
validate_and_execute()