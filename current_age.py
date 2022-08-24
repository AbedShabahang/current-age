# Abed Shabahang
# Checking the correctness of the date format and calculating the current age
#----------------------------------------------------------------------------

import datetime

date_string = str(input("Please enter your date of birth as YYYY/MM/DD: \n"))
format = '%Y/%m/%d'
try:
    datetime.datetime.strptime(date_string, format) #Checking the correctness of the date format and calculating the current age
    list_date_string= date_string.split("/")
    year = int(list_date_string.pop(0))
    age = 2022 - year
    print(age)

except ValueError:
    print("WRONG")

