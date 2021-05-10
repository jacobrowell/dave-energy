"""Added unit column to bill_history

Revision ID: 642acdb59418
Revises: 2a561b7d5c75
Create Date: 2020-07-13 13:00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '642acdb59418'
down_revision = '2a561b7d5c75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bill_history', sa.Column('unit_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_bill_history_unit_id_unit'), 'bill_history', 'unit', ['unit_id'], ['id'])
    op.drop_column('bill_history', 'unit')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bill_history', sa.Column('unit', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_constraint(op.f('fk_bill_history_unit_id_unit'), 'bill_history', type_='foreignkey')
    op.drop_column('bill_history', 'unit_id')
    # ### end Alembic commands ###