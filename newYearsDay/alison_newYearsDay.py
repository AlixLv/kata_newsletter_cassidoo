# Given a year, return the day of the week for New Year's Day of that year."""

from datetime import date

def new_years_day(year):
    date_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
    if type(year) == int and len(str(year)) == 4:
        # objet date(année, mois, jour) + methode weekday() qui retourne un int correspondant au jour de la semaine
        ordinal_day = date_dict[date(year, 1,1).weekday()]
        return ordinal_day
    else:
        print(f"{year} is not in the format yyyy-- please enter a four-digit integer.")
        return


print(new_years_day(2023))
