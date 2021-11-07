"""add content to posts table

Revision ID: 146d1f59746e
Revises: 7d92610a4f0d
Create Date: 2021-11-07 17:50:56.128859

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '146d1f59746e'
down_revision = '7d92610a4f0d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
