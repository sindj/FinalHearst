from flask import render_template,request,session
from flask import url_for
from app import app
from libs import apis
import dbHandler
import satchelHandler


def addToSatchel(objid):
	try:
		username=session['username']
		print "SH:", username, objid	
		tup1=(username,objid)
		dbHandler.addToSatchel(tup1)
	except Exception as e:
		return False

def querySatchel():
	try:
		listall=[]
		listall=dbHandler.queryAllByUser(session['username'])
		print len(listall), listall
		return listall
	except Exception as e:
		return e

def queryAllArtifacts(tribeid):
	try:
		listall=[]
		listall=dbHandler.queryAll()
		return listall
	except Exception as e:
		return e

def queryAllTeachers():
	try:
		listall=[]
		listall=dbHandler.queryTeachers()
		return listall
	except Exception as e:
		return e


def getClass(tup1):
	try: 
		listall={}
		listall=dbHandler.queryClassLogin(tup1)
		return listall
	except Exception as e:
		return e

def getStudentLogin(tup1):
	try: 
		listall={}
		listall=dbHandler.queryStudentLogin(tup1)
		return listall
	except Exception as e:
		return e
