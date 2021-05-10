"""Deleted utilities table

Revision ID: 67a48de52a60
Revises: 5f311ece51e5
Create Date: 2020-07-13 13:00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '67a48de52a60'
down_revision = '5f311ece51e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('utilities')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('utilities',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('authorization_uid', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('meter_uid', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('uid', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('utility', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('service_identifier', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('bill_end_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('bill_start_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('bill_total_cost', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('bill_total_kwh', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('bill_total_unit', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('bill_total_volume', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('peak_demand', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('peak_demand_cost', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('on_peak_demand', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('on_peak_cost', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('off_peak_demand', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('off_peak_cost', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('raw_url', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('building_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('billing_account', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['building_id'], ['buildings.id'], name='fk_utilities_building_id_buildings'),
    sa.PrimaryKeyConstraint('id', name='pk_utilities'),
    sa.UniqueConstraint('uid', name='uq_utilities_uid')
    )
    # ### end Alembic commands ###
