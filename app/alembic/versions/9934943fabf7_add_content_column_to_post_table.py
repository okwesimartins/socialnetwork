"""add content column to post table

Revision ID: 9934943fabf7
Revises: 09ccc426ddd2
Create Date: 2022-04-12 08:29:46.085827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9934943fabf7'
down_revision = '09ccc426ddd2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(60), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
