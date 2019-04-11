import os
import sys
import site
import logging
logging.basicConfig(stream=sys.stderr)
# Add virtualenv site packages
site.addsitedir(os.path.join(os.path.dirname(__file__), 'venv/local/lib64/python2.7/site-packages'))

# Path of execution
sys.path.append('/var/www/html/desgrabador')

# Fired up virtualenv before include application
#activate_env = os.path.expanduser(os.path.join(os.path.dirname(__file__), 'venv/bin/activate_this.py'))
#execfile(activate_env, dict(__file__=activate_env))

from youtubesubs_app import app as application
