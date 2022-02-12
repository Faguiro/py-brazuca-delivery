from flask import Blueprint, render_template

from app.auth.models import CartProduct
from app.products.models import ProductCategory

cartProduct = Blueprint(
    'cartProducts',
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path='/home-static'
)


@cartProduct.route("/cart", methods=['GET'])
def cart():
    return render_template('users/cart.html',
                           categories=ProductCategory.get_all_categories(),
                           price=CartProduct.get_price_and_count()['price'],
                           count=CartProduct.get_price_and_count()['count'],
                           products_in_cart=CartProduct.products_in_cart())
