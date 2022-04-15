"""add user table

Revision ID: 0cee811c39de
Revises: 9934943fabf7
Create Date: 2022-04-12 09:03:14.259932

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.sqltypes import TIMESTAMP

# revision identifiers, used by Alembic.
revision = '0cee811c39de'
down_revision = '9934943fabf7'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email',sa.String(50), nullable=False),
    sa.Column('password',sa.String(50), nullable=False),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('user')
    pass
