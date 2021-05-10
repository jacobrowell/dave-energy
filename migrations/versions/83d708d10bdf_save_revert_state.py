"""Save revert state

Revision ID: 83d708d10bdf
Revises: ade04caf2018
Create Date: 2021-01-09 16:40:08.351534

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '83d708d10bdf'
down_revision = 'ade04caf2018'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('point_dispatch_revert',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('point_id', sa.Integer(), nullable=False),
    sa.Column('dispatch_id', sa.Integer(), nullable=False),
    sa.Column('user_id_reverted', sa.Integer(), nullable=True),
    sa.Column('utc_reverted', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['dispatch_id'], ['dispatch.id'], name=op.f('fk_point_dispatch_revert_dispatch_id_dispatch')),
    sa.ForeignKeyConstraint(['point_id'], ['point.id'], name=op.f('fk_point_dispatch_revert_point_id_point')),
    sa.ForeignKeyConstraint(['user_id_reverted'], ['users.id'], name=op.f('fk_point_dispatch_revert_user_id_reverted_users')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_point_dispatch_revert')),
    sa.UniqueConstraint('point_id', 'dispatch_id', name=op.f('uq_point_dispatch_revert_point_id'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('point_dispatch_revert')
    # ### end Alembic commands ###
