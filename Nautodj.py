#! /usr/bin/env python
from os import system as syst  
import sys 
from colorama import init
from termcolor import cprint 
from pyfiglet import figlet_format
from time import sleep as sl 
from sys import exit as ex 
#global variabls 
pwd = "pwd"
install_django_cmd = "pip install django "
runserver = "python manage.py runserver"
dj_version = "python -m django --version"
migrate = "python manage.py migrate"
mkmigration = "python manage.py makemigrations "
admin_user  = "python manage.py createsuperuser"
#cmd Functions 
def pwwd(): #1
	pwd1 = syst(pwd)
	return("you are in : " , pwd1)
def install_dj(): #2
	install = syst(install_django_cmd)
	return("Begin The Installation : " , install)
def django_ver(): #3
	ver = syst(dj_version) 
	return("Your Django version is : " , ver)
def start_project(project_name): #4
	cmmand0 = "django-admin startproject  "
	startpro = syst( str (cmmand0 + project_name))
	print("Creating The Project ...// ")
	return(startpro)
def start_application(app_name): #5
	cmmand1 = "python manage.py startapp  "
	app_start = syst( str( cmmand1 + app_name ))
	print("Creating The Application")
	return(app_start)
def apply_migrates():
	mig_apply = syst(migrate)     
	return(mig_apply)
	#pass
def run_server() : #6 
	server_run = syst(runserver)
	return(server_run)
def mkmig(app_to_mig) :
	makemig = syst(str(mkmigration + app_to_mig ))
	return ( makemig ) 
def super_user(): 
	make_user = syst( admin_user )
	return (make_user) 

def main() :
	def Intro():
		init(strip=not sys.stdout.isatty())
		cprint(figlet_format('nautodj', font='starwars')
			,'blue', attrs=['bold'])
	def Prop():
		print("\033[1;31 [+]Enter 1 To see in what directory u are :  \n")
		print("\033[1;31 [+]Enter 2 For Installing django :  \n")
		print("\033[1;31 [+]Enter 3 To see what django version  \n")
		print("\033[1;31 [+]Enter 4 For starting a new project  :  \n")
		print("\033[1;31 [+]Enter 5 For starting a new application :  \n")
		print("\033[1;31 [+]Enter 6 To apply migrates :  \n")
		print("\033[1;31 [+]Enter 7 To Makemigration To an app :  \n")
		print("\033[1;31 [+]Enter 8 To Make a super user  :  \n")
		print("\033[1;31 [+]Enter 9 To run the Server :  \n")
		print("\033[1;31 [+]Enter 10 To exit the script :  \n")
		choose = int(input("\033[1;34m] [+]Shoose One  : "))
		if choose == 1 : 
		   pwwd()
		   sl(6)
		   Prop()
		   
		if choose == 2 :
			install_dj()
			sl(6)
			Prop()

		if choose == 3 :
			django_ver()
			sl(6)
			Prop()

		if choose == 4 :
			projet_nom = str(input("Choose a name for Your Project : "))
			start_project(projet_nom)
			sl(6)
			Prop()

		if choose == 5 :
			print("please make sure to exit the script an to copy it into the prject file , then use it again to create apps and to run the server")
			print("Make sure to migrate  after creating to application ...")
			app_nom = str(input("choose Your Application Name : "))
			start_application(app_nom)
			sl(6)
			Prop()

		if choose == 7 :
			application_name = input("Please Enter The name of The application : ")
			mkmig(application_name)
			sl(6)
			Prop()
 
		if choose == 6 :
			apply_migrates()
			sl(6)
			Prop()
		if choose == 8 :
			super_user()
			sl(6)
			Prop()
		if choose == 9:
			run_server()
			sl(6)
			Prop()

		if choose == 10 :
			ex(0)
	Intro()
	Prop()
if __name__ == '__main__':
	main()