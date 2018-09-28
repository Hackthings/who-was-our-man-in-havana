"""initial migration

Revision ID: 3b2d804f8ae4
Revises: 
Create Date: 2018-09-28 21:49:24.975076

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b2d804f8ae4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('country',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('capital_city', sa.String(length=150), nullable=True),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('name')
    )
    op.create_table('diplomat',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('birth_year', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('name')
    )
    op.create_table('post',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('role', sa.String(length=150), nullable=True),
    sa.Column('diplomat', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['diplomat'], ['diplomat.uid'], ),
    sa.PrimaryKeyConstraint('uid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post')
    op.drop_table('diplomat')
    op.drop_table('country')
    # ### end Alembic commands ###
