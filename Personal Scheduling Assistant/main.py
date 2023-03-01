import PSA
storage = {}#dfjjkjf
from datetime import datetime
class Dates():
#constructor that helps us get the current date
    def __init__(self):
        self.current_date = datetime.today().date()

    def validateStartDate(self,start_time):# method
        self.new_dates = datetime.strptime(self.start_time, "%d/%m/%Y").date()
        return self.new_dates
    
    def validateDueDate(self,end_time):
        self.new_dates = datetime.strptime(self.end_time, "%d/%m/%Y").date()
        return self.new_dates

    def getCurrentDate(self):
        return self.current_date

class Events(Dates):
    def __init__(self):
        Dates.__init__(self)
       
    def AddingEvent(self):

        self.category = input("Enter the category of the event : ")
        self.name = input("Enter the name of the event : ")
        self.description = input("Give the description of the event : ")
        self.start_time = input("Enter the starting time : ")
        self.start_time = Dates.validateStartDate(self,self.start_time)
        self.end_time = input("Enter the due date : ")
        self.end_time =Dates.validateDueDate(self,self.end_time)
        
        if self.end_time == Dates.getCurrentDate(self):
            self.status = "FALSE"
            PSA.addCategory(self.category)
            PSA.addEvent(self.name, self.category, self.start_time, self.end_time,self.status)
        
        if self.end_time > Dates.getCurrentDate(self):
            self.status = "FALSE"
            PSA.addCategory(self.category)
            PSA.addEvent(self.name, self.category, self.start_time, self.end_time,self.status)

        if self.end_time < Dates.getCurrentDate(self):
            self.status = "TRUE"
            PSA.addCategory(self.category)
            PSA.addEvent(self.name, self.category, self.start_time, self.end_time,self.status)

#method that adds data after selecting the edit choice 
    def newEvent(self,category,name):
        self.Category = category
        self.Name = name
        self.name = input("Enter the new name of the event : ")
        self.description = input("Give the description of the event : ")
        self.start_time = input("Enter the starting time : ")
        self.start_time = Dates.validateStartDate(self,self.start_time)
        self.end_time = input("Enter the due date : ")
        self.end_time =Dates.validateDueDate(self,self.end_time)
        while self.end_time <  Dates.getCurrentDate(self):
            self.end_time = input("Enter a valid due date : ")
            self.end_time =Dates.validateDueDate(self,self.end_time)
        
        PSA.editEvent(self.Category,self.name,self.start_time, self.end_time,self.Name)

    def EditEvent(self):
        self.Category = input("Enter the category of the event: ")
        self.name =  input("Enter the name of the event : ")
    
        self.forward = PSA.validEvent(self.Category,self.name)
        if self.forward == True:
            self.newEvent(self.Category,self.name)
        elif self.forward == False:
            print("Event not found")

#method searches if the event you want to edit exist 
    def searchEvent(self,Category, name):
        if self.Category in storage:
            if self.name in storage[self.Category]:
                self.value = self.newEvent()
                storage[self.Category] =self.value

            else : 
                return f" {self.name} is not found "
#this method enables elimination of a certain category 
    def deleteCategory(self):
        self.choice = input("Do you want to delete a\n1. category\n2. event:")
        if self.choice == "1":
            self.Category = input("Enter the category of the event: ")
            PSA.deleteCategory(self.Category)
        elif self.choice == "2":
            self.Category = input("Enter the category of the event: ")
            self.name =  input("Enter the name of the event : ")
            if PSA.validEvent(self.Category,self.name):
                PSA.deleteEvent(self.Category,self.name)
            else:
                print("Event not found")
    def getCategories(self):
        print("Categories include : ")
        PSA.getCategories()
#this method marks an event as finished                
    def MarkAsFinished(self):
        self.Category = input("Enter the category of the event: ")
        self.name =  input("Enter the name of the event : ")
        if PSA.validEvent(self.Category,self.name):
            PSA.markAsFinished(self.name,self.Category)
        else:
            print("Event not found")

    def ViewEvents(self):
        print("Events include : ")
        PSA.PrintEvents()

    def Pending(self):
        PSA.upcommingEvents()

    def OverDue(self):
        PSA.overDueEvents()

    def sortDate(self):
        for i in range(len(self.storage1)):
            i = j
            while self.storage1[j-1] > self.storage1[j] and j > 0:
                self.storage1[j-1],self.storage1[j] = self.storage1[j],self.storage1[j-1]
                j-=1

def main():
    
    events = Events()
    while True:
        print("Welcome to the Personal Scheduling Assistant")
        print("______menu______\n")
        print(" 1. Add Event \n 2. Edit Event \n 3. Remove Category\Delete Event \n 4. Mark as Finished \n 5. View Categories \n 6. View All Events \n 7. Upcoming Events \n 8. Expired Events " )
        choice =  int(input("Please enter your choice : "))

        if choice == 1:
            events.AddingEvent()

        elif choice == 2:
            events.EditEvent()

        elif choice == 3:
            events.deleteCategory()
            
        elif choice == 4:
            events.MarkAsFinished()
       
        if choice == 5:
            events.getCategories()

        if choice == 6:
            events.ViewEvents()

        if choice == 7:
            events.Pending()

        if choice == 8:
            events.OverDue()

main()
