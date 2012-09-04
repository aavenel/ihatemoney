"""empty message

Revision ID: aedf9b135394
Revises: f629c8ef4ab0
Create Date: 2017-06-20 22:11:40.860832

"""

# revision identifiers, used by Alembic.
revision = 'aedf9b135394'
down_revision = 'f629c8ef4ab0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.UnicodeText(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tags',
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.Column('bill_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bill_id'], ['bill.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags')
    op.drop_table('tag')
    # ### end Alembic commands ###
