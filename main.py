# print("200 is a great number")
# print(20 * 24 * 60


def days_to_units(no_of_days, calculation_to_units):
    if calculation_to_units == "hours":
        return f"{no_of_days} days are {no_of_days * 24}  hours"
    elif calculation_to_units == "minutes":
        return f"{no_of_days} days are {no_of_days * 24 * 60}  minutes"
    else:
        return "unsupported units"


# def days_to_units(num_of_days, conversion_unit):
#     if num_of_days > 0:
#         return f"{num_of_days} days are {num_of_days * conversion_unit} {name_unit}"
#     elif num_of_days == 0:
#         return "You entered zero , please enter a valid positive number"
#     else:
#         return "you entered a negative value so no conversion is required"
#     # my_var = "variable inside"
#     # print(to_hours)
#     # print(num_of_days)
#     # print(my_var)
#
#
# days_to_units(20)


def validate_and_execute():
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


user_input = ""
while user_input != "exit":
    user_input = input("Hwy User, enter number of days and I will convert it to hours!\n")
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_unit_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()

    # list_of_days = user_input.split(", ")
    # print(list_of_days)
    # print(set(list_of_days))
    # print(type(set(list_of_days)))
    # for num_of_days_element in set(user_input.split(", ")):
    #     validate_and_execute()

    # if user_input == "exit":
    # print("You have exited the program. Thank you")

# print(f"20 days are {20 * to_units}  {name_unit}")
# print(f"35 days are {35 * to_units}  {name_unit}")
# print(f"50 days are {50 * to_units}  {name_unit}")
# print(f"110 days are {110 * to_units}  {name_unit}")
