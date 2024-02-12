# My Habit Tracking Application
# Make sure you followed all instructions written in the README.md
# Python 3.9.13 was used writing this porject
# lib db: is for communication with the databse
# lib habit: the Habit class is for handling all kind of situation regarding the habits
# lib analytics: the analytics library brings functions for analyzing certain information stored inside the database

# Running the application:
# If you followed all instructions in the README.md you should be able to run it

import questionary
from db import get_db, get_habit_information_data, delete_habit, delete_all_habits
from habit import Habit
from analytics import get_all_habits, get_all_habits_periodicity, get_longest_recorded_streak_habit, get_longest_recorded_streak_all, get_entries_of_a_habit
import os.path

# First comes the welcome text
# After this the user is able to select the desired database
print("Welcome to the habit tracking app!")
choice = questionary.select(
    "Do you want to load the main DB or another?", 
    choices=["Main-DB", "Sample-DB", "Enter your own DB"]
    ).ask()
if choice == "Main-DB":
    db = get_db("main.db")
    print("Main DB was succesfully loaded!")
    exit = False
elif choice == "Sample-DB":
     db = get_db("sample.db")
     print("Sample DB was succesfully loaded!")
     exit = False
elif choice == "Enter your own DB":
    filename = questionary.text("What is the name of your DB?").ask()
    if os.path.isfile("./" + filename + ".db") == True:
        print("Your DB was found!")
        db = get_db(filename + ".db")
        print("Your DB was succesfully loaded!")
        exit = False
    else:
        print("No file with the name: (" + filename + ") was found!")
        if questionary.confirm("Do you want to create a blank DB with that name? If not the application exits! Note that you have to respect the naming guidelines! Exceptions will be cought!").ask() == True:
            db = get_db(filename + ".db")
            # If a exception was cought then close the aplication
            if db == None:
                print("Exiting the aplication")
                exit = True
            else:
                print("Your DB was succesfully loaded!")
                exit = False
        else:
            print("Bye")
            exit = True

