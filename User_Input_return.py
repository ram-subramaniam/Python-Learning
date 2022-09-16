calculation_to_units = 24
name_of_units = "Hours"


def days_to_units(num_of_days):
    print(f"{num_of_days} days are {int(num_of_days)*calculation_to_units} {name_of_units}.")


user_input = input("Hey User,enter the number of days \n")

days_to_units(user_input)
