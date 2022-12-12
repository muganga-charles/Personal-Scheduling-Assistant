from plyer import notification
from datetime import datetime

def Notification (date,time,activity):
    # convert the date from string to datetime format without time and return only the date 
    new_date = datetime.strptime(date, "%d/%m/%Y").date()
    #convert the time from string to datetime format and return only the time without date and seconds
    new_time = datetime.strptime(time, "%H:%M").time()
    
    # get the current date and time
    current_date = datetime.today().date()
    current_time = datetime.today().time().strftime("%H:%M")

    # convert the current time to datetime format   
    current_time = datetime.strptime(current_time, "%H:%M").time()
    if new_date == current_date and new_time == current_time:
        notification.notify(
            title = "Reminder",
            message = f"You have to {activity}  today",
           # app_icon = "icon.ico",
            timeout = 10
        )
    #the time is after the current time
    elif new_date == current_date and new_time > current_time:
        # convet the time to int to calculate the difference between the current time and the time of the activity
        new_time = int(new_time.strftime("%H%M"))
        current_time = int(current_time.strftime("%H%M"))
        # calculate the difference between the current time and the time of the activity
        difference = new_time - current_time
        # convert the difference to string to use it in the notification
        if difference < 60:
            hour = difference // 60
            minute = difference % 60
            difference = str(hour) + " hour and " + str(minute) + " minutes"

            notification.notify(
            title = "Reminder",
            message = f"You have to {activity} in {difference}",
            #app_icon = "icon.ico",
            timeout = 10    
        )
        
    #the time is before the current time
    elif new_date == current_date and new_time < current_time:
        # convet the time to int to calculate the difference between the current time and the time of the activity
        new_time = int(new_time.strftime("%H%M"))
        current_time = int(current_time.strftime("%H%M"))
        # calculate the difference between the current time and the time of the activity
        difference = current_time - new_time
        if difference < 60:
            hour = difference//60
            minute = difference%60
            difference = f"{hour} hour {minute} minutes"
    
        notification.notify(
            title = "Reminder",
            message = f"Your {activity} activity is overdue by {difference}",
            timeout = 10    
        )
    #the date is after the current date
    elif new_date > current_date:
        notification.notify(
            title = "Reminder",
            message = f"You have to {activity} on {date} at {time}",
            timeout = 10    
        )
    #the date is before the current date
    elif new_date < current_date:
        notification.notify(
            title = "Reminder",
            message = f"Your {activity} activity is overdue",
            timeout = 10    
        )

    
