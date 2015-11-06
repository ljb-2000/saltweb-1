# coding: utf8
#!/usr/bin/python

import datetime,os
from saltweb.mysql import *
import ConfigParser

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = ConfigParser.ConfigParser()
config.read(os.path.join(BASE_DIR, 'saltweb.conf'))

# db info
MYSQL_HOST = config.get('dashboard_db', 'host')
MYSQL_USERNAME = config.get('dashboard_db', 'username')
MYSQL_PASSWORD = config.get('dashboard_db', 'password')
MYSQL_DB = config.get('dashboard_db', 'db')


def list_week(num):
	'''列出指定num内的日期'''
	date_list = []
	for n in range(0,num):
		oneday = datetime.timedelta(days=n)
		last_day = datetime.date.today() - oneday
		format_last_day = last_day.strftime('%Y-%m-%d')
		date_list.append(format_last_day)
	date_list.reverse()
	return date_list
		

def list_week_count():
	'''列出一周内统计数'''
	sql = "select DATE_FORMAT(alter_time,'%Y-%c-%d'),count(*) from salt_returns where DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= date(alter_time) GROUP BY DATE_FORMAT(alter_time,'%Y-%c-%d');"
	mydb = MySQL_API(MYSQL_HOST,MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_DB)
	rows = mydb.query(sql)
	week_count = [ int(row[1]) for row in rows]
	return week_count
	

def fun_count():
	'''列出salt 使用函数的比例'''
	result_dict = {}
	sql = "SELECT fun,count(*) from salt_returns WHERE DATE_SUB(CURDATE(),INTERVAL 7 DAY) < alter_time GROUP BY fun;"
        mydb = MySQL_API(MYSQL_HOST,MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_DB)
        rows = mydb.query(sql)
	for row in rows:
		result_dict[row[0]] = int(row[1])
	return result_dict

def list_jobs():
	'''列出salt_returns表中的前20数据在index首页显示'''
	sql = "SELECT * from salt_returns ORDER BY alter_time DESC LIMIT 20;"
	mydb = MySQL_API(MYSQL_HOST,MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_DB)
	rows = mydb.query_dict(sql)
	return rows

def get_jids(jid):
	'''根据jid查询出详情'''
	sql = "SELECT full_ret from salt_returns WHERE jid=%s;" %jid
	mydb = MySQL_API(MYSQL_HOST,MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_DB)
	rows = mydb.query(sql)
	return rows

def list_job_all():
        sql = "SELECT * from salt_returns ORDER BY alter_time DESC;"
        mydb = MySQL_API(MYSQL_HOST,MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_DB)
        rows = mydb.query_dict(sql)
        return rows

def list_job_failed():
	sql = "select * from salt_returns WHERE `return` LIKE '%\"result\": false%' ORDER BY alter_time DESC;"
        mydb = MySQL_API(MYSQL_HOST,MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_DB)
        rows = mydb.query_dict(sql)
        return rows

def list_job_state():
        sql = "select *  from salt_returns WHERE fun='state.sls' ORDER BY alter_time DESC;"
        mydb = MySQL_API(MYSQL_HOST,MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_DB)
        rows = mydb.query_dict(sql)
        return rows

def list_job_highstate():
        sql = "select *  from salt_returns WHERE fun='state.highstate' ORDER BY alter_time DESC;"
        mydb = MySQL_API(MYSQL_HOST,MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_DB)
        rows = mydb.query_dict(sql)
        return rows

def list_job_search(searchname):
	'''用于job列表查询'''
	sql = "select * from salt_returns WHERE fun LIKE '%s' OR jid LIKE '%s' OR id LIKE '%s' ORDER BY alter_time DESC;" %("%"+searchname+"%","%"+searchname+"%","%"+searchname+"%")
        mydb = MySQL_API(MYSQL_HOST,MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_DB)
        rows = mydb.query_dict(sql)
        return rows

def list_job_failed_search(searchname):
	sql = "select * from salt_returns WHERE `return` LIKE '%s' AND (fun LIKE '%s' OR jid LIKE '%s' OR id LIKE '%s') ORDER BY alter_time DESC;" %("%\"result\": false%","%"+searchname+"%","%"+searchname+"%","%"+searchname+"%")
        mydb = MySQL_API(MYSQL_HOST,MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_DB)
        rows = mydb.query_dict(sql)
        return rows

def list_job_state_search(searchname):
        sql = "select * from salt_returns WHERE fun='state.sls' AND (jid LIKE '%s' OR id LIKE '%s') ORDER BY alter_time DESC;" %("%"+searchname+"%","%"+searchname+"%")
        mydb = MySQL_API(MYSQL_HOST,MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_DB)
        rows = mydb.query_dict(sql)
        return rows

def list_job_highstate_search(searchname):
        sql = "select * from salt_returns WHERE fun='state.highstate' AND (jid LIKE '%s' OR id LIKE '%s') ORDER BY alter_time DESC;" %("%"+searchname+"%","%"+searchname+"%")
        mydb = MySQL_API(MYSQL_HOST,MYSQL_USERNAME,MYSQL_PASSWORD,MYSQL_DB)
        rows = mydb.query_dict(sql)
        return rows
