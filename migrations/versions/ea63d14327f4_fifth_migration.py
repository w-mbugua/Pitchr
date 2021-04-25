"""fifth migration

Revision ID: ea63d14327f4
Revises: a20c75e5b321
Create Date: 2021-04-24 18:16:32.090780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea63d14327f4'
down_revision = 'a20c75e5b321'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_pitch_date_posted', table_name='pitch')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_pitch_date_posted', 'pitch', ['date_posted'], unique=False)
    # ### end Alembic commands ###