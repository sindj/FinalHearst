import sqlite3
from flask import g
"""
def get_db():
    db = getattr(g, '/tmp/flaskr.db', None)
    if db is None:
        db = g._database = connect_to_database()
    return db

def getBuds(myname):
	db = getattr(g, '/tmp/flaskr.db', None)
	query='sele#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	#c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	ct id, friendname,data from friends where id=\''+myname+'\''+'order by id desc')
	cur = g.db.execute(query)
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)
drop table if exists friends;
create table friends (
  id text not null,
  friendname text not null,
   data text not null
);
    """
def addTable(myname):
	conn = sqlite3.connect("app/dbase/hearstdata.db")
	c = conn.cursor()
	#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	#c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	querytoExec="create table hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()

def addMappingTable(myname):
	conn = sqlite3.connect("app/dbase/hearstdata.db")
	c = conn.cursor()
	#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	#c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	querytoExec="create table usermap (uname text not null,role text not null, classname text, mappedteacher text);"
	c.execute(querytoExec)
	conn.commit()
	conn.close()


	#query='select id, friendname,data from friends where id=\''+myname+'\''+'order by id desc'
	#c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]

def addUserMap():
	conn = sqlite3.connect("app/dbase/hearstdata.db")
	c = conn.cursor()
	#objtoadd= [('RobinWollowski','Teacher','null','null'),('MikeAdams','Teacher','null','null'),('JimmyPage','Teacher','null','null'),('LarryKing','Teacher','null','null')]
	#objtoadd= [('Mark','Student','null','RobinWollowski'),('Viny','Student','null','RobinWollowski'), ('Anand','Student','null','JimmyPage'), ('Bruce','Student','null','RobinWollowski'), ('Andy','Student','null','RobinWollowski'), ('Bradley','Student','null','RobinWollowski'), ('Suhen','Student','null','JimmyPage'), ('Katey','Student','null','JimmyPage'), ('Ashwin','Student','null','RobinWollowski'), ('Carlos','Student','null','JimmyPage'), ('Walt','Student','null','RobinWollowski'), ('Noah','Student','null','RobinWollowski'), ('Adams','Student','null','RobinWollowski'), ('Jacques','Student','null','RobinWollowski'), ('Alex','Student','null','MikeAdams'), ('HurtingFoot','Student','null','MikeAdams'), ('Kiddy','Student','null','MikeAdams')]
	#entries=( teachername, studname, objid,'1','2')

	query='insert into usermap values (?,?,?,?)'
	c.executemany('insert into usermap values (?,?,?,?)',objtoadd)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	#querytoExec="create table hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	);"
	conn.commit()
	conn.close()

def addUserData():
	conn = sqlite3.connect("app/dbase/hearstdata.db")
	c = conn.cursor()
	#hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	)
	#objtoadd= [('RobinWollowski','Teacher','null','null'),('MikeAdams','Teacher','null','null'),('JimmyPage','Teacher','null','null'),('LarryKing','Teacher','null','null')]
	#objtoadd= [('Mark','Student','null','RobinWollowski'),('Viny','Student','null','RobinWollowski'), ('Anand','Student','null','JimmyPage'), ('Bruce','Student','null','RobinWollowski'), ('Andy','Student','null','RobinWollowski'), ('Bradley','Student','null','RobinWollowski'), ('Suhen','Student','null','JimmyPage'), ('Katey','Student','null','JimmyPage'), ('Ashwin','Student','null','RobinWollowski'), ('Carlos','Student','null','JimmyPage'), ('Walt','Student','null','RobinWollowski'), ('Noah','Student','null','RobinWollowski'), ('Adams','Student','null','RobinWollowski'), ('Jacques','Student','null','RobinWollowski'), ('Alex','Student','null','MikeAdams'), ('HurtingFoot','Student','null','MikeAdams'), ('Kiddy','Student','null','MikeAdams')]
	#entries=( teachername, studname, objid,'1','2')

	query='insert into usermap values (?,?,?,?)'
	c.executemany('insert into usermap values (?,?,?,?)',objtoadd)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	#querytoExec="create table hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	);"
	conn.commit()
	conn.close()
"""
def alterColumns():
	conn = sqlite3.connect("app/dbase/hearstdata.db")
	c = conn.cursor()
	#hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	)
	#objtoadd= [('RobinWollowski','Teacher','null','null'),('MikeAdams','Teacher','null','null'),('JimmyPage','Teacher','null','null'),('LarryKing','Teacher','null','null')]
	#objtoadd= [('Mark','Student','null','RobinWollowski'),('Viny','Student','null','RobinWollowski'), ('Anand','Student','null','JimmyPage'), ('Bruce','Student','null','RobinWollowski'), ('Andy','Student','null','RobinWollowski'), ('Bradley','Student','null','RobinWollowski'), ('Suhen','Student','null','JimmyPage'), ('Katey','Student','null','JimmyPage'), ('Ashwin','Student','null','RobinWollowski'), ('Carlos','Student','null','JimmyPage'), ('Walt','Student','null','RobinWollowski'), ('Noah','Student','null','RobinWollowski'), ('Adams','Student','null','RobinWollowski'), ('Jacques','Student','null','RobinWollowski'), ('Alex','Student','null','MikeAdams'), ('HurtingFoot','Student','null','MikeAdams'), ('Kiddy','Student','null','MikeAdams')]
	#entries=( teachername, studname, objid,'1','2')

	query="ALTER TABLE usermap RENAME COLUMN 'classname' to 'password';"
	c.execute(query)
	#results = [dict(myname=row[0], fname=row[1], srcname=row[2]) for row in c.fetchall()]
	#conn.close()
	#return results

	#querytoExec="create table hearstmain (teacher text not null,student text not null,obj1 text not null,obj2 text not null,obj3 text not null	);"
	conn.commit()
	conn.close()"""

if __name__ == '__main__':
	alterColumns()
	#addUserMap()
	#addMappingTable("not")
	"""d= getBuds('aditya')
	for e in d:
		print e['fname']"""