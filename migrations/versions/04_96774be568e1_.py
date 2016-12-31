"""Add waveform to sound infos

Revision ID: 96774be568e1
Revises: 052e645c59f4
Create Date: 2016-12-31 19:31:52.606598

"""

# revision identifiers, used by Alembic.
revision = '96774be568e1'
down_revision = '052e645c59f4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sound_info', sa.Column('waveform', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sound_info', 'waveform')
    ### end Alembic commands ###