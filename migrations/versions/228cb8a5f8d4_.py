# type: ignore
"""Building

Revision ID: 228cb8a5f8d4
Revises: b6cf0738c323
Create Date: 2020-03-03 20:37:33.753999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "228cb8a5f8d4"
down_revision = "b6cf0738c323"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "buildings",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("address", sa.String(length=255), nullable=False),
        sa.Column("client", sa.String(length=255), nullable=True),
        sa.Column("utility", sa.String(length=255), nullable=True),
        sa.Column("market", sa.String(length=255), nullable=True),
        sa.Column("sq_footage", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_buildings")),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("buildings")
    # ### end Alembic commands ###
