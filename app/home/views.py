from flask import Blueprint, render_template

from app.auth.models import CartProduct
from app.products.models import ProductCategory

home = Blueprint(
    'home',
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path='/home-static'
)


@home.route("/")
def index():
    return render_template('home/home.html',
                           categories=ProductCategory.get_all_categories(),
                           price=CartProduct.get_price_and_count()['price'],
                           count=CartProduct.get_price_and_count()['count'])
