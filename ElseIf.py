calculation_to_units = 60*60
name_of_units = "minutes"


def days_to_units(num_of_days):

    if number_of_days > 0:
        print(f"{num_of_days} days are {num_of_days*calculation_to_units} {name_of_units}.")

    else:
        print("Invalid entry. Pls enter value over 0 days")


user_input = input("Hey User,enter the number of days \n")
user_input.isdigit()
user_input = number_of_days
days_to_units(number_of_days)





