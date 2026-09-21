from datetime import datetime

months_dict = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

days_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def get_sundays(year:int, month:int)-> list[str]:
    try: 
        max_date = months_dict[month]
        dates_list = []
        
        for day in range(1, max_date+1):
            date = datetime(year, month, day)
            day_of_week = date.weekday()
            day_name = days_list[day_of_week]

            if day_name == "Sunday":
                dates_list.append(str(date.date()))
            else:
                continue
            
        return dates_list
    except ValueError:
        print("Year must be a 4 digits number and month must be between 1 and 12.")

if __name__ == "__main__":
    res = get_sundays(2026, 12)
    print(f"🚀 {res}")
    
    