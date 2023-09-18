"""Initial migration.

Revision ID: 88122803c1de
Revises: 
Create Date: 2023-08-02 09:13:07.310212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88122803c1de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_user_last_name'), ['last_name'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_name'), ['name'], unique=False)
        batch_op.create_index(batch_op.f('ix_user_username'), ['username'], unique=True)

    op.create_table('plant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plant_name', sa.String(length=64), nullable=True),
    sa.Column('plant_moisture', sa.Integer(), nullable=True),
    sa.Column('plant_sunlight', sa.String(length=140), nullable=True),
    sa.Column('plant_outside_temp', sa.String(length=140), nullable=True),
    sa.Column('plant_reference', sa.String(length=140), nullable=True),
    sa.Column('plant_grower', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['plant_grower'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('plant', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_plant_plant_name'), ['plant_name'], unique=False)

    op.create_table('flowerpot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('flowerpot_location', sa.String(length=140), nullable=True),
    sa.Column('planted_plant_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['planted_plant_id'], ['plant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('flowerpot')
    with op.batch_alter_table('plant', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_plant_plant_name'))

    op.drop_table('plant')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_user_username'))
        batch_op.drop_index(batch_op.f('ix_user_name'))
        batch_op.drop_index(batch_op.f('ix_user_last_name'))

    op.drop_table('user')
    # ### end Alembic commands ###
