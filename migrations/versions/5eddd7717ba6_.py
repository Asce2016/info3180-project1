"""empty message

Revision ID: 5eddd7717ba6
Revises: 41469c2aab11
Create Date: 2017-03-13 22:41:40.629590

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5eddd7717ba6'
down_revision = '41469c2aab11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('user_name', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profile', 'user_name')
    # ### end Alembic commands ###
