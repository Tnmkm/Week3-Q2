'''
Find the number of days in the given month and year 

    Leap year (where February has 29 days) is the year that is either
        - a divisible by 400 OR 
        - b divisible by 4 but not divisible by 100
        Examples of leap year: 2000, 2020, 2024, 4, 40
        Examples of non-leap year (February has 28 days): 2025, 2019, 2100, 100
    
    If input doesn't exist return 'Error'
'''

# Student do quiz here below
# do not change the function name
# do not change the function input

# def NumberOfDays(month,year):
#     month = int(input("Enter month (1-12): "))
#     year = int(input("Enter year : "))
#     if month < 1 or month > 12 or year < 1:
#         return 'Error'
#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31   
#     elif month in [4, 6, 9, 11]:
#         return 30
#     elif month == 2:
#         if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#             return 29
#         else:
#             return 28

#     return 0 
# print("Number of days:", NumberOfDays(month, year))  # Example usage

# def NumberOfDays(month, year):
#     if month < 1 or month > 12 or year < 1:
#         return "Error"

#     def is_leap_year(y):
#         if y % 400 == 0:
#             return True
#         elif y % 4 == 0 and y % 100 != 0:
#             return True
#         else:
#             return False

#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         return 31
#     elif month in [4, 6, 9, 11]:
#         return 30
#     elif month == 2:
#         return 29 if is_leap_year(year) else 28
#     return "Error"
#     print("Number of days:", NumberOfDays(month, year))   




def NumberOfDays(month, year):
    print(month,year)
    if not isinstance(month, int) or not isinstance(year, int):
        return "Error"
    if month <= 0  or month > 12:
        return "Error"
    leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

    if month in (1, 3, 5, 7, 8, 10, 12):
        return 31
    elif month in (4, 6, 9, 11):
        return 30
    elif month == 2:
        return 29 if leap else 28
    else:
        return "Error"