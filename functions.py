calculation_to_units = 60*60
name_of_units = "minutes"


def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days*calculation_to_units} {name_of_units}.")
    print(custom_message)


days_to_units(10, "Awesome")
days_to_units(20, "Great")
days_to_units(30, "You are Great.")