#During runtime the application will stay inide this infinite loop until the exit function is called       
while not exit:
    # First comes the selection of which function i going to be called
    choice = questionary.select(
        "What do you want to do?", 
        choices=["Create a new habit", "Check one habit", "Analyse your habits", "Delete habit", "Exit the application"]
        ).ask()
    # Code block for handling the creating habit function
    if choice == "Create a new habit":
            choice = questionary.select(
                "Do you want to use a predefined habit or do you want to create your own habit?", 
                choices=["Predefined", "Your own"]
                ).ask()
            # The creation of predefined habits is done here
            if choice == "Predefined":
                # All predefined habits are listed here
                predefined_habits = [("Brush your teeth daily"), ("Workout every week once"), ("Workout everyday"), ("Spend quality time with your partner one evening every month"), ("Go every year one time to the dentist")]
                name = questionary.select(
                    "Which predefined habit do you want to select?", 
                    predefined_habits
                    ).ask()
                all_habits = get_habit_information_data(db, name)
                # Handling a doubled habit
                if all_habits!= []:
                    print("Habit exists already! Please choose a different one!")
                # Handling the period of the predefined habit
                else:
                    if (name == predefined_habits[0]) or (name == predefined_habits[2]):
                        period = "daily"
                    elif (name == predefined_habits[1]):
                        period = "weekly"
                    elif (name == predefined_habits[3]):
                        period = "monthly"
                    elif (name == predefined_habits[4]):
                        period = "yearly"
                    habit = Habit(name, db, period, True)
                    print("You created succesfully your habit named: " + name +"!")
            # The creation of custom habits is done here
            elif choice == "Your own":
                name = questionary.text("What´s the name/task of your habit? Describe it detailed so you know what you want to track!").ask()
                all_habits = get_habit_information_data(db, name)
                # Handling a doubled habit
                if all_habits!= []:
                    print("Name is already given to an existing habit! Please choose another name!")
                # Creating the habit by creating a habit object and writing an entry to the database
                else:
                    period = questionary.select(
                    "Which periodicity should the habit have?",
                    # The poible period options 
                    choices=["daily", "weekly", "monthly", "yearly"]
                    ).ask()
                    habit = Habit(name, db, period, True)
                    print("You created succesfully your habit named: " + name +"!")
    # Code block for handling the check habit function
    elif choice == "Check one habit":
        all_habits = get_all_habits(db)
        #Creating a list of all habits that were created
        x = 0
        choices = []
        for i in all_habits:
            choices.append(i[0])
            x =+ 1
        #Check that there are habits
        if all_habits == []:
            print("There are no habits created yet! Please create first some habits!")
        else:
            habit_choice = questionary.select(
                "Which habit do you want to check?", 
                choices
                ).ask()
            # Get information about the habit
            habit = Habit(habit_choice, db,)
            last_entry = habit.get_last_entry()
            act_streak = habit.get_act_streak()
            period = habit.get_habit_period()
            #Handling the habit checking
            if last_entry == None:
                print("This is your first entry of this habit! Your actual streak is set to 1. The periodicity of the habit is (" + habit.get_habit_period() + "). It was created on (" +habit.get_creation_date() + ").")
            else:
                print("Your last entry in this habit was on (" + str(habit.get_last_entry()) + "). Your actual streak is (" + str(habit.get_act_streak()) + "). The periodicity of the habit is (" + habit.get_habit_period() + "). It was created on (" +habit.get_creation_date() + ").")
            result = habit.check_habit()
            # Result 1 is streak increasing, 0 is broke the habit and -1 is checking in the same period again
            if  result == 1:
                if period == "daily":
                    str_time = "day(s)"
                elif period == "weekly":
                    str_time = "week(s)"
                elif period == "monthly":
                    str_time = "month(s)"
                elif period == "yearly":
                    str_time = "year(s)"
                            
                print("You checked your habit in time! Your streak is incremented! Your actual streak ist now (" + str(habit.streak) + ") " + str_time + ".")
            elif result == 0:
                print("You broke your habit! You missed your streak! You checked your habit the last time on (" + str(last_entry) +")! Your actual streak is resetted to 1!")
            elif result == -1:
                print("You are too early! You already checked your habit this period on (" + str(last_entry) +")!")
    # Code block for analyzing the habits                      
    elif choice == "Analyse your habits":
        all_habits = get_all_habits(db)
        # Check that there are habits created
        if all_habits == []:
            print("There are no habits created yet! Please create first some habits!")
        else:
            # Choosing one option for analizing
            choice = questionary.select(
            "What do you want to analyze?", 
            choices=["All current habits.", "All current habits with the same periodicity.", "The longest recorded streak of all habits.", "The longest recorded streak of a given habit.", "Number of entries for a given habit."]
            ).ask()
            # Giving all habits to the user
            if choice == "All current habits.":
                habit_list = get_all_habits(db)
                for i in habit_list:
                    print("(" + i[0] + ") with the periodicity (" + i[1] + ") was created on (" + i[2] +").")
            # Giving the habits that has the same period choosen by the user
            elif choice == "All current habits with the same periodicity.":
                # Question for period
                period = questionary.select(
                "Which periodicity?", 
                choices=["daily", "weekly", "monthly", "yearly"]
                ).ask()
                habit_list = get_all_habits_periodicity(db, period)
                # Handling the situation if no habits with this periodicity were created
                if habit_list == []:
                    print("There are no habits with this periodicity! Choose another!")
                # Print the result
                else:
                    for i in habit_list:
                        print("(" + i[0] + ") with the periodicity (" + i[1] + ") was created on (" + i[2] +").")
            # Giving the longest streak of all habits that was recorded
            elif choice == "The longest recorded streak of all habits.":
                streak_list = get_longest_recorded_streak_all(db)
                # Handling the situation that there were no entries in every habit
                if streak_list[0] == None or streak_list[1] == None or streak_list[2] == None:
                    print("There were no entries for a habit yet!")
                # Returning the longest streak found in the databse
                else:
                    print("The longest streak of all habits was recorded on (" + streak_list[0] + ") for the habit (" + streak_list[2] + ") with the value of (" + str(streak_list[1]) +").")
            # Giving the longest streak for a single habit
            elif choice == "The longest recorded streak of a given habit.":
                all_habits = get_all_habits(db)
                x = 0
                choices = []
                # Collecting all available habits and let the user choose
                for i in all_habits:
                    choices.append(i[0])
                    x =+ 1
                habit_choice = questionary.select(
                "Which habit do you want to analyse?", 
                choices
                ).ask()
                streak_list = get_longest_recorded_streak_habit(db, habit_choice)
                # Handling the situation that were no entrie written inside the database
                if streak_list[0] == None or streak_list[1] == None or streak_list[2] == None:
                    print("There were no entries for this habit yet!")
                # Return the result
                else:
                    print("The longest streak of (" + streak_list[2] + ") was recorded on (" + streak_list[0] + ") with the value of (" + str(streak_list[1]) +").")
            # Giving the the number of entries for a specific habit choosed by the user    
            elif choice == "Number of entries for a given habit.":
                all_habits = get_all_habits(db)
                x = 0
                choices = []
                # Create a list of all available habits
                for i in all_habits:
                    choices.append(i[0])
                    x =+ 1
                habit_choice = questionary.select(
                "Which habit do you want to analyse?", 
                choices
                ).ask()
                entries = get_entries_of_a_habit(db, habit_choice)
                # Handling the situation if there were no entries for thi habit
                if entries == 0:
                    print("There were no entries for this habit yet!")
                # Returning the result
                else:
                    print("For the habit (" + habit_choice +") there were (" + str(entries) + ") entries made!")
    # Code block for deleting function
    elif choice == "Delete habit":
        all_habits = get_all_habits(db)
        x = 0
        choices = []
        # List all stored habits
        for i in all_habits:
            choices.append(i[0])
            x =+ 1
        # Adding the option to delete all habits
        choices.append("All")
        # Adding the option to exit the function without deleting something
        choices.append("Exit")
        habit_choice = questionary.select(
        "Which habit do you want to delete from DB?", 
        choices
        ).ask()
        # Handling the user decision
        if habit_choice == "Exit":
            pass
        elif habit_choice == "All":
            delete_all_habits(db)
            print("Deleted all habits from DB!")
        else:
            delete_habit(db, habit_choice)
            print(habit_choice + " succesfully deleted from DB!")
    # Exit the aplication
    elif choice == "Exit the application":
        print("Bye")
        exit = True