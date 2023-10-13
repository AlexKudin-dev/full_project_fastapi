"""добавление еще данных

Revision ID: 8cd4c1812e81
Revises: 662fda2395d1
Create Date: 2023-10-12 18:06:55.291026

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8cd4c1812e81'
down_revision: Union[str, None] = '662fda2395d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Операция вставки данных
    op.execute("INSERT INTO users_test (id, username) VALUES (2, 'value2');")

def downgrade():
    # Операция отката
    op.execute("DELETE FROM users_test WHERE id = 2;")
