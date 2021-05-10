"""Alter dnv_forecast table

Revision ID: bb40827b9fa5
Revises: a01724e06851
Create Date: 2021-03-25 23:28:26.179414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb40827b9fa5'
down_revision = 'a01724e06851'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'dnv_forecast', ['building_id', 'utc_computed', 'utc_forecast'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'dnv_forecast', type_='unique')
    # ### end Alembic commands ###