import os
from people import *
# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
MONGO_HOST = os.getenv('MONGO_HOST', 'localhost')
MONGO_PORT = 27017
MONGO_DBNAME = 'eveapitest'

RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

XML = False
PAGINATION = False
JSON_SORT_KEYS = True

X_DOMAINS = ['http://localhost',  # The domain where Swagger UI is running
             'http://editor.swagger.io',
             'http://petstore.swagger.io',
             'http://swagger.demo.xentaurs.com']
X_HEADERS = ['Content-Type', 'If-Match']  # Needed for the "Try it out" buttons
