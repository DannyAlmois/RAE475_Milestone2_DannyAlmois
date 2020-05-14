import sys
import telnetlib

tn_ip = "10.0.2.15"
tn_port = "23"
tn_username = "danny"
tn_password =  "115588"

searchfor = "Specificdata"

def telnet():
	try:
		tn = telnetlib.Telnet("10.0.2.15", "23", 15)
		tn.set_debuglevel(100)
		tn.read_until("login: ")
		tn.write(tn_username + "\n")
		tn.read_until("Password: ")
		tn.write(tn_password + "\n")
		tn.read_until(searchfor)
		print "Welcome to my telnet server!"
	except:
		print "Unable to connect to Telnet server: " + tn_ip
telnet()

