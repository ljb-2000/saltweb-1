# encoding: utf8
#!/usr/bin/python

import MySQLdb
import json

class MySQL_API(object):
	def __init__(self,host,username,password,db):
		self.host = host
		self.username = username
		self.password = password
		self.db = db
		try:
			self.connect = MySQLdb.connect(self.host,self.username,self.password,self.db)
		except MySQLdb.Error,e:
			print "MySQLdb Error: %s" %e
		
	def query(self,sql):
		'''retrun all results'''
		try:
			cur = self.connect.cursor()
			cur.execute(sql)
			return cur.fetchall()
		except MySQLdb.ProgrammingError,e:
			print "exec sql failed: %s" %e
		except Exception,e:
			print "MySQLdb Error: %s" %e
		finally:
			cur.close()
			self.connect.close()	

	def query_dict(self,sql):
		'''返回结果为字典,可以根据键名来取数据'''
		try:
			cur = self.connect.cursor(MySQLdb.cursors.DictCursor)
			cur.execute(sql)
			return cur.fetchall()
                except MySQLdb.ProgrammingError,e:
                        print "exec sql failed: %s" %e
                except Exception,e:
                        print "MySQLdb Error: %s" %e
                finally:
                        cur.close()
                        self.connect.close()

	def update(self,sql):
		try:
			cur = self.connect.cursor()
			cur.execute(sql)
			self.connect.commit
			print "exec sql success!"
		except MySQLdb.ProgrammingError,e:
			print "exec sql faild: %s" %e
		except Exception,e:
			self.connect.rollback()
			print "MySQL Error: %s" %e
		finally:
			cur.close()
			self.connect.close()

#if __name__ == "__main__":
#	searchname = "lvs01"
#	sql = "select * from salt_returns WHERE `return` LIKE '%s' AND fun LIKE '%s' OR jid LIKE '%s' OR id LIKE '%s' ORDER BY alter_time;" %("%\"result\": false%","%"+searchname+"%","%"+searchname+"%","%"+searchname+"%")
#	mydb = MySQL_API('localhost','root','huangchao','salt')
#	rows = mydb.query_dict(sql)
#	print rows
