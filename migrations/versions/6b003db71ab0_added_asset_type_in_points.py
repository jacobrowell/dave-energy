# type: ignore
"""added_asset_type_in_points

Revision ID: 6b003db71ab0
Revises: 33b269191f57
Create Date: 2020-08-06 18:42:14.775741

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6b003db71ab0"
down_revision = "33b269191f57"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "points", sa.Column("asset_type", sa.String(length=255), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("points", "asset_type")
    # ### end Alembic commands ###
