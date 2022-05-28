"""create users table

Revision ID: e9e8a0adfc62
Revises: 
Create Date: 2022-05-28 01:58:27.724919

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import relationship


# revision identifiers, used by Alembic.
revision = 'e9e8a0adfc62'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('email', sa.String(50), nullable=False, unique=True, index=True),
        sa.Column('hashed_password', sa.String),
        sa.Column('is_active', sa.Boolean, default=True),
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
