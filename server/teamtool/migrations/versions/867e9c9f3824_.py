"""empty message

Revision ID: 867e9c9f3824
Revises: 
Create Date: 2020-12-28 07:31:53.317986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '867e9c9f3824'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('permission_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'permission_id')
    # ### end Alembic commands ###
