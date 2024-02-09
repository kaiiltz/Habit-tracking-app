# My Habit Tracker App

In this "Read Me" you get a overview of the functions, how to set everything up and start the app. I used VS Code and Python 3.9.13 creating and running this project.


## What is it?

This is a application to track habits. The interaction with the application is solely through the command line. You only have to use your keyboard. If you have to choose between different options, you must use the arrow keys "up" and "down". Sometimes you have to input a name or something like that. In this case use the numbers and letters of your keyboard. Every input you have to enter it with the "enter"-key.  You have four main functions:

### 1. Creating a Habit
Creating a habit is the first thing you should do before starting to track a certain habit. In this function you have to choose if you use one out of five predefined habits, or using your own name/ task description for your habit and choose one of these periodicity options:
+ daily
+ weekly
+ monthly
+ yearly

The periodicity means after which time period you have to do and check your habit to built a streak. For example if you want to workout once every week, then you have to do this at least once every week and check your habit in the App.

It is forbidden to create a second habit with the same name, either for predefined and own habits. But no worries, the application detects this and give you a warning about this.

### 2. Checking a habit
After creating your first habit you can start with the tracking. Every time you accomplish something regarding your habits, then you have to check them off. Note that it won´t let you check something if there is no habit created.
There are 3 possible outcomes when you check your habit.

#### Checking your habit in time:
If you manage to check your habit in time, then you get rewarded with a increased streak. Every time you accomplished this your streak is added a 1 to it.

#### Checking your habit not in time:
If you miss it for at least one time and you check your habit the next time, then you get a message that you broke your habit and your streak is getting a reset to 1. But don´t worry! Nothing is lost for now, except your streak. You can keep on tracking and build your streak again.

#### Checking again in the same period:
You can check your habit every time you want to. For example if you want to go to the dentist at least one time every year, then your are not forbidden of doing it twice a year. This is nice for you, but the tracking app doesn´t interest this. You get a message that you are too early and that nothing will happen to your streak. Also, there will be no new entry in the database.

### 3. Analyzing your habits
The analysis functions give you a overview of your habits and whats their highest streaks. Note that it will not let you using a function if there are no habits created! You have a set of 5 options to analyze something:

#### All current habits:
This option returns a list of all habits that were stored to the current database. It gives you the name, periodicity and the creation date of each habit.

#### All current habits with same periodicity:
To use this function you first have to decide which periodicity is interesting for you. Choosing one will return you a list of all created habits with this parameter, provided there are any created.

#### The longest recorded streak of all habits:
This function gives you the highest streak count combined with the associated habit name and the date it was tracked. The application will notice when there is no single entry in the database!

#### The longest recorded streak of a given habit:
This function works quite similar to the prior one. Except you have to choose which of the created habits you want to see.

#### Number of entries for a given habit:
This function let´s you see the number of all entries that were made for a single habit. First you have to choose which one.

### 4. Deleting habits.
You have the option to delete some of your habits in the database. There is the option to delete a certain one or the whole database. Note that only the entries are deleted from the database. The tables remain, but empty if you delete everything.

### 5. Exiting the application
The last function let´s you exit the aplication. You can also simply close the IDE or whatever you are using. There is no difference to use the function. Note that closing it during running a function could let a entry for one habit be unfinished.


## Instalation

To access this application you don´t need much. First open the directory using your favorite IDE (I used VS Code to write it and to run it). You are open to just use a command line if you are familiar to it. Make sure to install pip on your system. Here is a link where you can read a bit about it:

https://pip.pypa.io/en/stable/installation/

To check if pip is correctly installed you can type this in the terminal and it should print something with information about your pip version and how to use it:
```shell
pip
```

Is everything okay than we can continue and install all required librarys. They are all written down in the "requirements.txt". It is:
+ pytest (for testing obviously)
+ questionary (for the CLI implementation)


To set eveything up on your system you just have to run this command:

```shell
pip install -r requirements.txt
```
It should install everything from the text file. If you are encountering issues, try installing them one by one with this command:

```shell
pip install "here you have to input the name of the library"
```
## Usage

After the installation were a re ready to give it a try. Depending on how experienced you are, you can just run the main.py file. There are several ways to run it. If you are using VS Code open the main.py file in the editor and just hit the "F5"-key. It´s the same as if you go over "Run"-> "Start debugging". If you work with the terminal just type the followed to run it:
```shell
python main.py
```
Before entering the main menu, you have to choose which database you want to access. More details in the database section.

## Tests

For testing my project, I wrote a test suite. It´s called test_project.py and is using the pytest functionality. If you want to run it use one of the following suggestions and type it in the terminal:
```shell
pytest
```
or
```
python -m pytest
```
There should be 3 passing tests. They are all to ensure correct data reading/writing in cooperation with the database and the habit class. Feel free to check it or add something if you want to extend some functionalities. 

More information about pytest: https://docs.pytest.org/en/8.0.x/

## Database

The whole data that is used during the habit tracking is always stored in SQLite database file. I am using the SQLite3 Python library to handling the reading and writing of the data. All functions that are connected to the database are inside the db.py file. In the main program I am using the habit class as a object which uses the db functions. 

For storing all habit data, I am creating two tables with the following columns inside the database:
+ table habit: habit name, periodicity, creation date
+ table tracker: habit name, entry name, streak

The table habit is used to store all habits that are created by the user. So every time you create one habit there is a new entry made inside the database. To track all your entries and streaks of each habit, I use the table tracker to store every entry.

In the beginning of the program you are asked which database you want to use. There a three option that I will explain now. The frst one should be the normal use case. The Main-DB is the option if you just want to start to track all your habits. In the first run the database should be empty and all data is stored inside a file called main.db. If you delete the data using the function or delete the file inside the directory then all stored data is gone. No worries if you deleted the file. If you choose the option Main-DB then the application is creating a new file if not existing.
The Sample-DB option is for validating the functionality of the habit tracker app. I created a program called create_sample_db.py for creating a sample.db file with stored date. Note that if the sample.db is existing in the directory the running program will raise a exception. Delete it if you want to create a new one. Feel free to adjust the stored data. And check it out in the app.
The last option is for user who created their own database or who wants a database with custom name. Note that you have to input the name correctly. If there is no file with given name, the program will aks you if you want to create it.
Either way you choose, with every database you load, all functionalities of the app are the same, it only differs in the data that is stored in the database.

## Adding functions

If you want to add something, for example new predefined habits or new options in the main menu then you have to consider a few things. 
Adding a new option or feature in the main menu is not that hard. In the emost cases I used the .select() command from questionary. The most functions are stated as a simple string inside the question and then simply selected in an if-elif-structure.
If you want to add new functions to the habit you have to add it inside the habit class. All the database communication is done through the functions implemented in the db.py library. The habit creating/ checking habits are all done through the habit class. All analysis functions are functions in an own library in analitics.py. 

