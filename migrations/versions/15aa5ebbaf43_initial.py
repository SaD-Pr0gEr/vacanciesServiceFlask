"""'initial'

Revision ID: 15aa5ebbaf43
Revises: 
Create Date: 2022-02-27 22:16:31.990855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15aa5ebbaf43'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cities',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('program_languages',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('slug', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('users',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('city', sa.Integer(), nullable=True),
    sa.Column('language', sa.Integer(), nullable=True),
    sa.Column('subscribe_status', sa.Boolean(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('joined_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['city'], ['cities.ID'], ),
    sa.ForeignKeyConstraint(['language'], ['program_languages.ID'], ),
    sa.PrimaryKeyConstraint('ID'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vacancies',
    sa.Column('ID', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('creator', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=1500), nullable=False),
    sa.Column('company_name', sa.String(length=120), nullable=False),
    sa.Column('city', sa.Integer(), nullable=True),
    sa.Column('language', sa.Integer(), nullable=True),
    sa.Column('contacts', sa.String(length=120), nullable=False),
    sa.Column('created_date', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['city'], ['cities.ID'], ),
    sa.ForeignKeyConstraint(['creator'], ['users.ID'], ),
    sa.ForeignKeyConstraint(['language'], ['program_languages.ID'], ),
    sa.PrimaryKeyConstraint('ID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vacancies')
    op.drop_table('users')
    op.drop_table('program_languages')
    op.drop_table('cities')
    # ### end Alembic commands ###
