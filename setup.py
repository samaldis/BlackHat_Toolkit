#!/usr/bin/python
import sqlite3 as sql
import md5

def setup_dbs(user,passwd):
	#create the access database for web users
	userdb = sql.connect("dbs/users.db")
	ucur = userdb.cursor()
	ucur.execute("CREATE TABLE users(id INT PRIMARY KEY, name TEXT, password TEXT, admin INT)")
	ucur.execute("INSERT INTO users(id,name,password,admin) VALUES(?,?,?,?);", (1,user,passwd,1))
	userdb.commit()
	userdb.close()
	print "Created user database and added admin user"
	#create the hosts table
	hostdb = sql.connect("dbs/hosts.db")
	hcur = hostdb.cursor()
	hcur.execute("CREATE TABLE hosts(id INT PRIMARY KEY, ip TEXT, nmap TEXT)")
	hostdb.commit()
	hostdb.close()
	print "Creating session db"
	sessdb = sql.connect("www/dbs/sess.db")
	sesscur = sessdb.cursor()
	sesscur.execute("CREATE TABLE session(id INT PRIMARY KEY, sessionid TEXT, timestamp TEXT, hash TEXT)")
	sessdb.commit()
	sessdb.close()
	print "Created hosts database. all local databases created"
	print "Please use the latest github clone for the newest exploits and auxiliary dbs"
	  
	  
def setup():
	print "[x] Setting up the Blackhat Toolkit"
	username = raw_input("Please enter the username you want to use for\nthe web console: ")
	password = raw_input(username +"# please choose a password: ")
	m = md5.new()
	m.update(password)
	passwd = str(m.hexdigest())
	print "Hash created dropping into database setup"
	setup_dbs(username,passwd)
setup()
