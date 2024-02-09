#Test suite for the habit tracker
#Using pytest
#In setup_method:
#   DB connection is made
#   all Data is stored in the file test.db
#In teardown_method
#   DB connection is closed
#   test.db file is deleted
#Note: the db file is deleted after each run. If you want to keep the file after one run youhave to adjust the teardown_method!
#Also Note: the test run will fail, because the names of the habits repeats in the tests. Also if you rerun the test there will be an exception because of the filled db file
#First test test_habit() is for testing if the habit is correctly created in the db with given parameters and the entries are correct and retirevable
#Second test test analitics() is for testing streak handling with different situations and the analitics functions
#Third test test_habit_cheking() i for checking the logic of the habit handling by giving various dates as inputs

import os
from datetime import date
from habit import Habit
from db import get_db, get_habit_tracking_data, get_habit_information_data, write_entry, add_habit
from analytics import get_all_habits, get_all_habits_periodicity, get_longest_recorded_streak_habit, get_longest_recorded_streak_all, get_entries_of_a_habit

class Test_Suite:

    def setup_method(self):
        self.db = get_db("test.db")

    def test_habit(self):
        test_habit = Habit("Test Habit", self.db, "daily", True)
        test_habit.check_habit("2024-01-01")
        test_habit.check_habit("2024-01-02")
        test_habit.check_habit("2024-01-03")
        test_habit.check_habit("2024-01-04")
        test_habit.check_habit("2024-01-05")
        test_habit.check_habit("2024-01-07")


        assert test_habit.get_entries() == 6
        assert test_habit.get_habit_period() == "daily"
        assert str(test_habit.get_last_entry()) == "2024-01-07"
        assert test_habit.get_act_streak() == 1
        assert test_habit.name == "Test Habit"

    def test_analitics(self):
        test_habit1 = Habit("Test Habit1", self.db, "daily", True, "2024-01-01")
        test_habit2 = Habit("Test Habit2", self.db, "weekly", True, "2024-01-01")
        assert get_all_habits(self.db) == [('Test Habit1', 'daily', "2024-01-01"), ('Test Habit2', 'weekly', "2024-01-01")]
        assert get_all_habits_periodicity(self.db, "daily") == [('Test Habit1', 'daily', "2024-01-01")]
        assert get_all_habits_periodicity(self.db, "weekly") == [('Test Habit2', 'weekly', "2024-01-01")]

        assert test_habit1.get_creation_date() == "2024-01-01"

        test_habit1.check_habit("2024-01-01")
        test_habit1.check_habit("2024-01-02")
        test_habit1.check_habit("2024-01-03")
        test_habit1.check_habit("2024-01-04")
        test_habit1.check_habit("2024-01-05")

        test_habit2.check_habit("2024-01-01")
        test_habit2.check_habit("2024-01-08")
        test_habit2.check_habit("2024-01-15")
        test_habit2.check_habit("2024-01-25")
        test_habit2.check_habit("2024-02-01")

        assert test_habit1.get_act_streak() == 5
        assert test_habit2.get_act_streak() == 2

        test_habit1.check_habit("2024-01-08")
        test_habit2.check_habit("2024-02-08")

        assert test_habit1.get_act_streak() == 1
        assert test_habit2.get_act_streak() == 3

        test_array = get_longest_recorded_streak_all(self.db)
        assert test_array[1] == 5
        test_array = get_longest_recorded_streak_habit(self.db, test_habit1.name)
        assert test_array[1] == 5
        test_array = get_longest_recorded_streak_habit(self.db, test_habit2.name)
        assert test_array[1] == 3

        assert get_entries_of_a_habit(self.db, test_habit1.name) == 6
        assert get_entries_of_a_habit(self.db, test_habit2.name) == 6
    
    def test_habbit_checking(self):
        
        test_habit1 = Habit("Test Habit1", self.db, "daily", True)
        test_habit2 = Habit("Test Habit2", self.db, "weekly", True)
        test_habit3 = Habit("Test Habit3", self.db, "monthly", True)
        test_habit4 = Habit("Test Habit4", self.db, "yearly", True)

        assert test_habit1.check_habit("2024-01-01") == 1
        assert test_habit1.check_habit("2024-01-01") == -1
        assert test_habit1.check_habit("2024-01-02") == 1
        assert test_habit1.check_habit("2024-01-04") == 0

        assert test_habit2.check_habit("2024-01-01") == 1
        assert test_habit2.check_habit("2024-01-01") == -1
        assert test_habit2.check_habit("2024-01-08") == 1
        assert test_habit2.check_habit("2024-01-16") == 0

        assert test_habit3.check_habit("2024-01-01") == 1
        assert test_habit3.check_habit("2024-01-01") == -1
        assert test_habit3.check_habit("2024-01-31") == -1
        assert test_habit3.check_habit("2024-02-01") == 1
        assert test_habit3.check_habit("2024-03-30") == 1
        assert test_habit3.check_habit("2024-05-01") == 0

        assert test_habit4.check_habit("2024-01-01") == 1
        assert test_habit4.check_habit("2024-01-01") == -1
        assert test_habit4.check_habit("2024-12-31") == -1
        assert test_habit4.check_habit("2025-02-01") == 1
        assert test_habit4.check_habit("2026-12-31") == 1
        assert test_habit4.check_habit("2028-03-15") == 0
   

    def teardown_method(self):
            
        self.db.close()
        os.remove("test.db")