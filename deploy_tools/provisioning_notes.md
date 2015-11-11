Provisioning a new site
=======================

##Required packages:

* nginx
* python 3
* git
* pip
* virtualenv

eg, on Ubuntu: sudo apt-get install nginx git python3 python3-pip sudo pip3 install virtualenv

## Nginx Virtual Host config

* set nginx.template.conf
* replace SITENAME with, eg, staging.domain.com

##Upstart Job
* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.domain.com

## Folder structure
Assume we have a user account at /home/username


