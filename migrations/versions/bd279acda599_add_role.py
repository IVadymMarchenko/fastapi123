"""add role

Revision ID: bd279acda599
Revises: 9efd16dd9502
Create Date: 2024-03-28 23:21:57.964505

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd279acda599'
down_revision: Union[str, None] = '9efd16dd9502'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE TYPE role as ENUM('admin','moderator','user')")
    op.add_column('users', sa.Column('role', sa.Enum('admin', 'moderator', 'user', name='role'), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')
    op.execute("DROP TYPE role")
    # ### end Alembic commands ###
