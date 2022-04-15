"""create post table

Revision ID: 09ccc426ddd2
Revises: 
Create Date: 2022-04-12 05:07:55.559140

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09ccc426ddd2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id',sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(50), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
