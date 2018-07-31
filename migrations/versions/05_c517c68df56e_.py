"""Add markers for sound generation of infos

Revision ID: c517c68df56e
Revises: 96774be568e1
Create Date: 2016-12-31 19:52:36.320149

"""

# revision identifiers, used by Alembic.
revision = 'c517c68df56e'
down_revision = '96774be568e1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sound_info', sa.Column('done_basic', sa.Boolean(), nullable=True))
    op.add_column('sound_info', sa.Column('done_waveform', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sound_info', 'done_waveform')
    op.drop_column('sound_info', 'done_basic')
    ### end Alembic commands ###