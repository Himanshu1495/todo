
import csv
import sys
import datetime
from termcolor import colored

#function to read the file
def file_read():
	fileOpen = open('data.csv') #open the file
	fileRead = csv.reader(fileOpen) #read the file
	dataFile = list(fileRead) #create list of items in file
	fileOpen.close()
	return dataFile

#function to write the file
def file_write(id,task,date,time):
	fileOpen = open('data.csv','a')
	fileWrite = csv.writer(fileOpen)
	fileWrite.writerow([id,task,date,time])
	fileOpen.close()
	return	

#function to check todays tasks
def tasks_today():
	data = file_read()
	tasks_today = [x for x in data if x[2]==str(datetime.date.today())] #filter todays task using date

	if len(tasks_today) > 0: 
		#if tasks are present, display them
		print colored("Today's tasks : ",'green')
		print colored("Task ID    |     Task    |       Date       	|       Time",'yellow')
		print colored("-------------------------------------------------------",'yellow')			
		for task in tasks_today:
			print colored("    " + task[0] + "      |    " + task[1] + "    |    " + task[2] + "    |    " + task[3],'cyan')
		return
	else:
		#if no tasks are present 
		print colored("There are no tasks today!",'green')		
		return
	return	

#function to add tasks
def tasks_add():
	print ""
	print colored("What's your TODO? ",'cyan'),
	add = raw_input()
	print colored("TODO's date? (MM-DD) ",'cyan'),
	date = raw_input()
	year = datetime.datetime.now()
	year = year.year #attach year to date
	date = str(year) + "-" + date
	print colored("TODO's time? (24-hr,HH:MM) ",'cyan'), 
	time = raw_input()
	data = file_read()
	if len(data) > 0:
		id = int(data[-1][0]) #get the latest ID
		id += 1	#increment ID
	else:
		id = 1 #if first task
	file_write(id,add,date,time)
	response = colored("'%s' has been created at %s %s having ID %s!"  %(add,date,time,id),'green')
	return response

#function to close the application
def close_todo():
	print colored("Bye Bye!",'cyan')
	sys.exit()

#main controller function of the application
def controller_function():
	print ""
	print colored("What TODO? ",'yellow'),
	task = raw_input() #ask for input
	if task == "add": #if add
		print tasks_add()
		controller_function() #recursion
	elif task == "exit":
		print close_todo()		
	else:
		print colored("TODO doesn't understand that! Please read instructions!",'red') #invalid input
 		controller_function()



#start of application
#User Greeting 
print colored("Welcome to TODO!",'cyan')
print " "
#check for todays tasks
tasks_today()
#start main controller function 
controller_function()		
