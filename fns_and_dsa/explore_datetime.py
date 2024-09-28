# This script will demonstrate your ability to use the datetime module for handling dates and times in Python.
from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    f_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {f_current_date}")

def calculate_future_date():
    current_date = datetime.now()
    number_of_days = int(input("Enter the number of days to add to the current date:")) 
    future_date = current_date + timedelta(days=number_of_days)
    f_future_date = future_date.strftime("%Y-%m-%d")
    print (f"Future date: {f_future_date}")


display_current_datetime()
calculate_future_date()