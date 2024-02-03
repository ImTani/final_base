"""updated models for required app, added truck and user

Revision ID: 2976d6b91dde
Revises: cb4b0bdefcaf
Create Date: 2024-02-03 11:45:43.174795

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2976d6b91dde'
down_revision = 'cb4b0bdefcaf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('truck',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('driver_name', sa.String(length=64), nullable=False),
    sa.Column('license_plate', sa.String(length=20), nullable=False),
    sa.Column('schedule', sa.String(length=20), nullable=False),
    sa.Column('current_location', sa.String(length=100), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.Column('last_pickup_time', sa.DateTime(), nullable=False),
    sa.Column('next_pickup_date', sa.DateTime(), nullable=False),
    sa.Column('waste_type', sa.String(length=50), nullable=False),
    sa.Column('route', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('license_plate')
    )
    with op.batch_alter_table('truck', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_truck_driver_name'), ['driver_name'], unique=False)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('location', sa.String(length=100), nullable=False))
        batch_op.add_column(sa.Column('notification_preferences', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('scheduled_pickup_alerts', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('proximity_alerts', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('phone', sa.String(length=15), nullable=False))
        batch_op.add_column(sa.Column('registration_date', sa.DateTime(), nullable=False))
        batch_op.add_column(sa.Column('subscription_status', sa.String(length=20), nullable=False))
        batch_op.add_column(sa.Column('usage_history', sa.String(length=1000), nullable=False))
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.VARCHAR(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DATETIME(), nullable=True))
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
        batch_op.drop_column('usage_history')
        batch_op.drop_column('subscription_status')
        batch_op.drop_column('registration_date')
        batch_op.drop_column('phone')
        batch_op.drop_column('proximity_alerts')
        batch_op.drop_column('scheduled_pickup_alerts')
        batch_op.drop_column('notification_preferences')
        batch_op.drop_column('location')

    with op.batch_alter_table('truck', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_truck_driver_name'))

    op.drop_table('truck')
    # ### end Alembic commands ###
