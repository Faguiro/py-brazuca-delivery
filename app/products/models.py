from slugify import slugify

from app import db, ma


class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(500))
    composition = db.Column(db.String(500))
    weight = db.Column(db.Integer)
    price = db.Column(db.Numeric(5, 0))
    photo_url = db.Column(db.String(100))
    slug = db.Column(db.String(100), unique=True, nullable=True)

    category_id = db.Column(db.Integer, db.ForeignKey('product_category.id'))

    def __str__(self):
        return f"id={self.id}, name={self.name}, price={self.price}"

    def generate_slug(self):
        if self.name:
            self.slug = slugify(self.name)


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product


class ProductCategory(db.Model):
    __tablename__ = 'product_category'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100), unique=True, nullable=False)
    photo_url = db.Column(db.String(100), default='default_photo.jpeg')
    slug = db.Column(db.String(100), unique=True, nullable=False)

    products = db.relationship('Product',
                               foreign_keys='Product.category_id',
                               backref='product_category',
                               lazy='dynamic',
                               cascade='all, delete-orphan')

    @classmethod
    def get_all_categories(cls):
        return ProductCategory.query.all()

    def generate_slug(self):
        if self.category:
            self.slug = slugify(self.category)

    def __str__(self):
        return f"{self.category}"


class ProductCategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProductCategory
