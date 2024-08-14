def days_to_units(no_of_days, calculation_to_units):
    if calculation_to_units == "hours":
        return f"{no_of_days} days are {no_of_days * 24}  hours"
    elif calculation_to_units == "minutes":
        return f"{no_of_days} days are {no_of_days * 24 * 60}  minutes"
    else:
        return "unsupported units"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["units"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0, please enter valid positive number")
        else:
            print("You entered negative value. Please enter correctly")
    except ValueError:
        print("your input is not a valid number, Don't ruin my program!")


input_message = "Hwy User, enter number of days and I will convert it to hours!\n"
