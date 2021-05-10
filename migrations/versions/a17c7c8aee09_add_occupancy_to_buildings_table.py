"""Add occupancy to buildings table

Revision ID: a17c7c8aee09
Revises: b85fad7fe29c
Create Date: 2020-09-12 07:34:04.715543

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a17c7c8aee09'
down_revision = 'b85fad7fe29c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('buildings', sa.Column('occupancy', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('buildings', 'occupancy')
    # ### end Alembic commands ###