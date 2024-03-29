"""Add plenarprotokoll_text and drucksache_text tables

Revision ID: 2d2a36a65c30
Revises: c30fb340dbe4
Create Date: 2023-11-26 22:42:46.320056

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '2d2a36a65c30'
down_revision: Union[str, None] = 'c30fb340dbe4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    op.create_table(
        'drucksache_text',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('drucksache_id', sa.Integer(), nullable=False),
        sa.Column('text', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(
            ['drucksache_id'],
            ['dip.drucksache.id'],
        ),
        sa.PrimaryKeyConstraint('id'),
        schema='dip',
    )

    op.create_table(
        'plenarprotokoll_text',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('plenarprotokoll_id', sa.Integer(), nullable=False),
        sa.Column('text', sa.String(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['plenarprotokoll_id'], ['dip.plenarprotokoll.id']),
        sa.PrimaryKeyConstraint('id'),
        schema='dip',
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###

    op.drop_table('plenarprotokoll_text', schema='dip')
    op.drop_table('drucksache_text', schema='dip')
    # ### end Alembic commands ###
