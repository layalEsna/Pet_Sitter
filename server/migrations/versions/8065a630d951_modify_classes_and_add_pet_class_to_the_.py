"""Modify classes and add Pet class to the models.py

Revision ID: 8065a630d951
Revises: 55f229142641
Create Date: 2024-12-31 19:53:55.571481

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8065a630d951'
down_revision = '55f229142641'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pet_name', sa.String(), nullable=True),
    sa.Column('pet_type', sa.Enum('cat', 'dog', 'bird', name='pet_types'), nullable=False),
    sa.Column('owner_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['pet_owners.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.alter_column('duration',
               existing_type=sa.FLOAT(),
               type_=sa.Integer(),
               existing_nullable=False)

    with op.batch_alter_table('pet_owners', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_pet_owners_zip_code'), ['zip_code'], unique=False)
        batch_op.drop_column('pet_name')
        batch_op.drop_column('pet_type')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pet_owners', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pet_type', sa.VARCHAR(), nullable=False))
        batch_op.add_column(sa.Column('pet_name', sa.VARCHAR(), nullable=False))
        batch_op.drop_index(batch_op.f('ix_pet_owners_zip_code'))

    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.alter_column('duration',
               existing_type=sa.Integer(),
               type_=sa.FLOAT(),
               existing_nullable=False)

    op.drop_table('pets')
    # ### end Alembic commands ###
