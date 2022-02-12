from flask import Blueprint, abort, render_template

from app.auth.models import CartProduct
from app.products.models import Product, ProductCategory

products = Blueprint(
    'products',
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path='/home-static'
)


@products.route("/<product_category>", methods=['GET'])
def category(product_category):
    categories = ProductCategory.get_all_categories()
    if product_category not in [category.slug for category in categories]:
        abort(404)
    products = Product.query.all()
    products_for_category = [prod for prod in products
                             if prod.product_category.slug == product_category]
    return render_template('products/category.html',
                           categories=categories,
                           products=products_for_category,
                           product_category=product_category,
                           price=CartProduct.get_price_and_count()['price'],
                           count=CartProduct.get_price_and_count()['count'])


@products.route("/<product_category>/<product>", methods=['GET'])
def category_product(product_category, product):
    categories = ProductCategory.get_all_categories()
    if product_category not in [category.slug for category in categories]:
        abort(404)
    products = Product.query.filter(
        Product.product_category.has(slug=product_category)).all()
    if product not in [product.slug for product in products]:
        abort(404)
    product = Product.query.filter_by(slug=product).first()
    return render_template('products/product.html',
                           categories=categories,
                           product_category=product_category,
                           product=product,
                           price=CartProduct.get_price_and_count()['price'],
                           count=CartProduct.get_price_and_count()['count'])
