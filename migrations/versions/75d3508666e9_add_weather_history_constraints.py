"""Add weather history constraints

Revision ID: 75d3508666e9
Revises: de971390c478
Create Date: 2021-01-22 23:49:21.714517

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "75d3508666e9"
down_revision = "de971390c478"
branch_labels = None
depends_on = None


def upgrade():
    op.create_unique_constraint(
        op.f("uq_weather_history_weather_station_id"),
        "weather_history",
        ["weather_station_id", "utc_ts"],
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("uq_weather_history_weather_station_id"), "weather_history", type_="unique"
    )
    # ### end Alembic commands ###