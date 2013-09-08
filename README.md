Install instructions
=======
(1) clone extension source from github <br/>
cd /usr/lib/ckan/default/src/ckan <br/>
sudo git clone https://github.com/chrisho711/ckanext.git ckanext-tnhome <br/>

(2) install extension into python virtual enviroment<br/>
. /usr/lib/ckan/default/bin/activate<br/>
cd /usr/lib/ckan/default/src/ckan/ckanext-tnhome<br/>
sudo python setup.py develop <br/>

(3) add extension name to ckan configuration file<br/>
 1. sudo vim /etc/ckan/default/development.ini<br/>
 2. ckan.plugins = stats text_preview recline_preview myhome<br/>

(4) start web server<br/>
paster serve /etc/ckan/default/development.ini<br/>
