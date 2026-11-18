import datetime

date = input("Enter a date (in the format DD-MM-YYYY) : ")

birth_date = datetime.datetime.strptime(date, "%d-%m-%Y").date()
age = datetime.date.today() - birth_date

print(age.days // 365)

