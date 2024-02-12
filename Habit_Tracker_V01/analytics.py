#Analytics Module:
#These functions are for analyzing all recorded habits in the loaded DB.

from db import get_all_habits_from_db, get_all_habits_with_same_periodicity, get_longest_streak_from_db_all, get_longest_streak_from_db_habit, get_habit_tracking_data


def get_all_habits(db):
    """Function for getting all recorded Habits in the loaded DB. Returns a list of all entries in the table habits.
    :param db: the DB connection that is used to interact with the DB.
    """
    return get_all_habits_from_db(db)

def get_all_habits_periodicity(db, period):
    """Function for getting all recorded Habits with the same periodicity in the loaded DB. Returns a list of all entries in the table habits with given periodicity.
    :param db: the DB connection that is used to interact with the DB.
    :param period: periodicity that is used as filter.
    """
    return get_all_habits_with_same_periodicity(db, period)

def get_longest_recorded_streak_all(db):
    """Function for getting the alltime highest recorded streak of all habits. Returns the streak as integer.
    :param db: the DB connection that is used to interact with the DB.
    """
    return get_longest_streak_from_db_all(db)

def get_longest_recorded_streak_habit(db, name):
    """Function for getting the alltime highest recorded streak of a given habits. Returns the streak as integer.
    :param db: the DB connection that is used to interact with the DB.
    :param name: the name is used as filter.
    """
    return get_longest_streak_from_db_habit(db, name)

def get_entries_of_a_habit(db, name):
    """Function for getting the count of all entries for this habit.
    :param db: the DB connection that is used to interact with the DB.
    :param name: the name is used as filter.
    """
    return len(get_habit_tracking_data(db, name))