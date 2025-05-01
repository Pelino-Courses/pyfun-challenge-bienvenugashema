from datetime import datetime


def time_function(start, end, format="%Y-%m-%d"):

    """
    You will enter time in this form year-month-day
    """

    st = datetime.strptime(start, format).date()
    en = datetime.strptime(end, format).date()
    difference = (en - st).days
    return difference

 
print(time_function.__doc__)
final_date = input("Enter final date: ")
initial_date = input("Enter Initial date: ")

print(time_function(initial_date, final_date))

