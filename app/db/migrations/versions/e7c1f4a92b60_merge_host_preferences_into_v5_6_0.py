"""merge admin host preferences with the v5.6.0 migration chain

Existing databases are stamped d15b7a6c9e21, so that revision must stay a parent; re-parenting it
onto the v5.6.0 head would make Alembic treat the v5.6.0 migrations as already applied.

Revision ID: e7c1f4a92b60
Revises: d15b7a6c9e21, 1a2b3c4d5e6f
"""

revision = "e7c1f4a92b60"
down_revision = ("d15b7a6c9e21", "1a2b3c4d5e6f")
branch_labels = None
depends_on = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
