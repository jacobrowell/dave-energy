"""Removed client column

Revision ID: f2bd31992375
Revises: 57f29ad15286
Create Date: 2020-08-23 07:26:13.466554

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f2bd31992375'
down_revision = '57f29ad15286'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('buildings', 'client')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "buildings", sa.Column("client", sa.String(length=255), nullable=True,),
    )
    # ### end Alembic commands ###
