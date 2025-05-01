from datetime import datetime


def time_function(start, end):

    """
    You will enter time in this form year-month-day
    """

    st = datetime.strptime(start, "%Y-%m-%d")
    en = datetime.strptime(end, "%Y-%m-%d")
    difference = (en - st).days
    return difference

 
print(time_function.__doc__)
final_date = input("Enter final date: ")
initial_date = input("Enter Initial date: ")

print(time_function(initial_date, final_date))

