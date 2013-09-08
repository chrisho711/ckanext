Install instructions
=======
(1) clone extension source from github
cd /usr/lib/ckan/default/src/ckan
sudo git clone https://github.com/chrisho711/ckanext.git ckanext-tnhome

(2) install extension into python virtual enviroment
. /usr/lib/ckan/default/bin/activate
cd /usr/lib/ckan/default/src/ckan/ckanext-tnhome
sudo python setup.py develop 

(3) add extension name to ckan configuration file
 1. sudo vim /etc/ckan/default/development.ini
 2. ckan.plugins = stats text_preview recline_preview myhome

(4) start web server
paster serve /etc/ckan/default/development.ini
