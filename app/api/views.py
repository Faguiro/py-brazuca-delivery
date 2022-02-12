from flask import Blueprint, jsonify, request
from flask_restx import Api, Resource, fields

from app import db
from app.products.models import Product, ProductCategory, ProductSchema

api_bp = Blueprint('api', __name__, url_prefix='/api')
api = Api(api_bp,
          version='1.0',
          title='Delivery_food API',
          description='API for the "Delivery_food" service',
          doc='/doc/')


productModel = api.model('Product', {
    'name': fields.String(default='Name'),
    'description': fields.String(default='Description'),
    'composition': fields.String(default='Composition'),
    'weight': fields.Integer(default=666),
    'price': fields.Integer(default=777),
    'category': fields.String(default='Пицца')
})

priceModel = api.model('Price', {
    'price': fields.Integer
})


@api.route('/product')
class Products(Resource):
    def get(self):
        """Get all products"""

        query = Product.query.all()
        product_schema = ProductSchema(many=True)
        result = product_schema.dump(query)
        return jsonify(result)

    @api.expect(productModel)
    def post(self):
        """Create a new product"""

        try:
            data = request.get_json()
            name = data.get('name')
            description = data.get('description')
            composition = data.get('composition')
            weight = data.get('weight')
            price = data.get('price')
            category = data.get('category')

            category_id = ProductCategory.query.filter_by(
                category=category).one().id
            new_product = Product(name=name, description=description,
                                  composition=composition, weight=weight,
                                  price=price, category_id=category_id)

            db.session.add(new_product)
            db.session.commit()
            query = Product.query.filter_by(name=name).one()
            product_schema = ProductSchema()
            result = product_schema.dump(query)
        except Exception:
            return api.abort(404, "name or category required OR product exist")
        else:
            return jsonify(result)


@api.route('/product/<id>')
class Products(Resource):
    def get(self, id):
        """Get product info"""

        query = Product.query.get_or_404(id)
        product_schema = ProductSchema()
        result = product_schema.dump(query)
        return jsonify(result)

    @api.expect(priceModel)
    def put(self, id):
        """Change price product"""

        try:
            query = Product.query.get_or_404(id)
            data = request.get_json()
            query.price = data.get('price')
            db.session.commit()
        except Exception:
            return api.abort(404)
        else:
            return "Product price updated"

    def delete(self, id):
        """Delete product"""

        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()

        return "Product removed"
