"""init

Revision ID: e8e65c8776fc
Revises: 76a3dbda9d6f
Create Date: 2022-07-10 06:49:09.363349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8e65c8776fc'
down_revision = '76a3dbda9d6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'full_name')
    op.drop_column('user', 'image_url')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('image_url', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
