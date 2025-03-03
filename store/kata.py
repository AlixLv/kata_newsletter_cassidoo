from datetime import datetime, timedelta


def get_day_obj(str_date):
    date_list = str_date.split("-")

    #date_list_int = list(map(int, date_list))
    date_list_int = [int(element) for element in date_list]

    date_obj = datetime(date_list_int[0], date_list_int[1], date_list_int[2])
    return date_obj


def get_nb_weeks(closing_date, visit_date):
    closing_date_obj = get_day_obj(closing_date)
    visit_date_obj = get_day_obj(visit_date)

    # la soustraction des 2 objects date retourne une durée, de type class 'datetime.timedelta'
    # timedelta.days retourne le nombre total de jours dans la durée
    # // 7 division entière qui retourne le nombre de semaine 
    result = (closing_date_obj - visit_date_obj).days//7
    return result


def calculate_price(closing_date, visit_date, original_price):
    discount_price = original_price
    discount = 10
    weeks_nbr = get_nb_weeks(closing_date, visit_date) 
    
    while weeks_nbr > 0:
        discount_to_apply = (discount_price * discount) / 100
        discount_price -= discount_to_apply
        weeks_nbr -= 1  
           
    return discount_price

def main():
    res = calculate_price('2025-04-01', '2025-03-03', 100)
    print("🌈 ", res)


main()    




   