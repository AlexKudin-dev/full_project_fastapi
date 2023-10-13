"""добавление данных

Revision ID: 662fda2395d1
Revises: 8b836ddf29d3
Create Date: 2023-10-12 18:04:27.339718

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '662fda2395d1'
down_revision: Union[str, None] = '8b836ddf29d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Операция вставки данных
    op.execute("INSERT INTO users_test (id, username) VALUES (1, 'value1');")

def downgrade():
    # Операция отката
    op.execute("DELETE FROM users_test WHERE id = 1;")
