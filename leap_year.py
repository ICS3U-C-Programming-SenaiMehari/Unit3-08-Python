def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


try:
    year = int(input("Enter a year: "))
    if year > 0:
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not leap year.")
    else:
        print("Please enter a positive year.")
except ValueError:
    print("Invalid input. Please enter a valid year as a positive integer.")
