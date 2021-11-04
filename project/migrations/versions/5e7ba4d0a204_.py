"""empty message

Revision ID: 5e7ba4d0a204
Revises: 4cc69a2ff27e
Create Date: 2021-11-04 18:22:47.010482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e7ba4d0a204'
down_revision = '4cc69a2ff27e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('author_id', sa.Integer(), nullable=False))
    op.add_column('articles', sa.Column('category_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'articles', 'category', ['category_id'], ['id'])
    op.create_foreign_key(None, 'articles', 'authors', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.drop_constraint(None, 'articles', type_='foreignkey')
    op.drop_column('articles', 'category_id')
    op.drop_column('articles', 'author_id')
    # ### end Alembic commands ###
