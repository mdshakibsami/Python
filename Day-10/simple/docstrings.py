#documentation of a function is called docstrings

def leap_year(year):
    """
    Takes a year and return this year is leap year or not
    """
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else:
        return False

def days_in_month(y,m):
    """
    Take year and month as input and return the day in that month
    """
    month_days = [31,28,31,30,31,30,31,31.30,31,30,31]
    if m>12 or m<1:
        return "Invalid month input"
    elif m==2 and leap_year(year=y):
        return 29
    else:
        return month_days[m-1]

#Do not change anay code 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(y=year,m=month)
print(days)