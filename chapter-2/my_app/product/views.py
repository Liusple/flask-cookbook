from my_app.product.models import PRODUCTS
from flask import render_template,Blueprint
from werkzeug import abort

product_blueprint = Blueprint('product', __name__)

@product_blueprint.context_processor
def some_processor():
	def full_name(product):
		return '{0} / {1}'.format(product['category'], product['name'])
	return {'full_name': full_name}

#@product_blueprint.template_filter('full_name') #this way can not work
def full_name_filter(product):
	return '{0} / {1}'.format(product['category'], product['name'])

@product_blueprint.route('/')
@product_blueprint.route('/home')
def home():
	return render_template('home.html', products=PRODUCTS)


@product_blueprint.route('/product/<key>')
def product(key):
	product = PRODUCTS[key]
	if not product:
		abort(404)
	return render_template('product.html', product=product)