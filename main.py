from helper import *

user_input = ""
while user_input != "exit":
    user_input = input(input_message)
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_unit_dictionary = {"days": days_and_units[0], "units": days_and_units[1]}
    print(days_and_unit_dictionary)
    validate_and_execute(days_and_unit_dictionary)


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
