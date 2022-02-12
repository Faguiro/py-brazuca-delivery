"""empty message

Revision ID: 01364fac6cb0
Revises: 
Create Date: 2021-10-10 13:18:14.772726

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '01364fac6cb0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('price', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['product_category.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('product_category')
    # ### end Alembic commands ###