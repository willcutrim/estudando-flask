"""Add is_active column to users table

Revision ID: 5551a887a533
Revises: 
Create Date: 2024-12-31 17:09:39.831174

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5551a887a533'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Add the column with a default value
    with op.batch_alter_table('users') as batch_op:
        batch_op.add_column(sa.Column('is_active', sa.Boolean(), nullable=False, server_default=sa.sql.expression.true()))

    # Remove the server default
    with op.batch_alter_table('users') as batch_op:
        batch_op.alter_column('is_active', server_default=None)


def downgrade():
    with op.batch_alter_table('users') as batch_op:
        batch_op.drop_column('is_active')
