Introduction
-----------------------------------------
saltweb项目使用salt-api来是实现saltstack的dashboard项目

配置文件
----------------------------------------
my.cnf: django mysql配置文件
saltweb.conf: 各种api中的账户密码

开发环境
-----------------------------------------
Python: 2.7
Django: 1.8.5
MySQL: >= 5.1

Install dependency
-----------------------------------------
export WORKSPACE=/opt/saltweb
mkdir -p $WORKSPACE
cd $WORKSPACE && git clone https://github.com/hctech/saltweb.git
yum install -y mysql-server mysql-devel
cd $WORKSPACE/saltweb
pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
chmod 777 saltweb/upload/

Init database
-----------------------------------------
mysql -e 'create database salt;'
mysql -e 'grant all on salt.* to salt@localhost identified by "salt";'
mysql -e 'grant all on salt.* to salt@"%" identified by "salt";'
mysql -e 'create database saltweb DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;'
mysql -e 'grant all on saltweb.* to salt@localhost identified by "salt";'
mysql -e 'grant all on saltweb.* to salt@"%" identified by "salt";'

USE `salt`;

--
-- Table structure for table `jids`
--

DROP TABLE IF EXISTS `jids`;
CREATE TABLE `jids` (
  `jid` varchar(255) NOT NULL,
  `load` mediumtext NOT NULL,
  UNIQUE KEY `jid` (`jid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Table structure for table `salt_returns`
--

DROP TABLE IF EXISTS `salt_returns`;
CREATE TABLE `salt_returns` (
  `fun` varchar(50) NOT NULL,
  `jid` varchar(255) NOT NULL,
  `return` mediumtext NOT NULL,
  `id` varchar(255) NOT NULL,
  `success` varchar(10) NOT NULL,
  `full_ret` mediumtext NOT NULL,
  `alter_time` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  KEY `id` (`id`),
  KEY `jid` (`jid`),
  KEY `fun` (`fun`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



cd $WORKSPACE/saltweb
python saltweb/manage.py makemigrations
python saltweb/manage.py migrate

Start
-----------------------------------------
cd $WORKSPACE/saltweb
python saltweb/manage.py runserver 0.0.0.0:80


初始化超级用户
-----------------------------------------
http://xx/init_superuser/?username=root&password=123456


Django+Apache
-----------------------------------------
yum install -y httpd mod_wsgi

vim /etc/httpd/conf.d/wsgi.conf 

==========wsgi.conf============
LoadModule wsgi_module modules/mod_wsgi.so


WSGIScriptAlias / "/opt/saltweb/saltweb/saltweb/saltweb/wsgi.py"
WSGIPythonPath /opt/saltweb/saltweb/saltweb

<VirtualHost *:80>
        ServerName www.saltweb.com
        <Directory "/opt/saltweb/saltweb/saltweb">
                <Files wsgi.py>
                        Order deny,allow
                        Allow from all
                </Files>
        </Directory>
        Alias /static/ /opt/saltweb/saltweb/saltweb/static/
        <Directory "/static/">
                Order allow,deny
                Options Indexes
                Allow from all
                IndexOptions FancyIndexing
        </Directory>
</VirtualHost>
============================

