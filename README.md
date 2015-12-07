Introduction
-----------------------------------------
saltweb项目使用salt-api来是实现saltstack的dashboard项目

开发环境
-----------------------------------------
Python: 2.7
Django: 1.8.5
MySQL: >= 5.1

Install dependency
-----------------------------------------
export WORKSPACE=/opt/saltweb
mkdir -p $WORKSPACE
cd $WORKSPACE && git clone https://github.com
yum install -y python-virtualenv python-virtinst
cd $WORKSPACE/saltweb
virtualenv ./env
./env/bin/pip install -r pip_requirements.txt -i http://pypi.douban.com/simple

Init database
-----------------------------------------
./env/bin/python manage.py makemigrations
./env/bin/python manage.py migrate

Start
-----------------------------------------
./env/bin/python manage.py runserver 0.0.0.0:80


初始化超级用户
-----------------------------------------
http://172.16.30.219/init_superuser/?username=root&password=123456
python-virtinst: Usge MAC = virtinst.util.randomMAC(type="qemu")
