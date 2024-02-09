#DB library
#Based on the SQLite3 library
#This library contains all functions which are used to directly read or write to the db file


import sqlite3
from datetime import date


def get_db(name="main.db"):
    """Function to create DB connection. It isn´t important if the db file exists or not. If not a new blank db is created.
    Returns the DB Connection. Creates tables in a new db file.
    :param name: The name of the used db file in the project directory. Is left empty main.db is used
    """
    # Cathing an exception in case of faulty name
    try:
        db = sqlite3.connect(name)
        create_table(db)
        return db
    except:
        print("Exception cought during creating a database with faulty name!")
        print("You have to note that special characters like (:), (;) or others can create exceptions!")

def create_table(db):
    """Function to creat tables in the given db file.
    The table habit with the columns name, period, creation date and the table tracker with the columns date, streak, habitName are created if not existing.
    :param db: forwarded DB connection"""
    cur = db.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS habit (
        name TEXT PRIMARY KEY,
        period TEXT,
        creation date TEXT)""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS tracker (
        date TEXT,
        streak INTEGER,
        habitName TEXT,
        FOREIGN KEY (habitName) REFERENCES habit(name))""")
    
    db.commit()


def add_habit(db, name, period, event_date= None):
    """Function for adding a habit with given parameters to a DB.
    :param db: forwarded DB connection
    :param name: the Name of the habit which is writen to the table habit
    :param period: the Periodicity of the habit which is writen to the table habit
    :param event_date: the creation date which is writen to the table habit, if empty than system date is used
    """
    cur = db.cursor()
    if not event_date:
        event_date = str(date.today())
    cur.execute("INSERT INTO habit VALUES (?, ?, ?)", (name, period, event_date))
    db.commit()

def delete_habit(db, name):
    """Function for deleting a habit with given name in a DB.
    All entries in both tables referencing this habit name are deleted.
    :param db: forwarded DB connection
    :param name: the Name of the habit which is deleted
    """
    cur = db.cursor()
    cur.execute("DELETE FROM habit WHERE name=?", (name,))
    db.commit()
    cur.execute("DELETE FROM tracker WHERE habitName=?", (name,))
    db.commit()

def delete_all_habits(db):
    """Function to delete all habits.
    After using this function you will receive a blank db.
    :param db: forwarded DB connection"""
    cur = db.cursor()
    cur.execute("DELETE FROM habit")
    db.commit()
    cur.execute("DELETE FROM tracker")
    db.commit()

def write_entry(db, name, event_date=None, streak=None):
    """Function to write an entry. An entry line is written in the table tracker in the db.
    :param db: forwarded DB connection
    :param name: the Name of the habit which is writen to the table tracker
    :param event_date: the checking date which is writen to the table tracker, if empty than system date is used
    :param streak: the handled streak of this habit which is written to the table tracker
    """
    cur = db.cursor()
    if not event_date:
        event_date = str(date.today())
    cur.execute("INSERT INTO tracker VALUES (?, ?, ?)", (event_date, streak, name))
    db.commit()

def get_habit_tracking_data(db, name):
    """Function to receive all entries in the table tracker of one habit.
    Return a list of all entries.
    :param db: forwarded DB connection
    :param name: the Name of the habit which is writen to the table tracker
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM tracker WHERE habitName=?", (name,))
    return cur.fetchall()

def get_habit_information_data(db, name):
    """Function to receive the entry of a habit in the table habit.
    Return a list of the habit.
    :param db: forwarded DB connection
    :param name: the Name of the habit which is writen to the table habit
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM habit WHERE name=?", (name,))
    return cur.fetchall()

def get_all_habits_from_db(db):
    """Function to receive all entries of the table habit.
    Return a list of all habits.
    :param db: forwarded DB connection
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM habit")
    return cur.fetchall()

def get_all_habits_with_same_periodicity(db, period):
    """Function to receive all entries of the table habit with the given periodicity.
    Return a list of all habits that have the same periodicity.
    :param db: forwarded DB connection
    :param period: the periodicity of the habits that should be returned
    """
    cur = db.cursor()
    cur.execute("SELECT * FROM habit WHERE period=?", (period,))
    return cur.fetchall()

def get_longest_streak_from_db_all(db):
    """Function to receive the overall longest streak of all recorded habits.
    Returns the streak with the greatest value as integer.
    :param db: forwarded DB connection
    """
    cur = db.cursor()
    cur.execute("SELECT date, MAX(streak), habitName FROM tracker")
    return cur.fetchone()

def get_longest_streak_from_db_habit(db, name):
    """Function to receive the overall longest streak of a given habit.
    Returns the streak with the greatest value as integer of the given habit.
    :param db: forwarded DB connection
    :param name: the name of the habit the longest streak should be returned
    """
    cur = db.cursor()
    cur.execute("SELECT date, MAX(streak), habitName FROM tracker WHERE habitName=?", (name,))
    return cur.fetchone()