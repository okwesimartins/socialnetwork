"""add foreign-key to post table

Revision ID: 83589666db28
Revises: 0cee811c39de
Create Date: 2022-04-12 10:49:27.577901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83589666db28'
down_revision = '0cee811c39de'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="user", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
