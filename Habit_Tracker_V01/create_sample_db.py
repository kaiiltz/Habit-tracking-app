#Program for creating a sample database
#The databse is named sample.db
#If you want to create a new databse then make sure you deleted the old file, otherwise an exception is created
#Sample data is created for the predefined habits from main.py
#Each habit is a coherent block of entries
#Feel free to adjust or add the sample :D
#Just run the file

from db import get_db
from habit import Habit

#Creating the db connection and the habits
db = get_db("sample.db")
test_habit1 = Habit("Brush your teeth daily", db, "daily", True, "2023-01-01")
test_habit2 = Habit("Workout every week once", db, "weekly", True, "2023-01-01")
test_habit3 = Habit("Workout everyday", db, "daily", True, "2023-01-01")
test_habit4 = Habit("Spend quality time with your partner one evening every month", db, "monthly", True, "2023-01-01")
test_habit5 = Habit("Go every year one time to the dentist", db, "yearly", True, "2023-01-01")

#Sample data forhabit 1
test_habit1.check_habit("2023-01-01")
test_habit1.check_habit("2023-01-02")
test_habit1.check_habit("2023-01-03")
test_habit1.check_habit("2023-01-04")
test_habit1.check_habit("2023-01-05")
test_habit1.check_habit("2023-01-05")
test_habit1.check_habit("2023-01-07")
test_habit1.check_habit("2023-01-08")
test_habit1.check_habit("2023-01-09")
test_habit1.check_habit("2023-01-10")
test_habit1.check_habit("2023-01-12")
test_habit1.check_habit("2023-01-14")
test_habit1.check_habit("2023-01-20")
test_habit1.check_habit("2023-01-21")
test_habit1.check_habit("2023-01-22")
test_habit1.check_habit("2023-01-23")
test_habit1.check_habit("2023-01-24")
test_habit1.check_habit("2023-01-25")
test_habit1.check_habit("2023-01-26")
test_habit1.check_habit("2023-01-27")
test_habit1.check_habit("2023-01-28")
test_habit1.check_habit("2023-01-29")
test_habit1.check_habit("2023-01-30")
test_habit1.check_habit("2023-02-01")
test_habit1.check_habit("2023-02-02")


#Sample data forhabit 2
test_habit2.check_habit("2023-02-01")
test_habit2.check_habit("2023-02-02")
test_habit2.check_habit("2023-02-08")
test_habit2.check_habit("2023-02-15")
test_habit2.check_habit("2023-02-16")
test_habit2.check_habit("2023-02-20")
test_habit2.check_habit("2023-02-22")
test_habit2.check_habit("2023-03-01")
test_habit2.check_habit("2023-03-08")
test_habit2.check_habit("2023-03-20")
test_habit2.check_habit("2023-03-27")
test_habit2.check_habit("2023-04-10")
test_habit2.check_habit("2023-04-17")
test_habit2.check_habit("2023-04-24")
test_habit2.check_habit("2023-06-25")


#Sample data forhabit 3
test_habit3.check_habit("2023-01-01")
test_habit3.check_habit("2023-01-05")
test_habit3.check_habit("2023-01-06")
test_habit3.check_habit("2023-01-07")
test_habit3.check_habit("2023-01-10")
test_habit3.check_habit("2023-01-11")
test_habit3.check_habit("2023-01-12")
test_habit3.check_habit("2023-01-13")
test_habit3.check_habit("2023-01-14")
test_habit3.check_habit("2023-01-15")
test_habit3.check_habit("2023-01-16")
test_habit3.check_habit("2023-01-17")
test_habit3.check_habit("2023-01-18")
test_habit3.check_habit("2023-01-19")
test_habit3.check_habit("2023-01-20")
test_habit3.check_habit("2023-01-21")
test_habit3.check_habit("2023-01-21")
test_habit3.check_habit("2023-02-01")
test_habit3.check_habit("2023-02-03")
test_habit3.check_habit("2023-02-04")
test_habit3.check_habit("2023-02-06")
test_habit3.check_habit("2023-02-07")
test_habit3.check_habit("2023-02-08")
test_habit3.check_habit("2023-02-08")
test_habit3.check_habit("2023-03-20")
test_habit3.check_habit("2023-03-21")


#Sample data forhabit 4
test_habit4.check_habit("2023-01-15")
test_habit4.check_habit("2023-01-30")
test_habit4.check_habit("2023-02-10")
test_habit4.check_habit("2023-03-08")
test_habit4.check_habit("2023-04-13")
test_habit4.check_habit("2023-05-04")
test_habit4.check_habit("2023-06-21")
test_habit4.check_habit("2023-06-30")
test_habit4.check_habit("2023-08-19")
test_habit4.check_habit("2023-09-02")


#Sample data forhabit 5
test_habit5.check_habit("2020-05-25")
test_habit5.check_habit("2021-02-13")
test_habit5.check_habit("2021-12-31")
test_habit5.check_habit("2023-01-02")
test_habit5.check_habit("2023-11-20")
test_habit5.check_habit("2024-02-01")
