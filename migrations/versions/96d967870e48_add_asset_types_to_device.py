# type: ignore
"""add asset_types to device

Revision ID: 96d967870e48
Revises: e3d217e57ce6
Create Date: 2020-07-16 14:38:32.324823

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "96d967870e48"
down_revision = "e3d217e57ce6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    asset_type = postgresql.ENUM(
        "HVAC",
        "METER",
        "LIGHT",
        "SOLAR",
        "BATTERY",
        "ELEVATOR",
        name="assettype",
        create_type=False,
    )
    asset_type.create(op.get_bind())
    op.add_column("devices", sa.Column("asset_type", asset_type, nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("devices", "asset_type")
    postgresql.ENUM(name="assettype").drop(op.get_bind(), checkfirst=True)
    # ### end Alembic commands ###
