# This README file is all about python
Python:

# Needs / overview:

Python interpreter -> makes the system understand what we want it to do. I.e if you have python script you need a python interpreter to read and run that code.
Virtual Environments -> This allaws you to install everything you need to install python specific code. This means you don't have to install those specific packages system wide.
Package Management with pip -> pip is used to install and remove python packages for python to help make things run.


# Using Python Interpreter:

# How to install the Python interpreter
Linux = yum install Python
Fidora = dnf install python
Debian = apt-get install python


Check the version by using python --version

There are many version of python, currently version 3.8 is the default. Some python code needs to be ran by a specific version. I.e if you have python 2 code and you try running it using python 3 it will likely throw errors becasue they aren't compatible. 

# Using python interactive Console

just run python this will take you to the interactive console
to clear the screen use ctrl + l
to exit the console use exit()

# Saving and Running Python Code

create a python file with the .py extention.
you can use touch to create a file and vim to edit the file.
If you have some fancy development platform like eclipse or intelliJ then that works a bit differently.



# Virtual Environments and Package Management with pip:
We want this so we can write code that isn't tied to the existing environment. This allows you to write your own code and run tests that wont affect the system wide environment.

# Create a Virtual Environment

First install python.
Then install python-virtualenv
i.e sudo yum install python3-virtualenv

run python -m venv <Path/virtual_environment_name>

# Manage a Virtual Environment

to activate the environment cd to its directory then run source  <Path/virtual_environment_name>/bin/activate
to deactivate it you would run source  <Path/virtual_environment_name>/bin/deactivate

# Manage Packages with pip
To install pip
yum install pip or yum install pip3 

BEFORE YOU INSTALL PIP make sure you know your python version. MAKE SURE YOUR PIP AND PYTHON VERSON ARE THE SAME. Otherwise pip will install for a different python version.

pip list will show you a list of packages
pip search <name> lets you search for a specific package and give you details of the package.


# Python Data Types (used to store different types of data) :

Numbers ( If you put a number between '' or "" then that makes it a string )
Strings (You can use '' or "" )
Lists ( These are mutable ( means the values can change ) ) These are like arrays These are set using []
Tuples ( These are like lists except they aren't mutable ) These are set using ()
Dictionaries (Function based off of key values. Basically object arrays) These are similar to lists. These are set using {}

# Python Operators (used to perform operations on variables) :

Addition (+)
Subtraction (-)
Multiplication (*)
Modulus (%) (The remander after a division) I.e 5 % 2 = 5 
Exponent (**)
Division (/) (Normal divison which can spit out an int, float, or long) i.e 5 / 2 = 2.5
Floor Division (//) (is a normal division operation except that it returns the largest possible integer.) i.e 5 // 2 = 2

Equal to (==)
Not equal to (!=) or (<>) (<> is no longer in use after python 3 or above but it can be used in python 2 or below)
Greater than (>)
Greater than or equal to (>=)
Less than (<)
Less than or equal to (<=)


# Conditionals

if <condition>:
elif <condition:
else:

# Loops

for <condition>:
while <condition>:
