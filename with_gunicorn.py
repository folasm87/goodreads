# standard
from __future__ import absolute_import

# local
from myapp.service import create_app

app = create_app()
# Gunicorn looks for applicaiton by default, but app is the 'standard'
application = app
