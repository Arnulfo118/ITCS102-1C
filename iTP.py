first_year = int(input("Enter the first year: "))
second_year = int(input("Enter the second year: "))

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

leap_years = []
for year in range(first_year, second_year + 1):
    if is_leap_year(year):
        leap_years.append(year)

print("Leap years between", first_year, "and", second_year, "are:", leap_years)