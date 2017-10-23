#
# Project 4:  Brevet calculator
#
# Gnu make and bash are required. 
#


# Many recipes need to be run in the virtual environment, 
# so run them as $(INVENV) command
INVENV = . env/bin/activate ;

##
##  Virtual environment
##     
env:
	python3 -m venv env
	($(INVENV) pip install -r requirements.txt )


##
## Brevet Calculator
##

Create a replacement for the brevet controle time calculator at 
http://www.rusa.org/octime_acp.html in accordance with ACP rules described 
at http://www.rusa.org/octime_alg.html.
Controles are points where a rider must obtain proof of passage, and control[e] 
times are the minimum and maximum times by which the rider must arrive at the 
location.

## Installation
install: env credentials

credentials: brevets/credentials.ini

brevets/credentials.ini: 
	echo "You must manually create credentials.ini"


##
## How to use
##

Clone the repository and then CD into the proj4-brevets. 
Then in your terminal you type "make start" to install the enviornment
and then to see what port the computer is listening on.Then when you have the 
port type in your web browser, localhost:portnumber, which the port number 
will be 8000. 

Then there will be a calculator

##
## Preserve virtual environment for git repository
## to duplicate it on other targets
##
dist:	env
	$(INVENV) pip freeze >requirements.txt




