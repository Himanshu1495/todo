
import csv
import datetime
from termcolor import colored

#function to check todays tasks
def tasks_today():
	fileOpen = open('data.csv') #open the file
	fileRead = csv.reader(fileOpen) #read the file
	dataFile = list(fileRead) #create list of items in file
	tasks_today = [x for x in dataFile if x[2]==str(datetime.date.today())] #filter todays task using date

	if len(tasks_today) > 0: 
		#if tasks are present, display them
		print colored("Today's tasks : ",'green')
		print colored("Task ID    |     Task    |       Date",'yellow')
		print colored("-----------------------------------------",'yellow')			
		for task in tasks_today:
			print colored("    " + task[0] + "      |    " + task[1] + "    |    " + task[2],'cyan')
		return
	else:
		#if no tasks are present 
		print colored("There are no tasks today!",'green')		
		return
	return	
#User Greeting 
print colored("Welcome to TODO!",'cyan')
print " "

tasks_today()
#def on_start():
	
	
#on_start()

		
