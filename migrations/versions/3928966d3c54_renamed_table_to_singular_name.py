"""Renamed table to singular name

Revision ID: 3928966d3c54
Revises: 4fd2ace3bb49
Create Date: 2020-07-13 13:00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3928966d3c54'
down_revision = '4fd2ace3bb49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('buildings', 'building')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('building', 'buildings')
    # ### end Alembic commands ###
