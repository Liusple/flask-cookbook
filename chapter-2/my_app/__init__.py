from my_app.product.views import product_blueprint
from my_app.product.views import full_name_filter
from flask import Flask
import ccy
from flask import request

app = Flask(__name__)
app.register_blueprint(product_blueprint)
app.add_template_filter(full_name_filter, 'product_name')

@app.template_filter('format_currency')
def format_currency_filter(amount):
	currency_code = ccy.countryccy(request.accept_languages.best[-2:])
	return '{0} {1}'.format(currency_code, amount)