from flask import render_template,request,session
from flask import url_for
from app import app
from libs import apis
import dbHandler
import satchelHandler


def addToSatchel(objid):
	try:
		myname=session['username']
		myteachername=session['teachername']

		tup1=(myteachername,myname,objid)
		dbHandler.addToSatchel(tup1)
	except Exception as e:
		return False

def querySatchel():
	try:
		listall=[]
		listall=dbHandler.queryAll()
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