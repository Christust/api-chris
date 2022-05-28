"""create items table

Revision ID: 1412f391a9f2
Revises: e9e8a0adfc62
Create Date: 2022-05-28 11:58:27.883382

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import relationship


# revision identifiers, used by Alembic.
revision = '1412f391a9f2'
down_revision = 'e9e8a0adfc62'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('title', sa.String(50), index=True),
        sa.Column('description', sa.String(50), index=True),
        sa.Column('owner_id', sa.Integer, sa.ForeignKey('users.id')),
    )
    pass

def downgrade():
    op.drop_table('items')
    pass
