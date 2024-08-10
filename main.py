# print("200 is a great number")
# print(20 * 24 * 60)
calculation_to_units = 24
name_unit = "hours"


def days_to_units(no_of_days):
    print(f"{no_of_days} days are {no_of_days * calculation_to_units}  {name_unit}")


days_to_units(20)
days_to_units(35)
days_to_units(50)
days_to_units(110)


def days_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_unit}"
    elif num_of_days == 0:
        return "You entered zero , please enter a valid positive number"
    else:
        return "you entered a negative value so no conversion is required"
    # my_var = "variable inside"
    # print(to_hours)
    # print(num_of_days)
    # print(my_var)


days_to_units(20)


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0, please enter valid positive number")
        else:
            print("You entered negative value. Please enter correctly")
    except ValueError:
        print("your input is not a valid number, Don't ruin my program!")


user_input = ""
while user_input != "exit":
    user_input = input("Hwy User, enter number of days as comma separated list and I will convert it to hours!\n")
    print(type(user_input.split(", ")))
    print(user_input.split(", "))
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()

    # if user_input == "exit":
    #     print("You have exited the program. Thank you")


# print(f"20 days are {20 * to_units}  {name_unit}")
# print(f"35 days are {35 * to_units}  {name_unit}")
# print(f"50 days are {50 * to_units}  {name_unit}")
# print(f"110 days are {110 * to_units}  {name_unit}")
