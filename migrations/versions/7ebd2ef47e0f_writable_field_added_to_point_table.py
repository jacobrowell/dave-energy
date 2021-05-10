# type: ignore
"""writable field added to point table

Revision ID: 7ebd2ef47e0f
Revises: ddc6894c5051
Create Date: 2020-07-02 13:14:31.126981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "7ebd2ef47e0f"
down_revision = "ddc6894c5051"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "points",
        sa.Column("writable", sa.Boolean(), nullable=False, server_default="0"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("points", "writable")
    # ### end Alembic commands ###
