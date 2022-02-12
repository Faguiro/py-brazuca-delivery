from app import create_app, db
from app.admin.views import (CartProductView, CartView, CategoryView,
                             ProductView, UsersView, admin, create_admin)
from app.api.views import api_bp
from app.auth.models import Cart, CartProduct, Users
from app.auth.views import auth
from app.home.views import home
from app.products.models import Product, ProductCategory
from app.products.views import products
from app.users.views import cartProduct
from config import DevelopmentConfig

app = create_app(DevelopmentConfig)
app.register_blueprint(home)
app.register_blueprint(admin)
app.register_blueprint(products)
app.register_blueprint(auth)
app.register_blueprint(cartProduct)
app.register_blueprint(api_bp)

admin = create_admin(app)
admin.add_view(ProductView(Product, db.session))
admin.add_view(CategoryView(ProductCategory, db.session))
admin.add_view(UsersView(Users, db.session))
admin.add_view(CartView(Cart, db.session))
admin.add_view(CartProductView(CartProduct, db.session))

if __name__ == '__main__':
    app.run()
