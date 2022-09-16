calculation_to_units = 60*60
name_of_units = "minutes"


def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days*calculation_to_units} {name_of_units}.")


user_input = input("Hey User,enter the number of days \n")
number_of_days = int(user_input)

days_to_units(number_of_days)
