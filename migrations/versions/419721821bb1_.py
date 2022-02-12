"""empty message

Revision ID: 419721821bb1
Revises: a76cd4740049
Create Date: 2021-10-15 15:28:23.891623

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '419721821bb1'
down_revision = 'a76cd4740049'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category', sa.String(length=100), nullable=False),
    sa.Column('photo_url', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('category')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('composition', sa.String(length=500), nullable=True),
    sa.Column('price', sa.Numeric(precision=5, scale=0), nullable=True),
    sa.Column('photo_url', sa.String(length=100), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
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