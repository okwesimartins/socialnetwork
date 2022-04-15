"""add phonenumber

Revision ID: fd1297835045
Revises: 3eef6da45cab
Create Date: 2022-04-15 01:59:40.482539

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fd1297835045'
down_revision = '3eef6da45cab'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('phone_number', sa.String(50), nullable=True))
    # ### commands auto generated by Alembic - please adjust! ###
  
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_column('user', 'phone_number')
    # ### end Alembic commands ###
