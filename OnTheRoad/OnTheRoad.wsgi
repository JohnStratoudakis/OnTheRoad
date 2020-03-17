#!/usr/bin/python3

#import os
#print("OS"*80)
#for item, value in os.environ.items():
#    print("{}:{}".format(item, value))


from dotenv import load_dotenv
load_dotenv('.env')

#API_KEY = os.getenv("GOOG_API_KEY")
import sys
sys.path.insert(0,"/var/www/html/johnstratoudakis.com/OnTheRoad/")

LINE_LENGTH = 80
print("-" * LINE_LENGTH)
print("OnTheRoad.wsgi")
from flaskapp import set_up_logging
set_up_logging(True)

from flaskapp import app as application
