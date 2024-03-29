"""Add abstimmungen table

Revision ID: f8c93790f568
Revises: cd639eb06025
Create Date: 2023-12-06 22:53:46.026322

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'f8c93790f568'
down_revision: Union[str, None] = 'cd639eb06025'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'abstimmung',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('titel', sa.String(), nullable=False),
        sa.Column('abstract', sa.String(), nullable=True),
        sa.Column('sachgebiet', postgresql.ARRAY(sa.TEXT()), nullable=False),
        sa.Column('abstimmung_datum', sa.Date(), nullable=False),
        sa.Column('abstimmungsart', sa.String(), nullable=True),
        sa.Column('akzeptiert', sa.Boolean(), nullable=False),
        sa.Column('ja', sa.Integer(), nullable=False),
        sa.Column('nein', sa.Integer(), nullable=False),
        sa.Column('enthalten', sa.Integer(), nullable=False),
        sa.Column('nicht_abgegeben', sa.Integer(), nullable=False),
        sa.Column('ergebnis_anmerkung', sa.String(), nullable=True),
        sa.Column('aktualisiert', sa.DateTime(), nullable=True),
        sa.Column('initiative', postgresql.ARRAY(sa.TEXT()), nullable=True),
        sa.Column('beschlussfassung_id', sa.Integer(), nullable=False),
        sa.Column('dip_vorgangsposition_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('beschlussfassung_id'),
    )

    op.create_foreign_key(
        'fk_abstimmung_beschlussfassung_id',
        'abstimmung',
        'beschlussfassung',
        ['beschlussfassung_id'],
        ['id'],
        source_schema='public',
        referent_schema='dip',
        ondelete='CASCADE',
        onupdate='CASCADE',
    )

    op.create_foreign_key(
        'fk_abstimmung_dip_vorgangsposition_id',
        'abstimmung',
        'vorgangsposition',
        ['dip_vorgangsposition_id'],
        ['id'],
        source_schema='public',
        referent_schema='dip',
        ondelete='CASCADE',
        onupdate='CASCADE',
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('abstimmung')
    # ### end Alembic commands ###
