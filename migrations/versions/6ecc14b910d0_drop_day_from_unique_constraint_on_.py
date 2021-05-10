"""Drop day from unique constraint on billing_cycle

Revision ID: 6ecc14b910d0
Revises: 2101dab78797
Create Date: 2021-02-24 12:06:11.390565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6ecc14b910d0"
down_revision = "2101dab78797"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("uq_billing_cycle_building_id", "billing_cycle", type_="unique")
    op.create_unique_constraint(
        op.f("uq_billing_cycle_building_id"), "billing_cycle", ["building_id"]
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("uq_billing_cycle_building_id"), "billing_cycle", type_="unique"
    )
    op.create_unique_constraint(
        "uq_billing_cycle_building_id", "billing_cycle", ["building_id", "from_day"]
    )
    # ### end Alembic commands ###
