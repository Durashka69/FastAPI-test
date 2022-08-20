"""baseline

Revision ID: ca9299f5469c
Revises: 
Create Date: 2022-08-15 18:28:30.266913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca9299f5469c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('password', sa.String()),
        )


def downgrade() -> None:
    pass
