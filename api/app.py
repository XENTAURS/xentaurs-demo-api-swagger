from eve import Eve
from eve_swagger import swagger, add_documentation

app = Eve()
app.register_blueprint(swagger)
# required. See http://swagger.io/specification/#infoObject for details.

app.config['SWAGGER_INFO'] = {
    'title': 'Xentaurs - Example Infrastructure API',
    'version': '1.0',
    'description': 'Infrastructure Automation API',
    'contact': {
        'name': 'Xentaurs',
        'url': 'http://www.xentaurs.com'
    },
    'license': {
        'name': 'BSD',
    }
}

# optional. Will use flask.request.host if missing.
#app.config['SWAGGER_HOST'] = 'myhost.com'

if __name__ == '__main__':
    app.run()
