"""create top_topics table

Revision ID: 69e1b60db1cb
Revises: f8c93790f568
Create Date: 2023-12-08 07:48:27.611611

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '69e1b60db1cb'
down_revision: Union[str, None] = 'f8c93790f568'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('top_topics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ressort', sa.String(), nullable=False),
    sa.Column('word', sa.String(), nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.Column('month', sa.Integer(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('election_period', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('top_topics')
    # ### end Alembic commands ###
