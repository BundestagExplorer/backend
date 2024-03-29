"""update top_topics table

Revision ID: 4244e7fe7beb
Revises: e7026a158d4d
Create Date: 2024-01-25 21:52:37.694963

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '4244e7fe7beb'
down_revision: Union[str, None] = 'e7026a158d4d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('top_topics', 'id')
    op.add_column('top_topics', sa.Column('index', sa.INTEGER(), nullable=False))
    op.create_primary_key('PRIMARY', 'top_topics', ['month', 'year', 'election_period', 'ressort', 'index'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('top_topics', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_constraint('PRIMARY', 'top_topics', type_='primary')
    op.drop_column('top_topics', 'index')
    # ### end Alembic commands ###
