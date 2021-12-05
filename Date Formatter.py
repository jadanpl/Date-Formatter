dd=""
def what_is_the_day(day_of_the_year):
    if day_of_the_year==1 or day_of_the_year==21 or day_of_the_year==31:
        dd = str(day_of_the_year) + "st"
        return dd
    elif day_of_the_year==2 or day_of_the_year==22:
        dd = str(day_of_the_year) + "nd"
        return dd
    elif day_of_the_year==3 or day_of_the_year==23:
        dd = str(day_of_the_year) + "rd"
        return dd
    else:
        dd = str(day_of_the_year) + "th"
        return dd
result_dd=what_is_the_day(int(input("Enter a date: ")))


def what_is_the_month(month_of_year):
    month=month_of_year.lower()
    if month=="january" or month=="jan" or month_of_year=="1":
        return "January"
    elif month=="february" or month=="feb" or month_of_year=="2":
        return "February"
    elif month == "march" or month == "mar" or month_of_year == "3":
        return "March"
    elif month=="april" or month=="apr" or month_of_year=="4":
        return "April"
    elif month=="may" or month_of_year=="5":
        return "May"
    elif month == "june" or month == "jun" or month_of_year == "6":
        return "June"
    elif month == "july" or month == "jul" or month_of_year == "7":
        return "July"
    elif month == "august" or month == "aug" or month_of_year == "8":
        return "August"
    elif month == "september" or month == "sep" or month_of_year == "9":
        return "September"
    elif month == "october" or month == "oct" or month_of_year == "10":
        return "October"
    elif month == "november" or month == "nov" or month_of_year == "11":
        return "November"
    elif month == "december" or month == "dec" or month_of_year == "12":
        return "December"
    else:
        print("Please enter the month in digits or words.")
result_mm=what_is_the_month(input("Enter the month in digits or words: "))

# is it a leap year?
year=int(input("Enter year: "))
def what_is_the_year(year_from_user):
    if year_from_user % 400 ==0:
        return "It is a leap year."
    elif year_from_user % 100 == 0:
        return "It is not a leap year."
    elif year_from_user % 4 == 0:
        return "It is a leap year."
    else:
        return "It is not a leap year."
result_yy=what_is_the_year(year)

number_of_days=0
if result_mm=="January" or result_mm=="March" or result_mm=="May" or result_mm=="July" or result_mm=="August" or result_mm=="October" or result_mm=="December":
    number_of_days=31
elif result_mm=="April" or result_mm=="June" or result_mm=="September" or result_mm=="November":
    number_of_days=30
else:
    if result_yy == "It is a leap year.":
        number_of_days=29
    else:
        number_of_days = 28


print("It is ", result_dd, result_mm, year, ". ",result_yy,result_mm," has ",number_of_days," days.")

