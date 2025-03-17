"""init

Revision ID: 5de914e66a8e
Revises:
Create Date: 2025-03-17 06:30:10.808919

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = "5de914e66a8e"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "imports",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.Column("month", sa.Integer(), nullable=True),
        sa.Column("origin_name", sa.String(), nullable=True),
        sa.Column("origin_type_name", sa.String(), nullable=True),
        sa.Column("destination_name", sa.String(), nullable=True),
        sa.Column("destination_type_name", sa.String(), nullable=True),
        sa.Column("grade_name", sa.String(), nullable=True),
        sa.Column("quantity", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_imports_id"), "imports", ["id"], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f("ix_imports_id"), table_name="imports")
    op.drop_table("imports")
