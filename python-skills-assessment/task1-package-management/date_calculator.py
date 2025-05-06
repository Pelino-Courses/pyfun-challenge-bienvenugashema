from datetime import datetime


def time_function(start, end, format="%Y-%m-%d"):

    """
    You will enter time in this form year-month-day
    """
    try:
        st = datetime.strptime(start, format).date()
        en = datetime.strptime(end, format).date()
        difference = (en - st).days
        return difference
    except ValueError as e:
        print(f"Error for {start} or {end} : {e} or invalid date format" )

 
print(time_function.__doc__)
final_date = input("Enter final date: ")
initial_date = input("Enter Initial date: ")

print(time_function(initial_date, final_date))

