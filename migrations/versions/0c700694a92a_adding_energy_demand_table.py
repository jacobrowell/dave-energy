# type: ignore
"""Adding energy demand table

Revision ID: 0c700694a92a
Revises: 09b52dc34c95
Create Date: 2020-09-23 20:13:35.557425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "0c700694a92a"
down_revision = "09b52dc34c95"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "energy_demand",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("year", sa.Integer(), nullable=False),
        sa.Column("month", sa.Integer(), nullable=False),
        sa.Column("value", sa.Float(), nullable=False),
        sa.Column("building_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["building_id"],
            ["buildings.id"],
            name=op.f("fk_energy_demand_building_id_buildings"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_energy_demand")),
        sa.UniqueConstraint(
            "building_id", "year", "month", name=op.f("uq_energy_demand_building_id")
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("energy_demand")
    # ### end Alembic commands ###
