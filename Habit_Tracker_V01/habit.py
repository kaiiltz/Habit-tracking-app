from datetime import date, datetime, timedelta
from db import add_habit, write_entry, get_habit_information_data, get_habit_tracking_data

class Habit:
    """Habit Class to create habbits for tracking.
    
    :param name: the habit name
    :param period: the timeperiods where the habit has to be checked
    :param streak: the loaded streak
    :param db: the forwarded db connection
    :param creation date: used to write a custom creation date, defoult is system date
    :param create: used to create the habit in the db, if false then the object is created without writing in the db
    """

    def __init__(self, name: str, db, period: str = None, create: bool = False, creation_date: str = None):
        self.name = name
        self.period = period
        self.streak = 0
        self.db = db
        self.creation_date = creation_date
        if create == True:
            add_habit(self.db, self.name,self.period, self.creation_date)
    
    def __str__(self):
        return f"{self.name}: Actual streak = {self.get_act_streak()}"
    
    def check_habit(self, timestamp: str = None):
        """Function to check a habit in the db.
        param timestamp: used to write a custom date instead of the system date
        """
        #Creating the timestamp from the system date
        if timestamp == None:
            timestamp = str(date.today())
        #Handling the streak with the function handle_streak()
        handle = self.handle_streak(datetime.strptime(timestamp, '%Y-%m-%d').date()) 
        #If the result of the handle_streak() is streak incremented (1) or streak lost (0) than an entry is written to the db,
        #if result is that there is already an entry in this period (-1) no entry is written
        if handle != -1:
            write_entry(self.db, self.name,timestamp, self.streak)
            return handle
        else:
            return handle

    def get_last_entry(self): 
        """Function to get the date of the last entry of given habit.
        """
        #Get entries for this habit
        data = get_habit_tracking_data(self.db, self.name)
        #If no data was written return None, otherwise return the date of the last entry
        if not data:
            return None
        else:
            last_entry = data[len(data)-1]
            return datetime.strptime(last_entry[0], '%Y-%m-%d').date()
    
    def get_act_streak(self):
        """Function to get the actual streak of this habit.
        """
        #Get entries for this habit
        data = get_habit_tracking_data(self.db, self.name)
        #If no data was written return 0, otherwise return the streak of the last entry
        if not data:
            return 0
        else:
            last_entry = data[len(data)-1]
            return int(last_entry[1])

    def get_habit_period(self):
        """Function to get the periodicity of this habit.
        """
        #Get entries for this habit
        data = get_habit_information_data(self.db, self.name)
        #If no data was written return 0, otherwise return the periodicity
        if not data:
            return None
        else:
            last_entry = data[len(data)-1]
            return last_entry[1]
    
    def get_creation_date(self):
        """Function to get the cration date of this habit.
        """
        #Return the creation date of the habit
        data = get_habit_information_data(self.db, self.name)
        return data[0][2]

    def get_entries(self):
        """Function to get the entries of this habit.
        """
        #Return the amount of entries were made
        return len(get_habit_tracking_data(self.db, self.name))

    def handle_streak(self, timestamp):
        """Function to handle the streak of this habit. This function is calle during the function check_habit().
        Return 1 for increment, 0 for streak lost, -1 for already checked in this period.
        :param timestamp: this parameter is used to use this function with a custom date instead of system date
        """
        #get the last entry and the periodicity for the check
        last_entry = self.get_last_entry()
        period = self.get_habit_period()
        #Check if there are entries made in the DB for this habit
        if last_entry != None:
            #Each periodicity has it´s own checking mechanism, they are working the same, but the timedelta is different
            if period == "daily":
                #If the check is not made in time, then reset streak  and return streak lost(0)
                if ((timestamp - last_entry) > timedelta(days=1)):
                    self.streak = 1
                    return(0)
                #If the check is made in time, then increment streak  and return streak incremented(1)
                elif ((timestamp - last_entry) == timedelta(days=1)):
                    self.streak = self.get_act_streak()+1
                    return(1)
                #If the there is already a check in this period, then do nothing and return already checked(-1)
                else:
                    return(-1)
            
            elif period == "weekly":
                if ((timestamp - last_entry) > timedelta(weeks=1)):
                    self.streak = 1
                    return(0)
                elif ((timestamp - last_entry) == timedelta(weeks=1)):
                    self.streak = self.get_act_streak()+1
                    return(1)
                else:
                    return(-1)
                
            elif period == "monthly":
                timestamp = timestamp.replace(day=1)
                last_entry = last_entry.replace(day=1)

                if ((timestamp - last_entry) > timedelta(weeks=8)):
                    self.streak = 1
                    return(0)
                elif ((timestamp - last_entry) >= timedelta(weeks=4)):
                    self.streak = self.get_act_streak()+1
                    return(1)
                else:
                    return(-1)
                
            elif period == "yearly":
                timestamp = timestamp.replace(day=1)
                timestamp = timestamp.replace(month=1)
                last_entry = last_entry.replace(day=1)
                last_entry = last_entry.replace(month=1)

                if ((timestamp - last_entry) > timedelta(weeks=104)):
                    self.streak = 1
                    return(0)
                elif ((timestamp - last_entry) >= timedelta(weeks=52)):
                    self.streak = self.get_act_streak()+1
                    return(1)
                else:
                    return(-1)
        #If there were no entries set the streak to 1 and return streak incremented(1)
        else:
            self.streak = 1
            return(1)

