import sys 
import logging 
import sqlite3

logging.basicConfig(stream=sys.stderr) 
sys.path.insert(0,"/var/www/flaskApp/") 

from __init__ import app as application 

application.secret_key = 'alan047'
#renomear
